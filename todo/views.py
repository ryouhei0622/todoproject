from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
# Create your views here.

class Todolist(ListView):
    #どのhtmlファイルを使用するかを指定する
    template_name = 'list.html'
    #models.pyの中でどのモデルを使用するかを指定する
    #作成したデータの保存先を指定するためにmodel = TodoModelとしている
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # データが作成された時に遷移するurlを定義する
    #reverseを用いることによってurlに従って呼び出されるという流れが
    #反転してlistをもとに反対に流れが進んでいく
    #つまり引数でありるlistをurls.pyで指定する
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    #以下でどのモデルのデータを削除するのかを指定する
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')