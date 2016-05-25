#coding:utf-8

from	django.db	import	connections, transaction



### --- Получение списка модулей ---
def	GetModList():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_access_list;")
    data = cursor.fetchall()
    
    return data
    

### --- Переименование доступа ---
def	EditAccessName(kod,name):
    kod = kod.encode("utf-8")
    name = name.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_EditAccessName(%s,'%s');" % (kod,name))
    transaction.commit_unless_managed()
    data = cursor.fetchone()

    return data[0]

### --- Получение записи ---
def	GetRec(kod):
    kod = kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_access_list WHERE t_rec_id=%s;" % (kod))
    data = cursor.fetchone()
    
    return data



### --- Создание доступа ---
def	AddAccessName(name):
    name = name.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_AddAccessName('%s');" % (name))
    transaction.commit_unless_managed()
    data = cursor.fetchone()

    return data[0]
