import datetime
from typing import List

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_choices: List[Choice] = []

    def __str__(self):
        return f"{self.question_text} - {self.pub_date.isoformat()}"

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"
