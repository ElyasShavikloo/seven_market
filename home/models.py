from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=22)
    email = models.EmailField()
    title = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.message[:17]}'

