from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Livraria</h1><p>Esta é a página inicial.</p>")
