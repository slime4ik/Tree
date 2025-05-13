from django.db import models
from django.urls import reverse, NoReverseMatch

class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название меню')
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100, verbose_name='Название пункта')
    parent = models.ForeignKey('self', null=True, blank=True, 
                               on_delete=models.CASCADE, related_name='children')
    named_url = models.CharField(max_length=100, blank=True, null=True, 
                                 verbose_name='Named URL')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')  # Для отображения в подменю как мы захотим

    class Meta:
        ordering = ['order']
    
    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        return '#'
    
    def __str__(self):
        return self.name
