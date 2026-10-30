from django.db import models #I want to model this data

class Student(models.Model): #Connect to database
    MAJOR = (
        ("CSCI-BS", "BS in Computer Science"), #Active record
        ("CPEN-BS", "BS in Computer Engineering"),
        ("BIGD-BI", "BI in Game Design and Development"),
        ("BICS-BI", "BI in Computer Science"),
        ("BISC-BI", "BI in Computer Security"),
        ("CSCI-BA", "BA in Computer Science"),
        ("DASE-BS", "BS in Data Analytics and Systems Engineering"),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField("MSU Email")
    major = models.CharField(max_length=200, choices=MAJOR, blank=True) #Attrebute for the class, overloaded method charfield

    def __str__(self):
        return self.name


class Portfolio(models.Model):                                          
    student = models.OneToOneField( Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):                                          
    portfolio = models.ForeignKey( Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(): #Unfinsiehd method
        return



