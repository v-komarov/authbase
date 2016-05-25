#coding:utf-8
from	django.http	import	HttpResponse
from	django.http	import	HttpResponseRedirect
from	django.template	import	Context, loader, RequestContext
from	django.core.context_processors	import	csrf
from	django.shortcuts	import	render_to_response

from	authbase.lib.pwmail	import	GetLoginPw,SendLoginPw
from	forms			import	PwMailForm


def	PwMail(request):

    mess = ''

    ### --- Получение логина и пароля ---
    

    if request.method == 'POST':
	form = PwMailForm(request.POST)
	if form.is_valid():
	    email = form.cleaned_data['email']
	    r = GetLoginPw(email)
	    SendLoginPw(email,r[0],r[1])
	    mess = 'OK'

    form = PwMailForm(None)
    form.fields['email'].initial = ''


    c = RequestContext(request,{'mess':mess,'form':form})
    c.update(csrf(request))
    return render_to_response("pwmail/pwmail.html",c)

