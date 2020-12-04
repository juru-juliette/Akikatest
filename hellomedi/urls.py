from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.urls import path
urlpatterns=[
    # url(r'',views.home,name = 'home'),
    path('',views.news_update,name='newsUpdate'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('', views.HomeView.as_view(), name='home'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate'),
    url(r'^post$', views.post, name='post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)