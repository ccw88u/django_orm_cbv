# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from . import models
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

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


########################公司資訊 簡目 / 列出成員 / 新增 / 刪除 / 修改{S}########################
## 公司資訊 (簡目)
class companyListView(ListView):
    context_object_name = 'companys'
    model = models.company

## 公司資訊 + 成員資訊
class companyDetailView(DetailView):
    context_object_name = 'company_details'
    model = models.company
    template_name = 'proj/company_detail.html'

## 新增
class companyCreateView(CreateView):
    ## default html company_form.html
    fields = ("name","tel","location")
    model = models.company

## 修改
class companyUpdateView(UpdateView):
    fields = ("name","tel")
    model = models.company

## 刪除
class companyDeleteView(DeleteView):
    context_object_name = 'company_details'
    model = models.company
    success_url = reverse_lazy("list")
    
########################公司資訊 簡目 / 列出成員 / 新增 / 刪除 / 修改{E}########################