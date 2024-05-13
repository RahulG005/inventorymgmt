
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Transaction
from .forms import ItemForm, UpdateQuantityForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'home/item_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'home/add_item.html', {'form': form})

def delete_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    else:
        # Render a confirmation template for GET requests
        return render(request, 'home/delete_item.html', {'item': item})


def update_quantity(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = UpdateQuantityForm(request.POST)
        if form.is_valid():
            quantity_change = form.cleaned_data['quantity_change']
            item.quantity += quantity_change
            item.save()
            Transaction.objects.create(item=item, quantity_change=quantity_change)
            return redirect('item_list')
    else:
        form = UpdateQuantityForm()
    return render(request, 'home/update_quantity.html', {'form': form, 'item': item})
