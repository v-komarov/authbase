#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	forms			import	FilterForm
from	authbase.lib.phone	import	GetDepStru,GetPhoneUser



### --- Список ---
def	List(request):



    try:
	search = request.session['searchy']
	dep = request.session['dep']
    except:
	search = ''
	dep = '1'



    try:
	search = request.POST['search']
	dep = request.POST['dep']
	request.session['searchy'] = search
	request.session['dep'] = dep
    except:
	pass



    
    form = FilterForm()

    form.fields['search'].initial = search
    form.fields['dep'].initial = dep

    stru = GetDepStru()
    try:
	data = GetPhoneUser(search,dep)
    except:
	data = []

    c = RequestContext(request,{'data':data,'form':form,'dep':stru,'dep_kod':eval(dep)})
    c.update(csrf(request))
    return render_to_response("phone/list.html",c)





