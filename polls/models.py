from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models import Max


class Question(models.Model):
    question_text = models.CharField(
        'Texto da questão', max_length=200, help_text='informe o texto da questão')
    pub_date = models.DateTimeField('Data de publição')
    creation_date = models.DateTimeField(
        'Data da criação', default=timezone.now)

    def votos(self):

        return Choice.objects.filter(question=self).order_by('-votes').first()

    def was_published_recently(self):
        ontem = timezone.now() - timedelta(days=1)
        return self.pub_date >= ontem
    
    was_published_recently.short_description = "publicado recentemente"
    was_published_recently.boolean = True

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='questão')
    choice_text = models.CharField('texto da escolha', max_length=200)
    votes = models.IntegerField('Nº de votos', default=0)
    creation_date = models.DateTimeField(
        'Data da criação', default=timezone.now)

    def __str__(self):
        return self.choice_text
