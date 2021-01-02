
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from restaurants import views as restaurants_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('changeProfile/', user_views.change_profile, name='change-profile'),
    path('login/', user_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('blog/', include('blog.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('', restaurants_views.RestaurantListView, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
