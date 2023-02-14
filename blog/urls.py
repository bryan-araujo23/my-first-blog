# Aqui, estamos importando do Django a função url e todas as nossas
# views do aplicativo blog. (Não temos nenhuma ainda, mas chegaremos a isso em um minuto!)


from django.urls import path                                    # 38
from . import views                                             # 39


# Depois disso podemos adicionar nosso primeiro padrão de URLs:


urlpatterns = [                                                 # 40
    path('', views.post_list, name='post_list'),
]

#  Como você pode ver, estamos agora atribuindo uma view chamada post_list à URL raiz.
#  Este padrão de URL corresponde a uma sequência de caracteres vazia, e o resolvedor
#  de URLs do Django irá ignorar o nome de domínio (ou seja, http://127.0.0.1:8000 /) que antecede o caminho completo da URL.
#  Este padrão dirá ao Django que views.post_list é o lugar correto aonde ir se alguém
#  entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.
# A última parte, name='post_list', é o nome da URL que será usado para identificar a view.

# volter a introdução