from django.urls import path, include
from . views import TodoUpdate, Todolist, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', Todolist.as_view(), name='list'),
    #primarity_key を含めることによってどのモデルを対象にすれば良いのかを迷わなくなる
    #DetaiViewは個別のデータを対象としているのでこのような記載が必要となる
    #一般的にprimarty_keyは整数型なのでint:とする
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('create/',TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update')
]
