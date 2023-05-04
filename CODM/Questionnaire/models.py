from django.db import models
from django.utils import timezone


class Shuhuda(models.Model):
    Uhusiano_marehemu = (
        ('Baba', 'Baba'),
        ('Mama', 'Mama'),
        ('ndugu', 'ndugu'),
        ('Hakuna Uhusiano', 'Hakuna Uhusiano'),
        ('Nyingine','nyingine')
    )
    Uhusiano_kifo=(
        ('Ndio','Ndio'),
        ('Hapana','Hapana'),
    )
    jina_kwanza = models.CharField(max_length=255)
    jina_pili = models.CharField(max_length=255)
    jina_mwisho = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    shahidi = models.CharField(max_length=255)
    uhusiano = models.CharField(max_length=255, choices=Uhusiano_marehemu)
    simu = models.IntegerField()
    Uhusiano_kipindi_kifo = models.CharField(max_length=255, choices=Uhusiano_kifo)
    
    def __str__(self):
        return self.shahidi
    

class Mhanga(models.Model):
    Ndoa = (
        ('ndoa', 'ndoa'),
        ('hajafunga ndoa', 'hajafunga ndoa'),
        ('mjane', 'mjane'),
        ('mgane', 'mgane'),
        ('talaka','talaka'),
        ('kutengana','kutengana')
    )
    Mahali = (
        ('nyumbani', 'nyumbani'),
        ('hospitali', 'hospitali'),
        ('kituo cha afya', 'kituo cha afya'),
        ('sijui', 'sijui')
    )
    Jinsia=(
        ('mume','mwanaume'),
        ('mke','mwanamke')
    )
    shuhuda = models.ForeignKey(Shuhuda, on_delete=models.CASCADE)
    jina_kwanza = models.CharField(max_length=255 ,default='default_value')
    jina_pili = models.CharField(max_length=255)
    jina_mwisho = models.CharField(max_length=255)
    jinsia = models.CharField(max_length=255, choices=Jinsia)
    ndoa = models.CharField(max_length=255, choices=Ndoa)
    kuzaliwa = models.DateField(default=timezone.now)
    kufa = models.DateField(default=timezone.now)
    mahali = models.CharField(max_length=255, choices=Mahali)
    maelezo = models.TextField()
    sababu1 = models.CharField(max_length=255)
    sababu2 = models.CharField(max_length=255)
    
    def __str__(self):
        return self.jina_kwanza



class Uchunguzi(models.Model):
    MAGONJWA = [
        ('moyo', 'Ugonjwa wa Moyo'),
        ('kisukari', 'Non-fiction'),
        ('presha', 'Mystery'),
        ('saratani', 'Thriller'),
        ('ajali', 'Ajali'),
        ('pumu', 'Pumu'),
        ('vvu', 'VVU'),
        ('kifafa', 'Kifafa'),
        ('kifua kikuu', 'Kifua Kikuu'),
        ('sijui', 'Sijui'),
    ]

    mhanga = models.ForeignKey(Mhanga, on_delete=models.CASCADE)
    shahidi = models.ForeignKey(Shuhuda, on_delete=models.CASCADE)
    magonjwa = models.CharField(choices=MAGONJWA, max_length=20, blank=True)
    mengineyo = models.TextField()

