from django.contrib import admin
from django.shortcuts import redirect
from bar.models import Bar, Comanda, ComandaItens, Mesa, Item, Funcionario
# Register your models here.
admin.site.site_header = "Administração do Pede Bem"

class ComandaItensAdmin(admin.ModelAdmin):
    list_display = ("item", "comanda")
    list_filter = ('comanda__mesa','comanda__status')

    def get_form(self, request, obj=None, **kwargs):
        form = super(ComandaItensAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['comanda'].queryset = ComandaItens.comanda.get_queryset().exclude(status='Paga')
        return form

    def response_add(self, request, obj, post_url_continue=None):
        return None

    def response_change(self, request, obj):
        return None

class ComandaAdmin(admin.ModelAdmin):
    list_display = ("mesa", "status")
    list_filter = ('status',)
    readonly_fields = ('status', 'total')

    def response_add(self, request, obj, post_url_continue=None):
        return None

    def response_change(self, request, obj):
        return None

admin.site.register(Comanda, ComandaAdmin)
admin.site.register(Item)
admin.site.register(ComandaItens, ComandaItensAdmin)

