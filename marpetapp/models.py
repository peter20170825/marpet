from django.db import models

# Create your models here.
class Mech_Cad(models.Model):
    heading=models.CharField(max_length=150)
    short_paragraph=models.TextField(blank=True)
    long_paragraph=models.TextField(blank=True)
    cad_image=models.ImageField(upload_to='mech_images/')

    def __str__(self):
        return str(self.cad_image)

class Elect_Cad(models.Model):
    heading=models.CharField(max_length=150)
    short_paragraph=models.TextField(blank=True)
    long_paragraph=models.TextField(blank=True)
    cad_image=models.ImageField(upload_to='elect_images/')

    def __str__(self):
        return str(self.cad_image)

class Civil_Cad(models.Model):
    heading=models.CharField(max_length=150)
    short_paragraph=models.TextField(blank=True)
    long_paragraph=models.TextField(blank=True)
    cad_image=models.ImageField(upload_to='civil_images/')

    def __str__(self):
        return str(self.cad_image)

class Train_Cad(models.Model):
    heading=models.CharField(max_length=150)
    short_paragraph=models.TextField(blank=True)
    long_paragraph=models.TextField(blank=True)
    cad_image=models.ImageField(upload_to='train_images/')

    def __str__(self):
        return str(self.cad_image)

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150,default='')
    message = models.TextField()

    def __str__(self):
        return self.name
