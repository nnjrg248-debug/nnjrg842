# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem2
from .forms import ToDoForm

# ToDoアイテムのリストを取得
def todo_list(request):
    todos =ToDoItem2.objects.all()#'123'等文字列とか代入するとHPでエラーとなる
    return render(request, 'todo_list.html', {'todos': todos})

# ToDoアイテムを追加
def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'add_todo.html', {'form': form})

# 既存のToDoアイテムを編集
def edit_todo(request, todo_id):
    todo = ToDoItem2.objects.get(pk=todo_id)#pkとはid列のこと、慣習（作法）としてpkとかく（本来はidと書くべきだが、かぶるからとかだろう）
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form, 'todo_id': todo_id})

# ToDoアイテムを削除
def delete_todo(request, todo_id):
    todo = ToDoItem2.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')
#renderとredirectの違い　renderはurlファイル名とオブジェクトを指定（ファイルに合わせたオブジェクトの表示）、redirectは直接URL(のあだ名)を指定するだけ

def renshu(request):    
    return render(request, 'renshu.html')
    #return redirect('todo_list')