from django import forms
from .models import Links, Reports
class GetLink(forms.ModelForm):
    # thelink = forms.CharField(max_length=250)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['org_link'].widget.attrs.update({'class':'form-control','placeholder':'لینک را وارد کنید'})

    def __str__(self):
        return str(self.fields['org_link'])
    class Meta:
        model = Links
        fields = ['org_link']
    
class makeReport(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = ""

    class Meta:
        model = Reports
        fields = ['name','email','description']

