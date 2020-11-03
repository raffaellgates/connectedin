from django.shortcuts import render
from perfis.models import Perfil, Convite
from timeline.models import Publicacao
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):

    return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                          'perfil_logado': get_perfil_logado(request),
                                          'postagens': list_publicacao(get_perfil_logado(request))})


@login_required
def exibir_perfil(request, perfil_id):

    # perfil = get(perfil_id)
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request)})


@login_required
def convidar(request, perfil_id):

    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)

    if(perfil_logado.pode_convidar(perfil_a_convidar)):
        perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')


def get_perfil_logado(request):
    return request.user.perfil


def list_publicacao(perfil_logado):
    all_pub = Publicacao.objects.all()
    cont = perfil_logado.contatos.all()
    postagens = []
    for postagem in all_pub:
        if (postagem.usuario == perfil_logado):
            postagens.append(postagem)

        for contato in cont:
            if (postagem.usuario.id == contato.id):
                postagens.append(postagem)

    return postagens


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def recusar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.recusar()
    return redirect('index')


@login_required
def desfazer(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil.desfazer(get_perfil_logado(request))
    return redirect('index')
