from django.db import models

# Create your models here.

JOB_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)
GENDER = (
    ("Male","Male"),
    ("Female","Female"),
)

class Job (models.Model): #table
    title = models.CharField(max_length=100)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    gender = models.CharField(max_length=20, choices=GENDER)
    

    def __str__(self):
        return self.title
    
class category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name