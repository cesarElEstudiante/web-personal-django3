from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Marca {self.id}: {self.marca}'
    
class Cliente(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    celular = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Cliente {self.id}: {self.cedula}, {self.nombre} {self.apellido_1} {self.apellido_2}, {self.celular}'

class Recepcionista(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    celular = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Cliente {self.id}: {self.cedula}, {self.nombre} {self.apellido_1} {self.apellido_2}, {self.celular}'
  
class Repuesto(models.Model):
    repuesto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits = 100, decimal_places=2)
    stock = models.IntegerField(null=True)
    
    def __str__(self):
        return f'Repuesto {self.id}: {self.repuesto}, $ {self.precio}, {self.stock}'
    
class Area(models.Model):
    area = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Area {self.id}: {self.area}'
    
class Modelo(models.Model):
    modelo = models.CharField(max_length=255)
    id_marca = models.ForeignKey(Marca, on_delete = models.SET_NULL, null = True )
    
    def __str__(self):
        return f'Modelo {self.id}: {self.modelo}, {self.id_marca}'

class Equipo(models.Model):
    sn = models.CharField(max_length=255)
    id_modelo = models.ForeignKey(Modelo, on_delete= models.SET_NULL, null = True)
    
    def __str__(self):
        return f'Equipo {self.id}: {self.sn}, {self.id_modelo}'


class Ingreso(models.Model):
    f_ingreso = models.DateField(auto_now=True)
    id_recepcionista = models.ForeignKey(Recepcionista, on_delete= models.SET_NULL, null = True)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null = True)
    id_equipo = models.ForeignKey(Equipo, on_delete= models.SET_NULL, null = True)
    
    def __str__(self):
        return f'Ingreso {self.id}: {self.f_ingreso}, {self.id_recepcionista}, {self.id_cliente}, {self.id_equipo}'

class Tecnico(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    apellido_1 = models.CharField(max_length=255)
    apellido_2 = models.CharField(max_length=255)
    celular = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    id_area = models.ForeignKey(Area, on_delete= models.SET_NULL, null = True)
    
    def __str__(self):
        return f'Tecnico {self.id}: {self.cedula}, {self.nombre} {self.apellido_1} {self.apellido_2}, {self.celular}, {self.id_area}'

class tecnicoRepara(models.Model):
    f_inicio = models.DateField(auto_now=True)
    f_final = models.DateField(null = True)
    idTecnico = models.ForeignKey(Tecnico, on_delete= models.SET_NULL, null = True)
    id_ingreso = models.ForeignKey(Ingreso, on_delete= models.SET_NULL, null = True)
    
    def __str__(self):
        return f'Reparacion {self.id}: {self.f_inicio} : {self.f_final}, {self.idTecnico}, {self.id_ingreso}'

class detalleReparacion(models.Model):
    id_reparacion = models.ForeignKey(tecnicoRepara, on_delete= models.SET_NULL, null = True)
    id_repuesto = models.ForeignKey(Repuesto, on_delete= models.SET_NULL, null = True)
    cant = models.IntegerField()
    precio = models.DecimalField(max_digits = 100, decimal_places=2)
    
    def __str__(self):
        return f'Cotizacion {self.id}: {self.id_reparacion}, {self.id_repuesto}, {self.cant}, {self.precio}'
      
    
    