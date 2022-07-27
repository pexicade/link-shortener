from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView,TemplateView, FormView
from .forms import GetLink,makeReport
from .models import Links
from django.urls import reverse

import random
# Create your views here.

class HomePage(FormView):

    template_name = "shortit/homepageview.html"
    form_class = GetLink

    def get(self, request, *args, **kwargs):
        print("***GET")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print("***POST",request.session)
        form = self.form_class(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            a=0
            try:
                obj = Links.objects.get(org_link=f.org_link)
                request.session['link'] = obj.short_link     
                # request.session['pk']
                return redirect('success')
            except Links.DoesNotExist:
                print('doesnt exist')
            f.org_link = change_link(f.org_link)
            f.short_link = create_link()
            request.session['link'] = f.short_link
            f.save()
            return redirect('success')
        else:
            print(form.errors)
        
        return render(request, self.template_name, {'form': form})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = self.request.session['link']
        return context
        

class Success(TemplateView):
    template_name = 'shortit/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link'] = self.request.session['link']
        # context['pk'] = 
        # print('get: ',self.request.GET.get('amar',None))
        # if self.request.GET.get('amar',None) != None:
        #     print('hi')
        #     return redirect('linkstats',self.request.GET.get('amar',None))
        # obj = Links.objects.get(short_link=context['link'])
        # obj.stats+=1
        # obj.save()
        return context

def RedirectLink(request,link):
    try:
        obj = Links.objects.get(short_link=link)
        obj.stats+=1
        obj.save()
        Links.DoesNotExist
        return HttpResponseRedirect(obj.org_link)
    except Links.DoesNotExist:
        return redirect('homepage')


class Linkstats(DetailView):
    template_name= "shortit/linkstats.html"
    model = Links
    obj = ""
    def get_object(self):
        try:
            obj = Links.objects.get(short_link=self.kwargs['link'])
            return obj
        except Links.DoesNotExist:
            print('Doesnt exist')
    def get_context_data(self,**kwargs):
        print('hello')
        context = super().get_context_data(**kwargs)
        context['created'] = context['object'].created
        context['stats'] = context['object'].stats
        print(context)
        # return render(self.request,self.template_name,{'conte'})
        return context
    # def get(self,request,*args, **kwargs):
    #     print("***LINK GET*")

class Terms(TemplateView):
    template_name = 'shortit/terms.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class report(FormView):
    template_name = 'shortit/takhallof.html'
    form_class = makeReport
    msg = ''
    def get(self,request,*args, **kwargs):
        print("*F GET ")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # print('f: ',form)
        return render(request,self.template_name,{'form':form,'msg':'get'})
    
    def post(self,request,*args, **kwargs):
        print("*F POST")
        form = self.form_class(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=True)
            msg = 'valid'
        else:
            print('err:',form.errors)
            # request.session['msg'] = 
            msg = form.errors

        return render(request,self.template_name,{'form':form,'msg':msg})
        



def create_link():
    letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    
    n = random.randint(0,26)
    link = letters[n]
    for _ in range(0,5):
        n = random.randint(0,9)
        link += str(n)
    print('link: ',link)
    return link

def change_link(link):
    print('link: '+link)
    if not link.startswith("http://") and not link.startswith("https://"):
        link = "http://"+link
    return link