#coding:utf-8

from	django.db	import	connections, transaction
from	cryptpass	import	Encoded


### --- регистация пользователя в базе по логину и паролю ---
def	CheckUser(login,password):
    password = Encoded(password)
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_CheckUser('%s','%s','authbase');" % (login,password))
    data = cursor.fetchone()
    
    return data[0]
    

### --- Получение фио, телефона, email ---
def	GetUserData(request):
    sess = request.session['key009']

    cursor = connections['default'].cursor()
    cursor.execute("SELECT name1,name2,name3,phone_shot,email FROM t_show_user_list WHERE session='%s';" % (sess))
    data = cursor.fetchone()

    request.session['fio'] = data[0]+' '+data[1]+' '+data[2]
    request.session['phone'] = data[3]
    request.session['email'] = data[4]

    return 0



### --- Проверка доступа к модулям ---
def	CheckAccess(request,mod):
    try:
	sess = request.session['key009']
	sess.split('#')[3].index(mod)
	return 'OK'
    except:
	return 'NOTACCESS'
	


### --- Вспомогательная функция зашифровки паролей ---
def	PassCrypt():    
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_rec_id,t_passwd FROM t_user_list;")
    data = cursor.fetchall()

    for row in data:
	row_id = row[0]
	passwd = Encoded(row[1].encode('utf-8'))
	cursor.execute("UPDATE t_user_list SET t_passwd=%s WHERE t_rec_id=%s;", [passwd,row_id])
	transaction.commit_unless_managed()
	