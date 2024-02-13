from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import View, ListView, TemplateView
from base.models import Item
from collections import OrderedDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from pprint import pprint

class CartListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'pages/cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            return redirect('/')
        self.queryset = []
        self.total = 0
        for item_pk, quantity in cart['items'].items():
            item = Item.objects.get(pk=item_pk)
            item.quantity = quantity
            item.subtotal = int(item.price * quantity)
            self.queryset.append(item)
            self.total += item.subtotal
        self.tax_included_total = int(self.total * (settings.TAX_RATE + 1))
        cart['total'] = self.total
        cart['tax_included_total'] = self.tax_included_total
        self.request.session['cart'] = cart
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwarg):
        context = super().get_context_data(*args, **kwarg)
        try:
            context['total'] = self.total
            context['tax_included_total'] = self.tax_included_total
        except Exception:
            pass
        return context


class AddCartView(LoginRequiredMixin, View):

    def post(self, request):
        item_pk = request.POST.get('item_pk')
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            items = OrderedDict()
            cart = {'items': items}
        if item_pk in cart['items']:
            cart['items'][item_pk] += quantity
        else:
            cart['items'][item_pk] = quantity
        request.session['cart'] = cart
        return redirect('/cart/')

class RemoveCartView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/cart.html'
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', None)
        if cart is not None:
            pk = kwargs['pk']
            del cart['items'][pk]
            request.session['cart'] = cart
        return redirect('/cart/')

# 他の書き方1
# class RemoveCartView(TemplateView):
#     def get(self, request, pk):
#         cart = request.session.get('cart', None)
#         if cart is not None:
#             del cart['items'][id]
#             request.session['cart'] = cart
#         return redirect('/cart/')

# 他の書き方2(urls.pyとcart.htmlの修正も必要)
# class RemoveCartView(View):
#     def get(self, request):
#         id = request.GET.get('id')
#         cart = request.session.get('cart', None)
#         if cart is not None:
#             del cart['items'][id]
#             request.session['cart'] = cart
#         return redirect('/cart/')


# 関数ベースの書き方
# @login_required
# def remove_from_cart(request, pk):
#     cart = request.session.get('cart', None)
#     if cart is not None:
#         del cart['items'][pk]
#         request.session['cart'] = cart
#     return redirect('/cart/')
