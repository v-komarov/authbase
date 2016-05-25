#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	authbase.lib.start	import	CheckUser, GetUserData


def	Home(request):

    error = 'OK'

    ### --- Получение логина и пароля ---
    try:
	login = request.POST['login']
	password = request.POST['password']
	if login != '' and password != '':
	    sess = CheckUser(login,password)
	    if sess != 'ERRORUSER':
		request.session['key009'] = sess
		GetUserData(request)
		c = {'fio':request.session['fio'],'phone':request.session['phone'],'email':request.session['email']}
		c.update(csrf(request))
		return render_to_response("start/begin.html",c)
	    else:
		error = 'Неправильные логин или пароль!'
	    pass
    except:
	pass


    c = RequestContext(request,{'error':error})
    c.update(csrf(request))
    return render_to_response("start/start.html",c)



def	Exit(request):

    del request.session['key009']

    return HttpResponseRedirect('/')
    