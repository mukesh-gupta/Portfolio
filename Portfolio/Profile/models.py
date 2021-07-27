from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics',default='static/user.png')
    work_field=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    city=models.CharField(max_length=200)
    birth=models.DateField()
    desc=models.TextField(max_length=2000)
    gender=models.CharField(max_length=50)
    lang=models.CharField(max_length=100)
    hobb=models.CharField(max_length=200)
    add_skill=models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)

class Skills(models.Model):
    sub=models.CharField(max_length=200)
    perc=models.PositiveIntegerField()
    def __str__(self):
        return str(self.perc)


class Resume(models.Model):
    obj=models.TextField(max_length=500)

class Education(models.Model):
    edu_stdt = models.DateField()
    edu_eddt = models.DateField()
    edu_course = models.CharField(max_length=250)
    edu_clg = models.CharField(max_length=150)
    edu_mark = models.FloatField()
    def __str__(self):
        return str(self.edu_course)

class Certificate(models.Model):
    cert_name = models.CharField(max_length=300)
    cert_url= models.URLField()
    def __str__(self):
        return str(self.cert_name)

class Project(models.Model):
    proj_img=models.ImageField(upload_to='proj',default='static/user.png')
    img_1 = models.ImageField(upload_to='proj_img',default='static/user.png')
    img_2 = models.ImageField(upload_to='proj_img',default='static/user.png')
    img_3 = models.ImageField(upload_to='proj_img',default='static/user.png')
    img_4 = models.ImageField(upload_to='proj_img',default='static/user.png')
    img_5 = models.ImageField(upload_to='proj_img',default='static/user.png')
    proj_stdt = models.DateField(null=True)
    proj_eddt = models.DateField(null=True)
    proj_title = models.CharField(max_length=300)
    proj_desc = models.TextField(max_length=2000)
    proj_url = models.URLField()
    proj_sc = models.URLField(null=True)
    front_e=models.CharField(max_length=200,null=True)
    back_e=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.proj_title)


class Contact(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE,null=True)
    git=models.URLField()
    linked_in = models.URLField()
    def __str__(self):
        return self.about.city