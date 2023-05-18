from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Institutions(models.Model):
    institution_name = models.CharField(max_length=255)
    info = models.TextField()
    image = models.ImageField(upload_to='Institutions_img')
    site = models.URLField()

    def __str__(self):
        return self.institution_name

class Courses(models.Model):
    Status_list = [
        ('Published', 'Опубликованно'),
        ('Moderate', 'На модерации') ,
        ('Withdrawn', 'Снято с публикации')
    ]
    Categories_list = [
        ('Programming', 'Программирование'),
        ('Design', 'Дизайн'),
        ('Construction', 'Строительство')
    ]
    course_name = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    image = models.ImageField(upload_to='Courses_img')
    duration = models.CharField(max_length=255)
    price = models.IntegerField()
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE, blank=True)
    category = models.CharField(max_length=255, choices=Categories_list)
    status = models.CharField(max_length=255, choices=Status_list, blank=True)
    priority = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.course_name

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


