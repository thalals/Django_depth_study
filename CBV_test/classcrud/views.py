from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView      # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가
from .models import ClassBlog

class BlogView(ListView):       #블로그 리스트를 담은 html * html(default) :(소문자모델)_list.html
    model = ClassBlog

class BlogCreate(CreateView):   #form (입력공간)을 갖고있는 html * html(default) :(소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView): #상세 페이지를 담은 html * html(default) :(소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView): #form (입력공간)을 갖고있는 html * html(default) :(소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):   #삭제 * html(default) :(소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')
