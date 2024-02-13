from django.views.generic import ListView, DetailView
from base.models import Order
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from pprint import pprint
 
 
class OrderIndexView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/orders.html'
    ordering = '-created_at'
 
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
 
 
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'pages/order.html'
    
    # ＊get_querysetメソッドの追記
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        # pprint(obj.items)
        # json to dict
        context["items"] = json.loads(obj.items)
        context["shipping"] = json.loads(obj.shipping)
        pprint(context["shipping"])
        return context