from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist #sesuaikan dengan nama fungsi yang dibuat
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    # path('xml/', show_wishlist, name='show_wishlist'), #sesuaikan dengan nama fungsi yang dibuat
    # path('json/', show_wishlist, name='show_wishlist'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/<int:id>', show_wishlist, name='show_wishlist'), #sesuaikan dengan nama fungsi yang dibuat


]