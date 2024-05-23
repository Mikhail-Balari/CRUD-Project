from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name='update_url'),
    path('del/<int:f_oid>', views.deleteView, name='delete_url'),
    path('login/', views.loginView, name='login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('signup/', views.signupView, name='signup_url'),
    path('about/', views.aboutView, name='about_url'),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

