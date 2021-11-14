from django.db import models
from django.utils.translation import gettext_lazy as gl 

class An(models.Model):
    content = models.TextField(blank=True) # Voir pour mettre en False si le message vide est autorisé
    #liked après avoir géré la partie User
    #image plus tard
    #bookmark après User
    #author après User
    #parent plus tard
    #share_count plus tard
    #is_private
    #is_edited
    #update
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = gl("An")
        verbose_name_plural = gl("Ans")
        
    def __str__(self):
        return self.content
    
    #@property is_parent
    #@property like_count