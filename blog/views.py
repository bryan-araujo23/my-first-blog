from django.shortcuts import render

# Uma view é o lugar onde nós colocamos a "lógica" da nossa aplicação. Ela
# vai extrair informações do model que você criou e entregá-las a um template.



# Vamos criar uma view.


def post_list(request):                                                                         # 42
    return render(request, 'blog/post_list.html', {})


# Como você pode ver, nós criamos uma função (def) chamada post_list
# que leva a solicitação e irá retornar o valor que recebe ao chamar
# outra função render que irá renderizar (montar) nosso modelo blog/post_list.html.