from django.contrib import admin
from .models import Post                  # 23 vinte e três



admin.site.register(Post)                  # 24



# Como você pode ver, nós importamos (incluímos) o modelo Post definido no capítulo anterior(models).
# Para tornar nosso modelo visível na página de administração, precisamos registrá-lo com admin.site.register(Post)