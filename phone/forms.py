#coding:utf-8

from	django	import	forms

from	authbase.lib.phone	import	GetDepStru

class	FilterForm(forms.Form):
    search = forms.CharField(label='Строка поиска',required=False)
    dep = forms.ChoiceField(label='Отдел/Дирекция',choices=GetDepStru())




