from django.db import models

class Poll(models.Model):
    candidate_name=models.CharField(max_length=20,primary_key=True,unique=True)
    candidate_logo=models.ImageField(upload_to='media/')
    vote_count=models.IntegerField(null=True)