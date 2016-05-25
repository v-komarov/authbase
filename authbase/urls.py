from django.conf.urls import patterns, include, url
from	django.contrib.staticfiles.urls	import	staticfiles_urlpatterns
from	django.conf	import	settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authbase.views.home', name='home'),
    # url(r'^authbase/', include('authbase.foo.urls')),

    url(r'^$', 'start.views.Home', name='Home'),
    url(r'^exit/$', 'start.views.Exit', name='Exit'),

    url(r'^modules/$', 'modules.views.List', name='List'),
    url(r'^editaccessname/$', 'modules.views.EditName'),
    url(r'^addaccessname/$', 'modules.views.AddName'),

    url(r'^access/$', 'access.views.List'),
    url(r'^switch/$', 'access.views.Switch'),

    url(r'^users/$', 'users.views.List'),
    url(r'^edituser/$', 'users.views.Edit'),
    url(r'^newuser/$', 'users.views.New'),
    url(r'^deluser/$', 'users.views.Del'),
    url(r'^userdataservice/$', 'users.views.UserDataService'),

    url(r'^mydata/$', 'mydata.views.EditMyData'),
    url(r'^myphoto/$', 'mydata.views.MyPhoto'),
    url(r'^myphotoshow/$', 'mydata.views.MyPhotoShow'),
    url(r'^fiesta/$', 'mydata.views.MyFiestas'),
    url(r'^mystatus/$', 'mydata.views.MyStatus'),

    url(r'^phone/$', 'phone.views.List'),

    url(r'^dates/$', 'dates.views.List'),

    url(r'^pwmail/$', 'pwmail.views.PwMail'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'css/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/task/authbase/authbase/static/css/',}),
    url(r'js/(?P<path>.*)$','django.views.static.serve',{'document_root':'/home/task/authbase/authbase/static/js/',}),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
