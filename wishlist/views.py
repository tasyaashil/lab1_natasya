from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Natasya Ashil Zhafirah'
    }
    return render(request, "wishlist.html", context)

