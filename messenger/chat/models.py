from django.conf import settings
from django.db import models
from django.utils import timezone
from signin.models import user


class messege(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class chat(models.Model):
    user_sender= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    #user_deliver:user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    messeges = []
    text = models.TextField()
