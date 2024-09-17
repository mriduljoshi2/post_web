from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponsePermanentRedirect
from .models import Item
from .forms import ItemForm
from typing import Any
#from django.template import loader

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """Creates view for the index page

    Args:
        request (HttpRequest): incoming http request

    Returns:
        HttpResponse: renders the index page displaying a list of items
    """
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

def details(request: HttpRequest, item_id: int) -> HttpResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_
        item_id (int): _description_

    Returns:
        HttpResponse: _description_
    """
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/details.html', context)

def add_item(request: HttpRequest) -> (HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect):
    form = ItemForm(request.POST or None)
    context: dict[str, ItemForm] = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

def update_item(request: HttpRequest, item_id: int) -> (HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    context: dict[str, Any] = {
        'form': form,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', context)