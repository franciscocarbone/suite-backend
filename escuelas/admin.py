from django.contrib import admin
import models

admin.site.register(models.Contacto)

class EscuelaAdmin(admin.ModelAdmin):
    model = models.Escuela
    list_display = ('cue', 'nombre', 'localidad')
    search_fields = ('cue', 'nombre')

class PerfilAdmin(admin.ModelAdmin):
    model = models.Perfil
    list_display = ('user', 'nombre', 'apellido', 'grupo', 'dni', 'email')
    search_fields = ('user', 'nombre', 'apelido', 'dni')

admin.site.register(models.Escuela, EscuelaAdmin)
admin.site.register(models.Evento)
admin.site.register(models.Perfil, PerfilAdmin)

admin.site.register(models.TipoDeFinanciamiento)
admin.site.register(models.Nivel)
admin.site.register(models.TipoDeGestion)
admin.site.register(models.Area)
admin.site.register(models.Programa)
admin.site.register(models.Localidad)

admin.site.register(models.Experiencia)
admin.site.register(models.Cargo)
admin.site.register(models.Contrato)

admin.site.register(models.Tarea)
admin.site.register(models.MotivoTarea)
admin.site.register(models.PrioridadTarea)
admin.site.register(models.EstadoTarea)

class PisoAdmin(admin.ModelAdmin):
    model = models.Piso
    list_display = ('servidor', 'serie', 'ups', 'rack', 'estado')

admin.site.register(models.Piso, PisoAdmin)


class DistritoInline(admin.TabularInline):
    model = models.Distrito

class RegionAdmin(admin.ModelAdmin):
    inlines = [
        DistritoInline,
    ]

class LocalidadInline(admin.TabularInline):
    model = models.Localidad

class DistritoAdmin(admin.ModelAdmin):
    inlines = [
        LocalidadInline,
    ]

admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Distrito, DistritoAdmin)
