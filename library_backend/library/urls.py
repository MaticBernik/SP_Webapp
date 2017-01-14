from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls import include,url


from . import views

urlpatterns = [
    url(r'books/$', views.books, name='books'),
    url(r'^$', views.index, name='index'),
    url(r'login/$',views.login,name="login"),
    url(r'home/$',views.home,name="home"),
    url(r'users/$',views.users,name="users"),
    url(r'leases/$',views.leases,name="leases"),
    url(r'leases/add/$', views.lease, name="newLease"),
    url(r'books/lease/(?P<book_id>[0-9]+)/$',views.lease,name="lease"),
    url(r'books/reserve/(?P<book_id>[0-9]+)/$',views.reserve,name="reserve"),
    url(r'books/add/$',views.newBook,name="newBook"),
    url(r'^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

]