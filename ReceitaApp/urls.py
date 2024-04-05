from django.urls import path 
from ReceitaApp import views


urlpatterns = [
    #(caminho,        view correspondentes )
    path('', views.index, name='index'),
    path('receitas/',views.listar_receitas, name='receitas'),
    path('receita/<int:id>', views.detalhes_receita, name='receita')
]