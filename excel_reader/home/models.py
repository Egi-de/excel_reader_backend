from django.db import models
from django.contrib.auth.models import User

class ExcelData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='excel_data')
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)


    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ExcelData for {self.user.username} uploaded at {self.uploaded_at}"
