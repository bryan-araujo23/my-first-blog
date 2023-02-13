from django.conf import settings                            # 17
from django.db import models
from django.utils import timezone                           # 18

# No arquivo blog/models.py definimos todos os objetos chamados Modelos -- este é um lugar em que vamos
# definir nossa postagem do blog.



# class é uma palavra-chave especial que indica que estamos definindo um objeto.

# Post é o nome do nosso modelo. Nós podemos dar um nome diferente
# (mas precisamos evitar caracteres especiais e espaços em branco).
# Sempre inicie o nome de uma classe com uma letra em maiúsculo.

# models.Model significa que o Post é um modelo de Django,
# então o Django sabe que ele deve ser salvo no banco de dados.

class Post(models.Model):                                  # 19 esta linha define o nosso modelo (é um objeto).
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



# propriedades acima: title, text, created_date, published_date e author
# Para fazer isso, é necessário definir um tipo para cada campo

# models.CharField - é assim que definimos um texto com um número limitado de caracteres.
# models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
# models.DateTimeField - este é uma data e hora.
# models.ForeignKey - este é um link para outro modelo.

                                           # VOLTE PARA INTRODUÇÃO