from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    cat_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    cat_image = models.ImageField(upload_to='pictures')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cat_name
