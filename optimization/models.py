from django.db import models

class EC2Instance(models.Model):
    instance_id = models.CharField(max_length=20, unique=True)
    instance_type = models.CharField(max_length=50)
    # Add other fields like a name tag, etc.

class Recommendation(models.Model):
    instance = models.ForeignKey(EC2Instance, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)