from django.db import models


class Tasks(models.Model):
    TAGS = [
        ('Important','More Important'),
        ('General','Others'),
        ('Technical','Academic')
    ]


    title = models.CharField(max_length=100,null=False)
    desc = models.TextField(max_length=350,null=True)
    is_complete = models.BooleanField(default=False)
    tag = models.CharField(max_length=20, default='Others', null=False, choices=TAGS)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
