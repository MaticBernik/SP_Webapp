from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.conf.urls import include,url


from . import views

urlpatterns = [
    url(r'books/$', views.books, name='books'),
    url(r'^$', views.index, name='index'),
    #url(r'login/$',views.login,name="login"),
    #url(r'logout/$',views.logout,name="logout"),
    url(r'logout/$',logout, {'next_page': '/library'}),
    url(r'home/$',views.home,name="home"),
    url(r'users/$',views.users,name="users"),
    url(r'leases/$',views.leases,name="leases"),
    #url(r'^register/', CreateView.as_view(
    #        template_name='register.html',
    #        #form_class=UserCreationForm,
    #        form=UserCreationForm,
    #        success_url='/'
    #)),
    url(r'^register/',views.register,name='register'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'leases/add/$', views.lease, name="newLease"),
    url(r'leases/remove/(?P<lease_id>[0-9]+)/$',views.removeLease,name="removeLease"),
    url(r'books/lease/(?P<book_id>[0-9]+)/$',views.lease,name="lease"),
    url(r'books/reserve/(?P<book_id>[0-9]+)/$',views.reserve,name="reserve"),
    url(r'books/remove/(?P<book_id>[0-9]+)/$',views.removeBook,name="removeBook"),
    url(r'books/add/$',views.newBook,name="newBook"),


]