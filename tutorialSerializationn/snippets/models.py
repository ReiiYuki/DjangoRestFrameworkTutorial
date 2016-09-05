from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]] #Get language list from pygments
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) #sort it
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())  #sort style


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True) #Create Date
    title = models.CharField(max_length=100, blank=True, default='') #title
    code = models.TextField() #code inside Snippet
    linenos = models.BooleanField(default=False) #boolean of sometihng
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100) #language choices
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100) #coding style maybe

    class Meta:
        ordering = ('created',) #order by created
