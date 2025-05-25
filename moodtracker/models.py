from django.db import models
from django.contrib.auth.models import User # Para vincular o registro a um usuário

class HumorEscolha(models.TextChoices):
    FELIZ = 'FELIZ', 'Feliz 😊'
    CONTENTE = 'CONTENTE', 'Contente 🙂'
    NEUTRO = 'NEUTRO', 'Neutro 😐'
    TRISTE = 'TRISTE', 'Triste 😢'
    ANSIOSO = 'ANSIOSO', 'Ansioso 😬'
    ESTRESSADO = 'ESTRESSADO', 'Estressado 🤯'
    ANIMADO = 'ANIMADO', 'Animado 🎉'
    RELAXADO = 'RELAXADO', 'Relaxado 😌'
    # Adicione mais opções conforme vocês acharem necessário

class RegistroHumor(models.Model):
    # Quem fez este registro de humor
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_de_humor')

    # Quando o registro foi feito (será preenchido automaticamente na criação)
    data_registro = models.DateTimeField(auto_now_add=True)

    # O humor principal escolhido de uma lista
    humor = models.CharField(
        max_length=20,
        choices=HumorEscolha.choices,
        default=HumorEscolha.NEUTRO, # Um valor padrão
    )

    # Um sentimento ou pensamento principal mais específico (opcional)
    sentimento_principal = models.CharField(max_length=255, blank=True, null=True)

    # Notas adicionais ou um diário sobre o sentimento (opcional)
    notas_adicionais = models.TextField(blank=True, null=True)

    # Para quem este humor é "visível" ou para quem a notificação primária iria.
    # No seu caso, será o seu parceiro(a).
    # Podemos adicionar um campo específico para o parceiro aqui, ou gerenciar a lógica
    # de quem vê/é notificado nas views. Para começar simples, vamos assumir que
    # a lógica da view identificará o parceiro. Se quiser ser explícito:
    # parceiro_alvo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='humores_recebidos')
    # Por enquanto, vamos manter sem o parceiro_alvo explícito no modelo para simplificar.

    def __str__(self):
        # Uma representação em string amigável do objeto, útil no admin do Django
        return f"{self.usuario.username} - {self.get_humor_display()} em {self.data_registro.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        # Ordenar os registros por data, do mais recente para o mais antigo
        ordering = ['-data_registro']