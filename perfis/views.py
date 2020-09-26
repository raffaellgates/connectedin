from django.shortcuts import render
from perfis import models
from django.shortcuts import redirect

def index(request):
	perfil = models.Perfil.objects.all()
	return render(request, 'index.html',{'perfil' : perfil})

def exibir(request, perfil_id):
	perfil = models.Perfil.objects.get(id=perfil_id)
	return render(request, 'perfil.html',{'perfil' : perfil})

def convidar(request, perfil_id):
	perfil_convidado = models.Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidado)
	return redirect('index')

def get_perfil_logado(request):
	return models.Perfil.objects.get(id=1)