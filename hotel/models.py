from django.db import models
from decimal import Decimal
from datetime import date, timedelta, datetime
from core.models import Localidad, Categoria, Servicio, TipoHabitacion, Vendedor, Encargado
from .exceptions import DescuentoException, TipoHotelException
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class HotelManager(models.Manager):
    def en_zona(self, zona):
        return self.model.objects.filter(localidad__in=zona)

class HotelQuerySet(models.QuerySet):
    pass

# Hotel (Asignar Vendedor)
class Hotel(models.Model):
    objects = HotelManager.from_queryset(HotelQuerySet)()
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=800)
    #TODO: Email
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio)
    tipos = models.ManyToManyField(TipoHabitacion, through='PrecioPorTipo', through_fields=('hotel', 'tipo'))
    vendedores = models.ManyToManyField(Vendedor)
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)

    def es_comercializable(self):
        return self.vendedores.count() > 0

    def es_hospedaje(self):
        return self.categoria.estrellas in [Categoria.ESTRELLA_A, Categoria.ESTRELLA_B, Categoria.ESTRELLA_C]

    def __str__(self):
        return f"Hospedaje {self.nombre}" if self.es_hospedaje() else f"Hotel {self.nombre}"

    def agregar_habitacion(self, tipo, numero):
        # TODO: Validar que el tipo seleccionado sea un tipo del hotel
        if not self.tipos.filter(pk=tipo.pk).exists():
            raise TipoHotelException(f"El hotel no trabaja con el tipo de habitación {tipo}")
        return Habitacion.objects.create(tipo=tipo, numero=numero, hotel=self)

    def agregar_tarifa(self, tipo, baja, alta):
        # Que pasa si ya tengo el tipo cargado en el hotel?
        # que pasa si baja es mas grande que alta?
        pass 

    def agregar_descuento(self, habitaciones, coeficiente):
        if habitaciones <= 0:
            raise DescuentoException("El mínimo de habitaciones para aplicar descuento es de 1")
        if coeficiente < 0:
            raise DescuentoException("El descuento no puede ser negativo")
        # Condicion loca?
        if self.descuentos.filter(cantidad_habitaciones__lt=habitaciones, coeficiente__gt=coeficiente).exists():
            raise DescuentoException("No se puede crear un descuento menor a un descuento ya otorgado por menos habitaciones")
        return self.descuentos.create(cantidad_habitaciones=habitaciones, coeficiente=coeficiente)

    def obtener_descuento(self, habitaciones):
        return self.obtener_descuento_por_cantidad(len(habitaciones))

    def obtener_descuento_por_cantidad(self, cantidad):
        return self.descuentos.filter(cantidad_habitaciones__gte=cantidad).first()

class PrecioPorTipo(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='tarifario')
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, related_name='hoteles')
    # Precio por noche
    baja = models.DecimalField(max_digits=20, decimal_places=2)
    alta = models.DecimalField(max_digits=20, decimal_places=2)

# Habitación
class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="habitaciones", on_delete=models.CASCADE)
    numero = models.PositiveSmallIntegerField(default=101, validators=[MinValueValidator(101), MaxValueValidator(9999)]) # 403 <Piso><Cuarto> y cada habitacion puede ser del 1 al 99 al igual que los pisos
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hotel', 'numero')

    def get_numero(self):
        if len(str(self.numero)) == 4:
            num = str(self.numero)[2] + str(self.numero)[3]
        if len(str(self.numero)) == 3:
            num = str(self.numero)[1] + str(self.numero)[2]
        # Este if solo es para habitaciones cargadas con dos digitos
        if len(str(self.numero)) == 2:
            num = str(self.numero)[0]
        return num

    def piso(self):
        if len(str(self.numero)) == 4:
            return str(self.numero)[0] + str(self.numero)[1]
        else:
            return str(0) + str(self.numero)[0]

    def __str__(self):
        return f"{self.hotel}, Habitacion: {self.numero}"

    # Calcula el precio unitario de una habitación 
    def precio_por_noche(self, fecha):
        precio_por_tipo = self.hotel.tarifario.filter(tipo=self.tipo).first()
        if precio_por_tipo is None:
            #TODO: Custom exception
            raise Exception("No puedo calcular el precio")
        if self.hotel.temporadas.filter(inicio__lte=fecha, fin__gte=fecha).exists():
            return precio_por_tipo.alta
        return precio_por_tipo.baja

    # Suma el precio por noche desde la fecha inicial hasta la final
    def precio_alquiler(self, desde, hasta):
        if desde >= hasta:
            #TODO: Custom exception
            raise Exception("No puedo calcular el precio")
        total = Decimal(0)
        while desde < hasta:
            total += self.precio_por_noche(desde)
            desde += timedelta(days=1)
        return total

    # Confirma la disponibilidad de una habitación en una fecha dada. Es decir, si está alquilada o no en esa fecha.
    def esta_disponible(self, desde, hasta):
       return not self.alquileres.filter(inicio__lte=desde, fin__gt=hasta).exists()

# Temporada Alta
def validate_date_not_in_past(value):
    date = value
    validar_fecha_año_pasado(date)
    if date.year == datetime.now().year:
        validar_fecha_dia_pasado(date)
        validar_fecha_mes_pasado(date)

def validar_fecha_dia_actual(value):
    date = value
    if date.day == datetime.now().day:
        raise ValidationError('El dia es igual al actual')

def validar_fecha_dia_pasado(value):
    date = value
    if date.day < datetime.now().day:
        raise ValidationError('El dia es inferior al actual')

def validar_fecha_mes_pasado(value):
    date = value
    if date.month < datetime.now().month:
        raise ValidationError('El mes es inferior al actual')

def validar_fecha_año_pasado(value):
    date = value
    if date.year < datetime.now().year:
        raise ValidationError('El año es inferior al actual')

def validate_date_not_incorrect(value):
    date = value
    validar_fecha_año_pasado(date)
    if date.year == datetime.now().year:
            validar_fecha_dia_actual(date)
            validar_fecha_dia_pasado(date)
            validar_fecha_mes_pasado(date)
        

class TemporadaAlta(models.Model):
    nombre = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="temporadas")
    inicio = models.DateField(default=datetime.today, validators=[validate_date_not_in_past])
    fin = models.DateField(default=datetime.today, validators=[validate_date_not_incorrect])

    def clean_inicio(self):
        date = self.cleaned_data['inicio']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

# Descuentos
class Descuento(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="descuentos")
    # 1 = coeficiente1 = 0 opcionalmente
    # 2 = coeficiente1
    # 3 = coeficiente2
    # 4 = coeficiente3
    # 5 = coeficiente4
    cantidad_habitaciones = models.PositiveSmallIntegerField()
    coeficiente = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        ordering = ["cantidad_habitaciones"]

# Paquete Turistico
class PaqueteTuristico(models.Model):
    nombre = models.CharField(max_length=200)
    coeficiente = models.DecimalField(max_digits=3, decimal_places=2)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    inicio = models.DateField()
    fin = models.DateField()
    habitaciones = models.ManyToManyField(Habitacion)
