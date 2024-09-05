from django.db import models



class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50)  # Example: Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Leave blank for current job
    description = models.TextField()

    def __str__(self):
        return self.job_title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

