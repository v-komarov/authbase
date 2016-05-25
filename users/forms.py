#coding:utf-8

from	django	import	forms

from	authbase.lib.users	import	GetDepList


def	StatusList():
    status_list = (
	('0','Сотрудник'),
	('1','Руководитель'),
    )
    return status_list


class	EditUserForm(forms.Form):
    name1 = forms.CharField(label='Фамилия')
    name2 = forms.CharField(label='Имя')
    name3 = forms.CharField(label='Отчество')
    job = forms.CharField(label='Должность')
    phone_shot = forms.CharField(label='Телефон внутренний')
    phone_city = forms.CharField(label='Телефон городской',required=False)
    phone_mob = forms.CharField(label='Телефон мобильный',required=False)
    phone_home = forms.CharField(label='Телефон домашний',required=False)
    email = forms.CharField(label='Email')
    dep = forms.ChoiceField(label='Дирекция\Отдел',choices=GetDepList())
    status = forms.ChoiceField(label='Статус',choices=StatusList())
    login = forms.CharField(label='Логин')
#    passwd = forms.CharField(label='Пароль',widget=forms.PasswordInput)
    passwd = forms.CharField(label='Пароль')




class	DelUserForm(forms.Form):
    name1 = forms.CharField(label='Фамилия')
    name2 = forms.CharField(label='Имя')
    name3 = forms.CharField(label='Отчество')
    job = forms.CharField(label='Должность')
    phone_shot = forms.CharField(label='Телефон внутренний')
    phone_city = forms.CharField(label='Телефон городской',required=False)
    phone_mob = forms.CharField(label='Телефон мобильный',required=False)
    phone_home = forms.CharField(label='Телефон домашний',required=False)
    email = forms.CharField(label='Email')

