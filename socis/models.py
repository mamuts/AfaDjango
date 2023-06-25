from django.db import models
from django.conf import settings

# Create your models here.
class Socis(models.Model):
    soci_id = models.AutoField(primary_key=True)
    soci_nom = models.CharField(max_length=100)
    soci_curs = models.CharField(max_length=5)
    soci_direccio = models.CharField(max_length=100)
    soci_codi_postal = models.IntegerField()
    soci_ciutat  = models.CharField(max_length=50)
    soci_telefon = models.CharField(max_length=15)
    soci_email = models.EmailField()
    soci_drets_imatge = models.BooleanField()
    soci_drets_whatzap = models.BooleanField()
    soci_cc = models.CharField(max_length=25)
    soci_nom_pares = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Soci"
        verbose_name_plural = "Socis"
        ordering = ["-soci_nom"]

    def __str__(self):
        return self.soci_nom

class Importar(models.Model):
    """docstring for Importar.models"""

    importar_id = models.AutoField(primary_key=True)
    importar_nom = models.CharField(max_length=100)
    importar_ruta = models.FileField(verbose_name="Csv", upload_to="afadjango/arxius")

    class Meta:
        verbose_name = "Importar"
        verbose_name_plural = "Importacions"
