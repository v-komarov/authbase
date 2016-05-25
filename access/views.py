#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	authbase.lib.start	import	CheckAccess
from	authbase.lib.access	import	GetAccessUser,AddDelAccess
from	forms			import	FilterForm



### --- Список ---
def	List(request):



    if CheckAccess(request,'19') != 'OK':
	return render_to_response("notaccess.html")

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


    try:
	search = request.session['searchx']
	modul = request.session['modul']
    except:
	search = ''
	modul = '1'



    if request.method == 'POST':
	form = FilterForm(request.POST)
	if form.is_valid():
	    search = form.cleaned_data['search']
	    modul = form.cleaned_data['modul']
	    request.session['searchx'] = search
	    request.session['modul'] = modul
    else:
	form = FilterForm()



    form.fields['search'].initial = search
    form.fields['modul'].initial = modul


    data = GetAccessUser(search,modul)
    
    paginator = Paginator(data,50)
    try:
	data_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
	data_page = paginator.page(paginator.num_pages)


    



    c = RequestContext(request,{'data':data_page,'form':form})
    c.update(csrf(request))
    return render_to_response("access/list.html",c)






def	Switch(request):

    if request.method == 'GET':
	userkod = request.GET['userkod']
	accesskod = request.GET['accesskod']
	
	if AddDelAccess(userkod,accesskod) == 'ON':
	    switch = u'ВКЛЮЧЕНО'
	else:
	    switch = u'ОТКЛЮЧЕНО'
	
	ans = u"""
	    <td id=\"%s%s\"> \
		<a href="#" \
		onclick="new Ajax.Updater('%s%s','/switch?userkod=%s&accesskod=%s',{ method : 'GET' });" \
		style="color: blue;" \
		>%s</a> \
		\
	    </td> \
	""" % (userkod,accesskod,userkod,accesskod,userkod,accesskod,switch)
	

    return HttpResponse(ans)


