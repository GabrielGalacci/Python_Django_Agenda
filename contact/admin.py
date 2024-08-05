from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'show',
    )
    ordering = '-id', 
    # list_filter = ('created_date', )
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10 # Coloca uma quantidade padrão de quantidade de registros mostrados
    list_max_show_all = 20 # Coloca a quantidade máxima de registros a serem mostrados
    
    # Não pode existir o mesmo parâmetro em editable e links ao mesmmo tempo
    list_editable = 'last_name', 'show'
    list_display_links = 'id', 'first_name',
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = '-id', 
