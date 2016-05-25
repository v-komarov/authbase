#coding:utf-8
import	psycopg2
from	django.db	import	connections, transaction



### --- Получение кода записи ---
def	GetUserKod(request):
    
    kod = request.session['key009'].split('#')[0]
    
    return kod


### --- Загрузка фотографии ---
def	LoadPhotoFile(user_kod,file_name,file_ext,file_data):
    user_kod = user_kod.encode("utf-8")
    file_name = file_name.encode("utf-8")
    file_ext = file_ext.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("UPDATE t_user_list SET t_photo=%s,t_photo_filename=%s,t_photo_ext=%s WHERE t_rec_id=%s;", (psycopg2.Binary(file_data),file_name,file_ext,user_kod),)
    transaction.commit_unless_managed()


### --- Получение фатографии из базы ---
def	GetPhotoData(user_kod):
    user_kod = user_kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_photo,t_photo_filename,t_photo_ext FROM t_user_list WHERE t_rec_id='%s';" % (user_kod))
    data = cursor.fetchone()
    return data


### --- Добавление даты ---
def	NewFiesta(user_kod,date,fiesta):
    user_kod = user_kod.encode("utf-8")
    fiesta = fiesta.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("INSERT INTO t_user_fiestas(t_fiesta_date,t_fiesta_name,t_user_kod) VALUES('%s','%s','%s');" % (date,fiesta,user_kod))
    transaction.commit_unless_managed()


### --- Удаление даты ---
def	DelFiesta(rec_kod):
    rec_kod = rec_kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("DELETE FROM t_user_fiestas WHERE t_rec_id=%s;" % (rec_kod))
    transaction.commit_unless_managed()


### --- Получение списка дат ---
def	GetDateList(user_kod):
    user_kod = user_kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_user_fiestas WHERE user_kod='%s';" % (user_kod))
    data = cursor.fetchall()
    return data


### --- Получение списка статусов ---
def	GetStatusList():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_user_status_list;")
    data = cursor.fetchall()
    return data


### --- Установка нового статуса ---
def	NewStatus(user_kod,status_kod):
    user_kod = user_kod.encode("utf-8")
    status_kod = status_kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("UPDATE t_user_list SET t_status_kod=%s WHERE t_rec_id='%s';" % (status_kod,user_kod))
    transaction.commit_unless_managed()

