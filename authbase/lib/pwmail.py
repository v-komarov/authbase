#coding:utf-8

from	django.db	import	connections, transaction
from	django.core.mail	import	send_mail
from	cryptpass		import	Decoded


### --- Получение логина и пароля ---
def	GetLoginPw(email):
    email = email.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT count(*) FROM t_show_user_list WHERE upper(btrim(email))=upper(btrim('%s'));" % (email))
    data = cursor.fetchone()
    
    if data[0] == 0:
	return 'ERRORUSER'
    
    cursor = connections['default'].cursor()
    cursor.execute("SELECT login,passwd FROM t_show_user_list WHERE upper(btrim(email))=upper(btrim('%s'));" % (email))
    data = cursor.fetchone()
    
    
    return data
    


### --- Отправка логина и пароля ---
def	SendLoginPw(email,login,passwd):

    passwd = Decoded(passwd)

    address = []
    address.append(email)
    m = u"Доступ КИС,ТИС,AuthBase\n\nКИС http://10.6.0.80:8000\nТИС http://10.6.0.250:8000\nAuthBase http://10.6.0.223:20000\nSCatalog http://10.6.1.10:8000\n\nЛогин %s\nПароль %s" % (login,passwd)
    send_mail('KIS,TIS Login&Password',m,'it@sibit.ttk.ru',address)



### --- Получение списка email адресов ---
def	GetEmailList():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT email,name2||' '||name1 FROM t_show_user_list WHERE email!='' ORDER BY name2,name1;")
    data = cursor.fetchall()
    
    return data

