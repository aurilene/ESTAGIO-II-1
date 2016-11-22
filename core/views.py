# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Category


# Create your views here.

def index(request):
	context = {
		'categories': Category.objects.all()
	}	
	return render(request,'index.html',context)

def contact(request):
	return render(request,'contact.html')

def product_list(request):
	return render(request,'product_list.html')

def product(request):
	return render(request,'product.html')
