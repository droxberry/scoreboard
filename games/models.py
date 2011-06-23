from django import forms
from django.db import models

class Game(models.Model):
    player_one = models.CharField('Player One', max_length=255)
    player_two = models.CharField('Player Two', max_length=255)
    player_one_score = models.IntegerField("Player One's Score")
    player_two_score = models.IntegerField("Player Two's Score")
    played_on = models.DateTimeField('Date/Time Played', auto_now_add=True)
        
    class Meta:
        ordering = ['-played_on']
        
    def __unicode__(self):
        return 'Game: %s (%s) vs. %s (%s) on %s' % (self.player_one, 
                                                    self.player_one_score,
                                                    self.player_two,
                                                    self.player_two_score, 
                                                    self.played_on)
        
    def winner(self):
        if self.player_one_score > self.player_two_score:
            return self.player_one
        else:
            return self.player_two
        

class GameForm(forms.ModelForm):
    class Meta:
        model = Game