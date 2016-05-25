#coding:utf-8

from	django.db	import	connections, transaction



### --- Получение списка дат на сегодня ---
def	GetDatesList():
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM t_show_user_dates;")
    data = cursor.fetchall()
    
    return data
    
