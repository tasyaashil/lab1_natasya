from django.urls import path
from wishlist.views import show_wishlist, show_wishlistxml, show_wishlistjson, show_wishlistxmljson, register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('html/', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlistxml, name='show_wishlistxml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_wishlistjson, name='show_wishlistjson'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_wishlistxmljson, name='show_wishlistxmljson'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat

]