from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    def __str__(self):
        return self.q_text
    q_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def was_published_recently(self):
        return timezone.now() >= self.pub_date \
            >= timezone.now() - datetime.timedelta(days=1)

    # For admin page management of list_display()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
