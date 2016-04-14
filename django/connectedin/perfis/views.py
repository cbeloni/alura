from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Perfil, Convite
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
    print request.user.username #novo
    print request.user.email #novo
    print request.user.has_perm('perfis.add_convite') #novo
    return render(request, 'index.html', {"perfis" : Perfil.objects.all() , "perfil_logado" : get_perfil_logado(request) } )

@login_required
def exibir(request, perfil_id):
    try:
        perfil = Perfil.objects.get(id=perfil_id)
    except Exception, e:
        perfil = Perfil()

    perfil_logado = get_perfil_logado(request)
    eh_contato = perfil in perfil_logado.contatos.all()
    
    return render(request, 'perfil.html', { "perfil" : perfil , "eh_contato" : eh_contato })

@permission_required('perfis.add_convite', raise_exception=True)
@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect(index)

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect(index)

@login_required
def get_perfil_logado(request):
    return request.user.perfil