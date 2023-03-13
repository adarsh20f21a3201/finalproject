from datetime import date

from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email=models.EmailField()
    roll_no=models.CharField(max_length=100)
    department=models.CharField(max_length=150)
    def __str__(self):
        return self.name


class images(models.Model):
    image=models.ImageField()

    def __str__(self):
        return self.image


'''image=images()
image.image="C:/Users/Mohan Krishna/Desktop/Main Project/project/finalproject2/finalproject/static/ai.jpeg"
image.save()'''


from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    

    
    



