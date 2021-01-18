from django.urls import path
from . import views
from django.conf.urls.static import static
from poetryweb.settings import MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('',views.index,name="index"),
    path('poetry/',views.poetry,name="poetry"),
    path("search/", views.search, name="search"),
    path('contact/',views.contact,name="contact"),
    path('contact',views.contact,name="contact")

] + static(MEDIA_URL,document_root=MEDIA_ROOT)
