from django.contrib import admin

# Register your models here.
from .models import Etudiant
# admin.site.register(Etudiant)



class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom_etudiant', 'note')
    fields = ('nom_etudiant', 'note')

admin.site.register(Etudiant, EtudiantAdmin)
