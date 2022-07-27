from django.urls import path
from .views import HomePage,Success, RedirectLink, Linkstats, Terms, report

urlpatterns = [
    path('',HomePage.as_view(),name="homepage"),
    path('success/',Success.as_view(),name="success"),
    path('terms/',Terms.as_view(),name="terms"),
    path('report/',report.as_view(),name="report"),
    path('<str:link>',RedirectLink,name="redirect"),
    path('stats/<slug:link>',Linkstats.as_view(),name="linkstats")
    
]
