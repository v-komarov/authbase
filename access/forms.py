#coding:utf-8

from	django	import	forms

from	authbase.lib.modules	import	GetModList


class	FilterForm(forms.Form):
    search = forms.CharField(label='Строка поиска',required=False)
    modul = forms.ChoiceField(label='Модуль',choices=GetModList())

    def	__init__(self, *args, **kwargs):
	super(FilterForm,self).__init__(*args,**kwargs)
	self.fields['modul'].choices = GetModList()

