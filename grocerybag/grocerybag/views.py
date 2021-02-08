from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from groceries.models import Grocery
from django.views.generic import TemplateView, ListView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(ListView):
    model = Grocery
    template_name = "index.html"
    
    template_name = 'groceries/user_grocery_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'grocery'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Grocery.objects.filter(user=user).order_by('-date')


class IndexPage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home", args=[request.user.username]))
        return super().get(request, *args, **kwargs)
