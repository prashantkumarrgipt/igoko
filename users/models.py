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
    
class productItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/products/productItems", null=True)
    price = models.IntegerField()  
    productInclude = models.TextField(null=True)


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
    specialNotes = models.TextField()
    def __str__(self):
        return self.name
    


# join out team models
class JoinTeam(models.Model):
    email_address = models.EmailField()
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    Gender=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    gender = models.CharField(choices=Gender,max_length=200,default="")
    colg_name = models.CharField(max_length=100)
    colg_address = models.CharField(max_length=100)

    Qualifications=(
        ('B.A/B.Com/BBA/B.Ed/Diploma','B.A/B.Com/BBA/B.Ed/Diploma'),
        ('BCA/B.Tech/BE/B.Sc','BCA/B.Tech/BE/B.Sc'),
        ('M.A/M.Com/MBA/MCA/M.Ed/PG Diploma/PG Program','M.A/M.Com/MBA/MCA/M.Ed/PG Diploma/PG Program'),
        ('MCA/M.Tech/M.Sc','MCA/M.Tech/M.Sc'),
        ('others','others'),
    ) 
    qualification = models.CharField(choices=Qualifications,max_length=200,default="")

    times=(
        ('lessthan2hour','lessthan2hour'),
        ('3-4hours','3-4hours'),
        ('5hours','5hours'),
        ('Morethan5hours','Morethan5hours'),
    )
    spend_time = models.CharField(choices=times,max_length=200,default="")

    availablity_time = models.CharField(max_length=100, blank=True)
    internship_date = models.DateField()

    area=(
        ('Campaign manager','Campaign manager'),
        ('Business Development Assicoate (BDA)','Business Development Assicoate (BDA)'),
        ('Human Resource (HR)','Human Resource (HR)'),
        ('Social Media Marketing intern','Social Media Marketing intern'),
        ('Digital marketing Intern','Digital marketing Intern'),
        ('Web Developer','Web Developer'),
        ('Graphic Designer','Graphic Designer'),
        ('Campus Ambassder','Campus Ambassder'),
    )
    internship_area = models.CharField(choices=area,max_length=200,default="")
    pc=(
        ('Yes','Yes'),
        ('No','No'),
    )
    desktop_or_not = models.CharField(choices=pc,max_length=200,default="")

    types=(
        ('Internship for college credit','Internship for college credit'),
        ('Summer Internship','Summer Internship'),
        ('Non-profit Internship','Non-profit Internship'),
        ('Co-OP(Coperative Education)','Co-OP(Coperative Education)'),
        ('Externship','Externship'),
        ('Learning purpose','Learning purpose'),
    )
    internship_type = models.CharField(choices=types,max_length=200,default="")

    any_suggestion = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
