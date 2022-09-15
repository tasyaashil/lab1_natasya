from django.urls import path
from wishlist.views import show_wishlistxml, show_wishlistjson, show_wishlistxmljson

app_name = 'wishlist'

urlpatterns = [
    # path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlistxml, name='show_wishlistxml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_wishlistjson, name='show_wishlistjson'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_wishlistxmljson, name='show_wishlistxmljson'), #sesuaikan dengan nama fungsi yang dibuat


]