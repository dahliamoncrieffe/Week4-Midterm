from django.conf.urls import url
from moncrieffeLTS import views

app_name = 'moncrieffeLTS'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^view_book', views.show_book, name='show_book'),
    #url(r'^book', views.Book, name='book'),
    #url(r'^dvd', views.Dvd, name='dvd'),
        #This is how you map to about page
    #url(r'^base', views.base, name='base'),
]
