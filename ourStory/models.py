from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_data = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
