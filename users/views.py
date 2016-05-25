#coding:utf-8
import	json
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	authbase.lib.pwgen	import	CreatePassword
from	authbase.lib.pwmail	import	SendLoginPw,GetEmailList
from	authbase.lib.start	import	CheckAccess
from	authbase.lib.users	import	GetUserList,GetRec,GetDepList,EditUser,AddUser,DelUser
from	forms			import	EditUserForm,StatusList,DelUserForm


import	commands


### --- Список ---
def	List(request):


    if CheckAccess(request,'20') != 'OK':
	return render_to_response("notaccess.html")


    ### --- Строка поиска ---
    try:
	search = request.POST['search']
	request.session['search'] = search
    except:
	pass
	
    try:
	search = request.session['search']
    except:
	search = ''



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

    data = GetUserList(search)

    paginator = Paginator(data,20)
    try:
	data_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
	data_page = paginator.page(paginator.num_pages)


    c = RequestContext(request,{'data':data_page,'search':search})
    c.update(csrf(request))
    return render_to_response("users/list.html",c)






### --- Редактирование учетной записи ---
def	Edit(request):

    error = ''


    if CheckAccess(request,'20') != 'OK':
	return render_to_response("notaccess.html")

    ### --- Код учетной записи ---
    try:
	kod = request.GET['rec_id']
	request.session['rec_id'] = str(kod)
    except:
	pass

    try:
	kod = request.session['rec_id']
    except:
	return HttpResponseRedirect('/users')


    
    if request.method == 'POST':
	form = EditUserForm(request.POST)
	error = form.errors
	if form.is_valid():
	    name1 = form.cleaned_data['name1']
	    name2 = form.cleaned_data['name2']
	    name3 = form.cleaned_data['name3']
	    job = form.cleaned_data['job']
	    phone_shot = form.cleaned_data['phone_shot']
	    phone_city = form.cleaned_data['phone_city']
	    phone_mob = form.cleaned_data['phone_mob']
	    phone_home = form.cleaned_data['phone_home']
	    email = form.cleaned_data['email']
	    dep = form.cleaned_data['dep']
	    status = form.cleaned_data['status']
	    login = form.cleaned_data['login']
	    passwd = form.cleaned_data['passwd']
	    #print form.cleaned_data
	    r = EditUser(kod,name1,name2,name3,job,phone_shot,phone_city,phone_mob,phone_home,email,dep,status,login,passwd)
	    if r == 'OK':
		return HttpResponseRedirect('/users')
    else:
	form = EditUserForm()

    rec = GetRec(kod)
    form.fields['name1'].initial = rec[1]
    form.fields['name2'].initial = rec[2]
    form.fields['name3'].initial = rec[3]
    form.fields['job'].initial = rec[4]
    form.fields['phone_shot'].initial = rec[5]
    form.fields['phone_city'].initial = rec[6]
    form.fields['phone_mob'].initial = rec[7]
    form.fields['phone_home'].initial = rec[8]
    form.fields['email'].initial = rec[9]

#    form.fields['dep'].choices = GetDepList()
    form.fields['dep'].initial = rec[10]

#    form.fields['status'].choices = StatusList()
    form.fields['status'].initial = rec[12]
    
    form.fields['login'].initial = rec[13]
    form.fields['passwd'].initial = rec[14]


    ### --- Отправка логина и пароля по email ---
    if request.method == 'GET':
	try:
	    sendemail = request.GET['sendemail']
	    if rec[9] != '':
		SendLoginPw(rec[9],rec[13],rec[14])
	except:
	    pass

    
    c = RequestContext(request,{'form':form,'error':error})
    c.update(csrf(request))
    return render_to_response("users/edit.html",c)







### --- Создание учетной записи ---
def	New(request):

    error = ''


    if CheckAccess(request,'20') != 'OK':
	return render_to_response("notaccess.html")

    if request.method == 'POST':
	form = EditUserForm(request.POST)
	error = form.errors
	if form.is_valid():
	    name1 = form.cleaned_data['name1']
	    name2 = form.cleaned_data['name2']
	    name3 = form.cleaned_data['name3']
	    job = form.cleaned_data['job']
	    phone_shot = form.cleaned_data['phone_shot']
	    phone_city = form.cleaned_data['phone_city']
	    phone_mob = form.cleaned_data['phone_mob']
	    phone_home = form.cleaned_data['phone_home']
	    email = form.cleaned_data['email']
	    dep = form.cleaned_data['dep']
	    status = form.cleaned_data['status']
	    login = form.cleaned_data['login']
	    passwd = form.cleaned_data['passwd']
	    #print form.cleaned_data
	    r = AddUser(name1,name2,name3,job,phone_shot,phone_city,phone_mob,phone_home,email,dep,status,login,passwd)
	    if r == 'OK':
		return HttpResponseRedirect('/users')
    else:
	form = EditUserForm()
#	form.fields['passwd'].initial = commands.getoutput('authbase/lib/genpass')
	form.fields['passwd'].initial = CreatePassword()


    
    c = RequestContext(request,{'form':form,'error':error})
    c.update(csrf(request))
    return render_to_response("users/new.html",c)






### --- Удаление учетной записи ---
def	Del(request):

    error = ''


    if CheckAccess(request,'20') != 'OK':
	return render_to_response("notaccess.html")

    ### --- Код учетной записи ---
    try:
	kod = request.GET['rec_id']
	request.session['rec_id'] = str(kod)
    except:
	pass

    try:
	kod = request.session['rec_id']
    except:
	return HttpResponseRedirect('/users')

    
    if request.method == 'POST':
	form = DelUserForm(request.POST)
	error = form.errors
	if form.is_valid():
	    name1 = form.cleaned_data['name1']
	    name2 = form.cleaned_data['name2']
	    name3 = form.cleaned_data['name3']
	    job = form.cleaned_data['job']
	    phone_shot = form.cleaned_data['phone_shot']
	    phone_city = form.cleaned_data['phone_city']
	    phone_mob = form.cleaned_data['phone_mob']
	    phone_home = form.cleaned_data['phone_home']
	    email = form.cleaned_data['email']
	    #print form.cleaned_data
	    r = DelUser(kod)
	    if r == 'OK':
		return HttpResponseRedirect('/users')
    else:
	form = DelUserForm()

    rec = GetRec(kod)
    form.fields['name1'].initial = rec[1]
    form.fields['name2'].initial = rec[2]
    form.fields['name3'].initial = rec[3]
    form.fields['job'].initial = rec[4]
    form.fields['phone_shot'].initial = rec[5]
    form.fields['phone_city'].initial = rec[6]
    form.fields['phone_mob'].initial = rec[7]
    form.fields['phone_home'].initial = rec[8]
    form.fields['email'].initial = rec[9]

    form.fields['name1'].widget.attrs['readonly'] = True
    form.fields['name2'].widget.attrs['readonly'] = True
    form.fields['name3'].widget.attrs['readonly'] = True
    form.fields['job'].widget.attrs['readonly'] = True
    form.fields['phone_shot'].widget.attrs['readonly'] = True
    form.fields['phone_city'].widget.attrs['readonly'] = True
    form.fields['phone_mob'].widget.attrs['readonly'] = True
    form.fields['phone_home'].widget.attrs['readonly'] = True
    form.fields['email'].widget.attrs['readonly'] = True


    
    c = RequestContext(request,{'form':form,'error':error})
    c.update(csrf(request))
    return render_to_response("users/del.html",c)







### --- Сервис ---
def	UserDataService(request):


    if request.method == 'GET':
	try:
	    user_id = request.GET['user_id']

	    rec = GetRec(user_id)

	    response_data = {}
	    response_data['user_id'] = user_id
	    response_data['name1'] = rec[1]
	    response_data['name2'] = rec[2]
	    response_data['name3'] = rec[3]
	    response_data['job'] = rec[4]
	    response_data['phone_office'] = rec[5]
	    response_data['phone_mobile'] = rec[6]
	    response_data['phone_city'] = rec[7]
	    response_data['phone_home'] = rec[8]
	    response_data['email'] = rec[9]
	    response_data['department'] = rec[11]
	    response_data['chief'] = rec[12]
	    


	    return HttpResponse(json.dumps(response_data), content_type="application/json")



	except:

	    pass




	try:
	    user_list = request.GET['user_list']
	    
	    data = GetUserList('')
	    
	    response_data = {}

	    for item in data:
		response_data[item[0]] = item


	    return HttpResponse(json.dumps(response_data), content_type="application/json")	    
	
	except:
	    pass





	try:
	    email_list = request.GET['email_list']
	    
	    data = GetEmailList()
	    
	    response_data = {}

	    for item in data:
		response_data[item[0]] = item[1]


	    return HttpResponse(json.dumps(response_data), content_type="application/json")	    
	
	except:
	    pass



    response_data = {}
    response_data['error'] = 'ERROR DATA'

    return HttpResponse(json.dumps(response_data), content_type="application/json")


