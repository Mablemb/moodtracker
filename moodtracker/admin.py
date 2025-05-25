from django.contrib import admin
from .models import RegistroHumor # Importe seu modelo

# Crie uma classe de admin para customizar como o modelo aparece (opcional para começar)
class RegistroHumorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'get_humor_display', 'data_registro', 'sentimento_principal') # Campos a serem mostrados na lista
    list_filter = ('usuario', 'humor', 'data_registro') # Filtros que aparecerão na lateral
    search_fields = ('usuario__username', 'sentimento_principal', 'notas_adicionais') # Campos pelos quais se pode buscar
    date_hierarchy = 'data_registro' # Navegação hierárquica por data

    # Para usar o get_humor_display na list_display, você pode precisar definir um short_description
    def get_humor_display(self, obj):
        return obj.get_humor_display()
    get_humor_display.short_description = 'Humor' # Nome da coluna no admin

# Registre seu modelo com a classe de admin customizada (ou sem ela para o padrão)
admin.site.register(RegistroHumor, RegistroHumorAdmin)

# Forma mais simples de registrar (sem customizações iniciais):
# admin.site.register(RegistroHumor)