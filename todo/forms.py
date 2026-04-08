from django import forms
from .models import ToDoItem2

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem2          # どのモデル（テーブル）を使うか
        fields = ['title', 'description']  # どの項目を画面に出すか
