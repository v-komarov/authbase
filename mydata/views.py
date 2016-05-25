#coding:utf-8
import	os.path
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	authbase.lib.start	import	CheckAccess
from	authbase.lib.users	import	GetUserList,GetRec,GetDepList,EditUser
from	authbase.lib.mydata	import	GetUserKod,LoadPhotoFile,GetPhotoData,NewFiesta,DelFiesta,GetDateList,NewStatus
from	forms			import	EditUserForm,StatusList,LoadPhotoForm,DateForm,StatusForm


### --- Изменение учетной записи ---
def	EditMyData(request):


    ### --- Получение кода учетной записи ---
    try:
	kod = GetUserKod(request)
    except:
	return HttpResponseRedirect('/')
	#return render_to_response("notaccess.html")

    error = ''


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
	    rec = GetRec(kod)
	    r = EditUser(kod,name1,name2,name3,job,phone_shot,phone_city,phone_mob,phone_home,email,rec[10],rec[12],login,passwd)


    form = EditUserForm(None)

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
    form.fields['dep'].initial = rec[10]
    form.fields['status'].initial = rec[12]
    form.fields['login'].initial = rec[13]
    form.fields['passwd'].initial = rec[14]

    form.fields['dep'].widget.attrs['disabled'] = True
    form.fields['status'].widget.attrs['disabled'] = True

    c = RequestContext(request,{'form':form,'error':error})
    c.update(csrf(request))
    return render_to_response("mydata/editmydata.html",c)




### --- Фотография ---
def	MyPhoto(request):


    ### --- Получение кода учетной записи ---
    try:
	kod = GetUserKod(request)
    except:
	return render_to_response("notaccess.html")


    if request.method == 'POST':
	form = LoadPhotoForm(request.POST)
	if form.is_valid():
	    try:
		file_name = request.FILES['file_load'].name
		file_data = request.FILES['file_load'].read()
		file_name = file_name.split('\\')[-1]
		(path,ext) = os.path.splitext(file_name)
		file_name = file_name.replace(' ','_')
		file_ext = ext
		if file_ext.lower() == '.jpg' or file_ext.lower() == '.tif':
		    LoadPhotoFile(kod,file_name,file_ext,file_data)
	    except:
		pass


    form = LoadPhotoForm(None)

    c = RequestContext(request,{'form':form,'kod':kod})
    c.update(csrf(request))
    return render_to_response("mydata/myphoto.html",c)





### --- Фотография ---
def	MyPhotoShow(request):



    ### --- Получение кода учетной записи ---
    try:
	kod = request.GET['user_id']
	#kod = GetUserKod(request)
    except:
	return render_to_response("notaccess.html")


    ### --- Данные фото ---
    d = GetPhotoData(kod)

    response = HttpResponse(content_type='application/%s' % d[2][-1:])
    attach = u'attachment; filename=\"%s\"' % (d[1])
    response['Content-Disposition'] = attach.encode('utf-8')
    response.write(d[0])
    return response




### --- Даты ---
def	MyFiestas(request):


    ### --- Получение кода учетной записи ---
    try:
	kod = GetUserKod(request)
    except:
	return render_to_response("notaccess.html")


    if request.method == 'POST':
	form = DateForm(request.POST)
	if form.is_valid():
	    fiesta = form.cleaned_data['fiesta']
	    date = form.cleaned_data['date']
	    NewFiesta(kod,date,fiesta)

    if request.method == 'GET':
	try:
	    delete_id = request.GET['delete_fiesta']
	    DelFiesta(delete_id)
	except:
	    pass

    form = DateForm(None)

    data = GetDateList(kod)

    c = RequestContext(request,{'form':form,'data':data})
    c.update(csrf(request))
    return render_to_response("mydata/fiestas.html",c)





### --- Статус ---
def	MyStatus(request):


    ### --- Получение кода учетной записи ---
    try:
	kod = GetUserKod(request)
    except:
	return render_to_response("notaccess.html")


    if request.method == 'POST':
	form = StatusForm(request.POST)
	if form.is_valid():
	    status = form.cleaned_data['status']
	    NewStatus(kod,status)
    ## --- Данные учетной записи ---
    r = GetRec(kod)

    form = StatusForm(None)

    c = RequestContext(request,{'form':form,'r':r})
    c.update(csrf(request))
    return render_to_response("mydata/status.html",c)

