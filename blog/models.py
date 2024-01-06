from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering=["-created_at", "-updated_at"]

    def __str__(self) -> str:
        return self.title