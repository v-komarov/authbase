#coding:utf-8
import	datetime

from	django	import	forms
from	django.forms.extras.widgets	import	SelectDateWidget


from	authbase.lib.users	import	GetDepList
from	authbase.lib.mydata	import	GetStatusList

year = range(1960,datetime.date.today().year+1)


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
    dep = forms.ChoiceField(label='Дирекция\Отдел',choices=GetDepList(),required=False)
    status = forms.ChoiceField(label='Статус',choices=StatusList(),required=False)
    login = forms.CharField(label='Логин')
    passwd = forms.CharField(label='Пароль')



### --- Форма загрузки файла с фото ---
class	LoadPhotoForm(forms.Form):
    file_load = forms.FileField(label='Загрузить файл (*.jpg,*.tif)',widget=forms.FileInput,required=False)


### --- Новая дата ---
class	DateForm(forms.Form):
    fiesta = forms.CharField(label='Событие *',widget=forms.TextInput(attrs={'class':'g-4',}))
    date = forms.DateField(label='Дата *',widget=SelectDateWidget(years=year),initial=datetime.date.today())


### --- Форма установки статуса ---
class	StatusForm(forms.Form):
    status = forms.ChoiceField(label='Статус *',choices=GetStatusList())
