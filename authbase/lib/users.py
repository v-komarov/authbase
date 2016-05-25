#coding:utf-8

from	django.db	import	connections, transaction
from	cryptpass	import	Encoded





### --- Получение списка пользователей ---
def	GetUserList(search):
    cursor = connections['default'].cursor()
    if search == '':
	cursor.execute("SELECT * FROM t_show_user_list;")
    else:
	cursor.execute("""SELECT * FROM t_show_user_list \
	WHERE \
	to_tsvector('russian',name1) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',name2) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',name3) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',t_user_job) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',phone_shot) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',department_name) @@ to_tsquery('russian','%s') \
	;""" % (search,search,search,search,search,search))
	
	
    data = cursor.fetchall()
    return data





### --- Получение записи ---
def	GetRec(kod):
    kod = kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_user_list WHERE user_kod='%s';" % (kod))
    data = cursor.fetchone()
    
    return data





### --- Получение списка дирекций\записи ---
def	GetDepList():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_dep_list;")
    data = cursor.fetchall()
    
    return data





### --- Изменение учетной записи ---
def	EditUser(kod,name1,name2,name3,job,phone_shot,phone_city,phone_m,phone_h,email,dep_kod,status_kod,login,passwd):
    kod = kod.encode("utf-8")
    name1 = name1.encode("utf-8")
    name2 = name2.encode("utf-8")
    name3 = name3.encode("utf-8")
    job = job.encode("utf-8")
    phone_shot = phone_shot.encode("utf-8")
    phone_city = phone_city.encode("utf-8")
    phone_m = phone_m.encode("utf-8")
    phone_h = phone_h.encode("utf-8")
    email = email.encode("utf-8")
    dep_kod = dep_kod.encode("utf-8")
    status_kod = status_kod.encode("utf-8")
    login = login.encode("utf-8")
    passwd = passwd.encode("utf-8")
    if len(passwd)>10 and passwd[-1] == '=':
	pass
    else:
	passwd = Encoded(passwd)
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_EditUserAB('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,'%s','%s');" % (kod,name1,name2,name3,job,phone_shot,phone_city,phone_m,phone_h,email,dep_kod,status_kod,login,passwd))
    transaction.commit_unless_managed()
    data = cursor.fetchone()

    return data[0]





### --- Создание учетной записи ---
def	AddUser(name1,name2,name3,job,phone_shot,phone_city,phone_m,phone_h,email,dep_kod,status_kod,login,passwd):
    name1 = name1.encode("utf-8")
    name2 = name2.encode("utf-8")
    name3 = name3.encode("utf-8")
    job = job.encode("utf-8")
    phone_shot = phone_shot.encode("utf-8")
    phone_city = phone_city.encode("utf-8")
    phone_m = phone_m.encode("utf-8")
    phone_h = phone_h.encode("utf-8")
    email = email.encode("utf-8")
    dep_kod = dep_kod.encode("utf-8")
    status_kod = status_kod.encode("utf-8")
    login = login.encode("utf-8")
    passwd = Encoded(passwd.encode("utf-8"))
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_AddUserAB('%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,'%s','%s');" % (name1,name2,name3,job,phone_shot,phone_city,phone_m,phone_h,email,dep_kod,status_kod,login,passwd))
    transaction.commit_unless_managed()
    data = cursor.fetchone()

    return data[0]





### --- Удаление учетной записи ---
def	DelUser(kod):
    kod = kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_DelUserAB('%s');" % (kod))
    transaction.commit_unless_managed()
    data = cursor.fetchone()

    return data[0]
