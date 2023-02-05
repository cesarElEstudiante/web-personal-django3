from django.contrib import admin
from usuarios.models import Marca
from usuarios.models import Cliente
from usuarios.models import Recepcionista
from usuarios.models import Repuesto
from usuarios.models import Area
from usuarios.models import Modelo
from usuarios.models import Equipo
from usuarios.models import Ingreso
from usuarios.models import Tecnico
from usuarios.models import tecnicoRepara
from usuarios.models import detalleReparacion

# Register your models here.
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Recepcionista)
admin.site.register(Repuesto)
admin.site.register(Area)
admin.site.register(Modelo)
admin.site.register(Equipo)
admin.site.register(Ingreso)
admin.site.register(Tecnico)
admin.site.register(tecnicoRepara)
admin.site.register(detalleReparacion)
