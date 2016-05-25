#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	authbase.lib.start	import	CheckAccess
from	authbase.lib.modules	import	GetModList,GetRec,EditAccessName,AddAccessName



### --- Список модулей доступа ---
def	List(request):


    if CheckAccess(request,'1') != 'OK':
	return render_to_response("notaccess.html")

    data = GetModList()

    ### --- Получение номера страницы ---
    try:
	page = int(request.GET.get('page',1))
	request.session['page'] = page
    except:
	pass
	
    try:
	page = int(request.session['page'])
    except:
	page = 1

    paginator = Paginator(data,15)
    try:
	data_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
	data_page = paginator.page(paginator.num_pages)


    c = RequestContext(request,{'data':data_page})
    c.update(csrf(request))
    return render_to_response("modules/list.html",c)






### --- Переименование модуля ---
def	EditName(request):


    if CheckAccess(request,'1') != 'OK':
	return render_to_response("notaccess.html")

    try:
	kod = request.POST['kod']
	name = request.POST['name']
	if EditAccessName(kod,name) == 'OK':
	    return HttpResponseRedirect('/modules')
    except:
	pass



    if request.method == 'GET':
	rec_id = request.GET['rec_id']
	data = GetRec(rec_id)
	request.session['rec_id'] = rec_id
	c = RequestContext(request,{'kod':data[0],'name':data[1]})
	c.update(csrf(request))
	return render_to_response("modules/editname.html",c)
	
    try:
	rec_id = request.session['rec_id']
	data = GetRec(rec_id)
	c = RequestContext(request,{'kod':data[0],'name':data[1]})
	c.update(csrf(request))
	return render_to_response("modules/editname.html",c)
    except:
	pass



    c = RequestContext(request,{})
    c.update(csrf(request))
    return render_to_response("modules/editname.html",c)







### --- Добавление модуля ---
def	AddName(request):


    if CheckAccess(request,'1') != 'OK':
	return render_to_response("notaccess.html")


    try:
	name = request.POST['name']
	if AddAccessName(name) == 'OK':
	    return HttpResponseRedirect('/modules')
    except:
	pass



    c = RequestContext(request,{})
    c.update(csrf(request))
    return render_to_response("modules/addname.html",c)
