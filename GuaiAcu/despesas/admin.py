from django.contrib import admin

# Register your models here.
from .models import Tipo_Despesa, Item_Despesas


admin.site.register(Tipo_Despesa)
admin.site.register(Item_Despesas)
