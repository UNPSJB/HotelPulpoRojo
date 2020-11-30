from django.shortcuts import render

from .models import Factura
from core.models import Vendedor


# Create your views here.
def mis_facturas(request):
	vendedor = Vendedor.objects.filter(user=request.user).first()
	facturas = Factura.objects.filter(is_ordered=True, owner=vendedor)
	context = {
		'my_orders': facturas
	}

	return render(request, "mis_facturas.html", context)