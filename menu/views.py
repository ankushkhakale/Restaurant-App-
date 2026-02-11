from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem

def menu_list(request):
    categories = Category.objects.all()
    # Prefetch related items to minimize queries
    return render(request, 'menu/menu_list.html', {'categories': categories})

def menu_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu/menu_detail.html', {'item': item})
