from django.shortcuts import render
from django.views.generic import View
from timeline.forms import PublicarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from perfis.models import Perfil

# def list_posts(request):
# posts = Post.objects.all()
# return render(request, "list_posts.html", {'posts': posts})

@login_required
def add_post(request):
    if request.method == "POST":
        form = PublicarForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.perfil = get_perfil_logado(request)
            model_instance.save()
        return redirect('list_posts')

    else:
        form = PublicarForm()
        return render(request, "timeline/publicar.html", {'form': form})

@login_required
def get_perfil_logado(request):
    return request.user.perfil