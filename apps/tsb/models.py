from django.db import models


class Sample(models.Model):
    code = models.CharField(max_length=8, unique=True)

    def __unicode__(self):
        return self.code
