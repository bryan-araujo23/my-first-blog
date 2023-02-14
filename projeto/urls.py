"""
# → URL’s: Um mapeador de URL é usado para redirecionar solicitações HTTP para a visualização
# apropriada com base na URL de solicitação.


projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include                                           # 35 include


# A URL do admin, que você visitou no capítulo anterior, já está aqui:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))                                               # 36

]


# Isso significa que para cada URL que começa com admin/, o Django irá encontrar uma view correspondente.
# É hora de criar nossa primeira URL! Queremos que http://127.0.0.1:8000 / seja a página inicial do nosso
# blog e exiba uma lista de posts.