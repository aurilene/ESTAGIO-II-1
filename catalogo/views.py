# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

class ProductListView(generic.ListView):
    model = Product # é o object.all
    template_name = 'catalogo/product_list.html'
    context_object_name = 'products'
    paginate_by = 3


product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):
    template_name='catalogo/category.html'
    context_object_name = 'product_list'
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.filter(category__slug=category)
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()

def product(request, slug):
	product = Product.objects.get(slug=slug)
	context = {
		'product' : product
	}
	return render(request, 'catalogo/product.html', context)
