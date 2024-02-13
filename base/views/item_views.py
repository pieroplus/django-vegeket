from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Item, Tag, Category

# クラスの場合
class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'

# 関数の場合
# def index(request):
#     object_list = Item.objects.all()
#     context = {
#         'object_list': object_list
#     }
#     return render(request, 'pages/index.html', context)

# def detail(request, pk):
#     object = Item.objects.get(pk=pk)
#     context = {
#         'object': object
#     }
#     return render(request, 'pages/item.html', context)
    

class CategoryListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 2
 
    def get_queryset(self):
        queryset = super().get_queryset()
        self.category = Category.objects.get(slug=self.kwargs['pk'])
        return queryset.filter(is_published=True, category=self.category)
        # こちらの書き方でもOK
        # self.category = Category.objects.get(slug=self.kwargs['pk'])
        # return Item.objects.filter(is_published=True, category=self.category)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Category #{self.category.name}'
        return context
 
 
class TagListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 2
 
    def get_queryset(self):
        queryset = super().get_queryset()
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        return queryset.filter(is_published=True, tags=self.tag)
        # こちらの書き方でもOK     
        # self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        # return Item.objects.filter(is_published=True, tags=self.tag)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Tag #{self.tag.name}"
        return context