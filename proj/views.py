from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView

# Create your views here.

class CBView(View):
 
    def get(self, request, *args, **kwargs):
        return HttpResponse('CBView is very good!')

class CBV_viewone(TemplateView):
    template_name = 'proj/viewone.html'
    def get_context_data(self, **kwargs):
         ## pythono3 context = super().get_context_data(**kwargs)
         context = super(CBV_viewone, self).get_context_data(**kwargs)   
         context['injectme'] = 'Basic injection!'
         return context                

def rootindex(request):
    return HttpResponse('Here is websitr root!')

def index(request):
    return render(request, 'proj/index.html')