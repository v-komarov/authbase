#coding:utf-8

from	django.db	import	connections, transaction



### --- Получение списка телефонов пользователей ---
def	GetPhoneUser(search,dep):
    search = search.replace(' ','')
    search = search.encode("utf-8")
    dep = dep.encode("utf-8")
    cursor = connections['default'].cursor()


    if search == '':
	cursor.execute("""\
	SELECT * FROM t_show_user_list WHERE to_number(department_kod,'9999999') IN \
	(WITH RECURSIVE included_departs(id, parent, dname, notes, level, path) AS (\
	SELECT t.t_rec_id, t.t_department_parent, t.t_department_name, t_notes, 0, ''   \
	FROM t_department_list t \
	WHERE t.t_rec_id=%s AND t.t_rec_delete=0 \
	UNION ALL \
	SELECT p.t_rec_id, p.t_department_parent, p.t_department_name, p.t_notes, pr.level+1, path || '>' || p.t_department_name\
	FROM included_departs pr, t_department_list p \
	WHERE p.t_department_parent = pr.id AND p.t_rec_delete=0) \
	SELECT id FROM included_departs ORDER BY path);""" % (dep))
	
    else:
	cursor.execute("""\
	SELECT * FROM t_show_user_list WHERE (\
	to_tsvector('russian',name1) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',name2) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',name3) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',t_user_job) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',department_name) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',phone_shot) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',phone_city) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',phone_m) @@ to_tsquery('russian','%s:*') OR \
	to_tsvector('russian',phone_h) @@ to_tsquery('russian','%s:*') \
	) AND \
	to_number(department_kod,'9999999') IN \
	(WITH RECURSIVE included_departs(id, parent, dname, notes, level, path) AS (\
	SELECT t.t_rec_id, t.t_department_parent, t.t_department_name, t_notes, 0, ''  \
	FROM t_department_list t \
	WHERE t.t_rec_id=%s AND t.t_rec_delete=0 \
	UNION ALL \
	SELECT p.t_rec_id, p.t_department_parent, p.t_department_name, p.t_notes, pr.level+1, path || '>' || p.t_department_name\
	FROM included_departs pr, t_department_list p \
	WHERE p.t_department_parent = pr.id AND p.t_rec_delete=0) \
	SELECT id FROM included_departs ORDER BY path);""" % (search,search,search,search,search,search,search,search,search,dep))
    
    data = cursor.fetchall()
	
    return data





### --- Структура ---
def	GetDepStru(dep_id='1'):
    cursor = connections['default'].cursor()
    cursor.execute("""WITH RECURSIVE included_departs(id, parent, dname, notes, level, path) AS (\
    SELECT t.t_rec_id, t.t_department_parent, t.t_department_name, t_notes, 0, ''  \
    FROM t_department_list t \
    WHERE t.t_rec_id=%s AND t.t_rec_delete=0 \
    UNION ALL \
    SELECT p.t_rec_id, p.t_department_parent, p.t_department_name, p.t_notes, pr.level+1, path || '>' || p.t_department_name\
    FROM included_departs pr, t_department_list p \
    WHERE p.t_department_parent = pr.id AND p.t_rec_delete=0) \
    SELECT * FROM included_departs ORDER BY path;""" % (dep_id.encode('utf-8')))
    data = cursor.fetchall()
    
    result = []
    
    for item in data:
	result.append([item[0],'&nbsp;&nbsp;&nbsp;&nbsp;'*item[4] + item[2]],)

    result[0] = [1,'Bce']

    return result
