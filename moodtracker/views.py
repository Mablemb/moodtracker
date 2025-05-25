from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # Para proteger a view
from .forms import RegistroHumorForm
from .models import RegistroHumor # Embora não usemos diretamente aqui, é bom ter para referência
from django.contrib import messages # Para feedback ao usuário
from django.contrib.auth.models import User

# Sua view registrar_humor (vamos modificá-la um pouco depois)
@login_required
def registrar_humor(request):
    if request.method == 'POST':
        form = RegistroHumorForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            messages.success(request, 'Seu humor foi registrado com sucesso! 😊')
            # MODIFICAR AQUI: Redirecionar para a página de histórico
            return redirect('moodtracker:meu_historico')
    else:
        form = RegistroHumorForm()
    return render(request, 'moodtracker/registrar_humor.html', {'form': form})

# NOVA VIEW: Meu Histórico de Humores
@login_required
def meu_historico(request):
    # Busca todos os registros de humor feitos pelo usuário logado.
    # A ordenação por data (mais recente primeiro) já está definida
    # no Meta do modelo RegistroHumor (ordering = ['-data_registro']).
    registros = RegistroHumor.objects.filter(usuario=request.user)
    context = {
        'registros': registros
    }
    return render(request, 'moodtracker/meu_historico.html', context)
    
@login_required
def humor_parceiro(request):
    parceiro = None
    registros_parceiro = []
    mensagem_erro = None

    try:
        # Tenta encontrar o "outro" usuário. Isso assume que há apenas 2 usuários
        # ativos no sistema para esta lógica funcionar de forma simples.
        outros_usuarios = User.objects.exclude(pk=request.user.pk) # Exclui o usuário logado
        if outros_usuarios.count() == 1:
            parceiro = outros_usuarios.first()
            registros_parceiro = RegistroHumor.objects.filter(usuario=parceiro)
        elif outros_usuarios.count() > 1:
            # Se houver mais de um outro usuário, esta lógica simples não é suficiente.
            # Você precisaria de uma forma mais explícita de definir quem é o parceiro.
            # Por agora, vamos apenas indicar isso.
            mensagem_erro = "Muitos usuários no sistema para determinar o parceiro automaticamente."
            # Em um app real, você poderia ter um campo no perfil do usuário para o parceiro
            # ou permitir selecionar qual parceiro visualizar.
        else: # outros_usuarios.count() == 0
            mensagem_erro = "Nenhum outro usuário encontrado para ser seu parceiro(a)."

    except User.DoesNotExist:
        mensagem_erro = "Não foi possível encontrar o parceiro(a)."
    except Exception as e:
        # Para capturar outros erros inesperados
        print(f"Erro ao buscar parceiro: {e}") # Log para o console do servidor
        messages.error(request, "Ocorreu um erro ao tentar buscar os dados do parceiro(a).")
        mensagem_erro = "Ocorreu um erro."


    context = {
        'parceiro': parceiro,
        'registros': registros_parceiro,
        'mensagem_erro': mensagem_erro,
    }
    return render(request, 'moodtracker/humor_parceiro.html', context)