#coding:utf-8

from	django.db	import	connections, transaction



### --- Получение списка модулей с доступом ---
def	GetAccessUser(search,modul):
    search = search.encode("utf-8")
    modul = modul.encode("utf-8")
    cursor = connections['default'].cursor()


    if search == '':
	cursor.execute("SELECT * FROM t_show_access_user WHERE al_kod='%s';" % (modul))
    else:
	cursor.execute("""SELECT * FROM t_show_access_user \
	WHERE al_kod='%s' AND (\
	to_tsvector('russian',name1) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',name2) @@ to_tsquery('russian','%s') OR \
	to_tsvector('russian',name3) @@ to_tsquery('russian','%s')) \
	;""" % (modul,search,search,search))
	
	
    data = cursor.fetchall()
    
    return data
    


def	AddDelAccess(user_kod,access_kod):
    user_kod = user_kod.encode("utf-8")
    access_kod = access_kod.encode("utf-8")
    cursor = connections['default'].cursor()
    cursor.execute("SELECT t_AddDelAccess('%s',%s);" % (user_kod,access_kod))
    transaction.commit_unless_managed()
    data = cursor.fetchone()
    return data[0]

