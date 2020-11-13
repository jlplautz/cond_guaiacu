from django.db import models

# Create your models here.


class Cad_Condomino(models.Model):
    num_apto = models.IntegerField()


class Tipo_Despesa(models.Model):
    desc_despesa = models.CharField(max_length=100)


class Item_Despesas(models.Model):
    desc_item_despesa = models.CharField(max_length=100)
    tipo_despesa = models.ForeignKey(Tipo_Despesa, on_delete=models.CASCADE)


class Desp_Comum(models.Model):
    item_despesa = models.ForeignKey(Item_Despesas, on_delete=models.CASCADE, null=True, blank=True)
    valor_desp_comum = models.DecimalField('valor', max_digits=8, decimal_places=2)
    data_desp_comum = models.DateField(null=True, blank=True)


class Desp_Comum_Parcelas(models.Model):
    item_despesa = models.ForeignKey(Item_Despesas, on_delete=models.CASCADE, null=True, blank=True)
    valor = models.DecimalField('valor', max_digits=8, decimal_places=2)
    num_parc_comum = models.IntegerField('num_par_comum')
    Valor_parc_comum = models.DecimalField('Valor_Parcela', max_digits=8, decimal_places=2)
    data_parc_comum = models.DateField(null=True, blank=True)


class Desp_Individual(models.Model):
    num_apto = models.ForeignKey(Cad_Condomino, on_delete=models.CASCADE, null=True, blank=True)
    qtdade_gas = models.FloatField(max_length=8)
    mes_ref = models.DateField()
    item_despesa = models.ForeignKey(Item_Despesas, on_delete=models.CASCADE, null=True, blank=True)
