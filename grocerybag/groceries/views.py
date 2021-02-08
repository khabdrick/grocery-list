from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Grocery

from .forms import GroceryForm, GroceryUpdateForm




class UserGroceryListView(ListView):
    model = Grocery
    template_name = 'groceries/user_grocery_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'grocery'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Grocery.objects.filter(user=user).order_by('-date')



class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = Grocery
    form_class = GroceryForm
    template_name = 'groceries/grocery_form.html'
    # redirect_field_name = 'groceries/user_grocery_list.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GroceryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grocery
    # fields = ['item_name', 'item_quantity', 'item_status', ]
    form_class = GroceryUpdateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        grocery = self.get_object()
        print(grocery)
        if self.request.user == grocery.user:
            return True
        return False


class GroceryDeleteView(LoginRequiredMixin, DeleteView):
    model = Grocery
    success_url = '/'

 

