from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    # data = BarangWishlist.objects.all()
    data = BarangWishlist.objects.filter(pk=id)
    context = {
    'list_barang': data,
    'nama': 'Natasya Ashil Zhafirah'
    }
    # return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # // Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    # // Jika XML
    # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")