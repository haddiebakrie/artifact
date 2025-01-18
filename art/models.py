from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ArtData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    objektgattung = models.CharField(max_length=100)
    sphaere = models.CharField(max_length=50)
    datierung = models.CharField(max_length=100)
    anbringungsort = models.CharField(max_length=200)
    aufbewahrungsort = models.CharField(max_length=200)
    kultempfaenger = models.CharField(max_length=100)
    amunsikonographie = models.TextField()
    namen_und_beiwoerter = models.TextField()
    uebersetzung = models.TextField()
    kommentar = models.TextField()
    literatur = models.TextField()
    bild_url = models.URLField()

    def __str__(self):
        return self.id 

