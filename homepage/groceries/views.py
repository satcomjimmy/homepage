from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Grocery, WhenNeeded

# Create your views here.
def index(request):
    grocery_list = Grocery.objects.all()
    num_groceries = Grocery.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    context = {'grocery_list': grocery_list, 
    'num_groceries': num_groceries,
    }
    return render(request, 'groceries/index.html', context)

def detail(request, grocery_name):
    grocery_item = get_object_or_404(Grocery, pk=grocery_name)
    grocery_desc = Grocery.grocery_desc
    context = {'grocery_desc': grocery_desc}
    return render(request, 
    'groceries/detail.html', 
    {'grocery_item': grocery_item}, 
    context)
