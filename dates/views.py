#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	django.core.paginator	import	Paginator, InvalidPage, EmptyPage

from	authbase.lib.dates	import	GetDatesList



### --- Список ---
def	List(request):


    data = GetDatesList()

    c = RequestContext(request,{'data':data})
    c.update(csrf(request))
    return render_to_response("dates/dates.html",c)



