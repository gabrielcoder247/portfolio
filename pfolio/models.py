from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    image = models.ImageField(upload_to = 'uploads')
    git_url = models.CharField(max_length = 66)
    live_site = models.CharField(max_length=66)
    techs = (
        ('python','python'),
        ('django','django'),
        ('css','css'),
        ('html5','htm'),
        ('flask','flask'),
        ('geodjango','geodjango'),
        ('angularjs','angularjs'),
        ('postgresql','postgresql'),
    )

    technologies = models.CharField(max_length=255, choices=techs)

    def __str__(self):
        return self.title

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    def delete_project(self):
        self.delete()

    def save_project(self):
        self.save()


    


