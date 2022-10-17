from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class HodimlarPageView(TemplateView):
    template_name = 'hodimlar.html'

class YuldashevaPageView(TemplateView):
    template_name = 'yuldasheva.html'

class TuychievPageView(TemplateView):
    template_name = 'tuychiev.html'

class ZiyodulloPageView(TemplateView):
    template_name = 'ziyodullo.html'

class BulimlarPageView(TemplateView):
    template_name = 'bulimlar.html'