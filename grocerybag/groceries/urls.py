from django.urls import path, re_path
from .views import (
    GroceryCreateView,
    GroceryUpdateView,
    GroceryDeleteView,
    UserGroceryListView,
)





app_name='groceries'
 


urlpatterns = [
    path('new/', GroceryCreateView.as_view(), name='create'),
    path('<str:username>/', UserGroceryListView.as_view(), name='user-groceries'),
    
    path('<int:pk>/update/', GroceryUpdateView.as_view(), name='grocery-update'),
    # path('<int:pk>/delete/', GroceryDeleteView.as_view(), name='grocery-delete'),
    re_path(r'^grocery/(?P<pk>\d+)/delete/$', GroceryDeleteView.as_view(), name='grocery-delete'),
]
