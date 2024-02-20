from django.db import models
import re

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.CharField(max_length=50)
    date = models.DateField()

    def get_brief_content(self):
        str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\>]", "", self.content)
        return f'{str[:5]}...'

    def get_modify_url(self):
        return f'/editblog?id={self.id}'

    def get_delete_url(self):
        return f'/deleteblog?id={self.id}'
