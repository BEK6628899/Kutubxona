from django.db import models

class muallif(models.Model):
    live = [("ha","ha"),("yo`q","yo`q")]
    ism = models.CharField(max_length=50)
    trik = models.CharField(max_length=30,choices=live,null=True,default="yo`q")
    kitob_soni = models.PositiveIntegerField()
    jinsi = models.CharField(max_length=10)
    tugilgan_sanasi = models.DateField()
    yosh = models.SmallIntegerField(default=70)
    def __str__(self):
        return f"{self.ism} "

class kitob(models.Model):
    nom = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30)
    muallif = models.ForeignKey(muallif, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom} "

class talaba(models.Model):
    bitiruv = [("ha","ha"),("yo`q","yo`q")]
    ism = models.CharField(max_length=30)
    bitiruvchi = models.CharField(max_length=10,choices=bitiruv)
    kitoblar_soni = models.PositiveSmallIntegerField(default=3)
    kursi = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.ism} "
    class Meta:
        ordering = ("ism",)

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.DateField()
    def __str__(self):
        return f"{self.ism} "

class record(models.Model):
    qaytar = [("ha","ha"),("yo`q","yo`q")]
    talaba = models.ForeignKey(talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(kitob,on_delete=models.CASCADE)
    Admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sanasi = models.DateField()
    qaytardi = models.CharField(max_length=20,choices=qaytar,default="ha")









