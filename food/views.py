from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list,
       }
    #return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

def items(request):
    return HttpResponse('<h1>items<h1>')

def detail(request,item_id):
    item_dtls = Item.objects.get(pk=item_id)
    context = {
        'item_dtls':item_dtls,
    }
    return render(request,'food/item_detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/add_item.html',{'form':form})

def delete_item(request,item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete_item.html',{'item':item})

def edit_item(request,item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request,'food/add_item.html',{'form':form,'item':item})