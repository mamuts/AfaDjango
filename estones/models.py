from django.db import models

# Create your models here.
class EstonesQuotes(models.Model):
    """ Model per definir els preus i sistema de cobrament d'estones """
    quota_id = models.AutoField(primary_key=True)
    quota_curs_escolar = models.CharField(max_length=100)
    quota_preu_dia = models.DecimalField(max_digits=6, decimal_places=2)
    quota_preu_mes =  models.DecimalField(max_digits=6, decimal_places=2)
    quota_bonificar_mes = models.BooleanField()
    quota_complir_mes = models.BooleanField()

class EstonesUsuaris(models.Model):
    """ Model per gestionar els usuaris d'estones """
    usuari_id = models.AutoField(primary_key=True)
    usuari_nom = models.CharField(max_length=150)
    usuari_curs = models.CharField(max_length=5)

class EstonesDia(models.Model):
    """ Model per emmagatzemar els dies que utilitza un soci estones """
    dia_id = models.AutoField(primary_key=True)
    dia_data = models.DateTimeField(auto_now_add=True)
    usuari = models.ForeignKey(EstonesUsuaris, verbose_name="Soci", on_delete=models.CASCADE)
