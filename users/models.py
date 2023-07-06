from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class requestQuote(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    SelectedService = models.CharField(max_length=100)
    Message = models.TextField()
    def __str__(self):
        return self.Name


class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()  
    def __str__(self):
        return self.name
    

class product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/services/products", null=True)
    url = models.CharField(max_length=100, default=' ')


# love from client models start 

class loveFromClient(models.Model):
    clientName = models.CharField(max_length=100)
    clientProfession = models.CharField(max_length=200)
    clientImage = models.ImageField(upload_to="static/LoveFromClient/Client Image", null=True)
    clientMessage = models.TextField()

 # love from client models end       



# blog list models start

class blogSiteBackend(models.Model):
    blogImage = models.ImageField(upload_to="static/blog/Blog Image", null=True)
    blogRelatedTitle = models.CharField(max_length=50)
    writterName = models.CharField(max_length=50)
    publishDate = models.DateField()
    blogTitle = models.CharField(max_length=200)
    blogDetail = models.TextField()
# blog list models end


# newsletter

class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # number = models.IntegerField()
    # # service = models.CharField(max_length=100)
    # SERVICE=(
    #     ('Web Designing','Web Designing'),
    #     ('Email Marketing','Email Marketing'),
    #     ('SEO','SEO'),
    # )
    # service_options=models.CharField(choices=SERVICE,max_length=200,default="")
    specialNotes = models.TextField()
    def __str__(self):
        return self.name
