from django.shortcuts import render_to_response
from django.template import RequestContext

from games.models import Game, GameForm

def index(request):
    '''
        Shows all games, sorted by date.
    '''
    
    games = Game.objects.all()

    if (request.method == 'POST'):
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            game_form.save()
            # Reset the form.
            game_form = GameForm()
    else:
        game_form = GameForm()
    
    context = RequestContext(request)
    return render_to_response('index.html',
                              {
                                'games': games,
                                'game_form': game_form
                              },
                              context_instance=context)