import time

from django.db import models


class LifeCard(models.Model):
    STATUS_INFO = (
        ('0', 'Active'),
        ('1', 'Inactive'),
    )

    TYPE_INFO = (
        ('W', 'Work'),
        ('P', 'Play'),
        ('R', 'Rest'),
    )

    title = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_INFO)
    type = models.CharField(max_length=1, choices=TYPE_INFO)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'LifeLog Model : {}, {}, {}, {}'.\
            format(self.title, self.timestamp, self.type, self.status)

    class Meta:
        ordering = ['-timestamp']
