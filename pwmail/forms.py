#coding:utf-8

import	datetime

from	django	import	forms
from	django.forms.extras.widgets	import	SelectDateWidget


from	authbase.lib.pwmail		import	GetEmailList


emaillist = GetEmailList()
emaillist.insert(0,['',''])


class	PwMailForm(forms.Form):
    email = forms.ChoiceField(label='Пользователь *',choices=emaillist)
    def	__init__(self,*args,**kwargs):
	super(PwMailForm,self).__init__(*args,**kwargs)
	email = forms.ChoiceField(label='Пользователь *',choices=emaillist)
