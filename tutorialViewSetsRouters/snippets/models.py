from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
    class Meta:
        ordering = ('created',) #order by created
