
from django.shortcuts import render
from .models import Piece, Person
# Create your views here.
def all_pieces(request, instrument,parts):

    piece_list = Piece.objects.all()
    #print (instrument, parts)
    if parts:
        parts=int(parts)
        if parts<7:
            piece_list = piece_list.filter(parts=parts)
        else:
            piece_list = piece_list.filter(parts__gte=6)
    if not instrument=='all':
        piece_list = piece_list.filter(shortinst__icontains=instrument)        
    composer_list = []
    for piece in piece_list:
        composer=piece.composer_id
        composer_list.append(composer)
    composer_set=set(composer_list)
    oeuvres_list = []
    for composer in composer_set:

        his_pieces = piece_list.filter(composer_id = composer)
        composer_record = Person.objects.get(id = composer)
        #print ('Pieces for composer {c}'.format(c=composer_record.surname))
        oeuvre={'composer' : composer_record, 'piece_list' : his_pieces, 'surname' :composer_record.surname}
        oeuvres_list.append(oeuvre)
    oeuvres_list =sorted(oeuvres_list, key=lambda tup: tup['surname'])
    if instrument == 'recorder':
        title_text = 'List of recorder'
    elif instrument == 'viol':
        title_text = 'List of viol'
    else:
        title_text = 'Full list of'
    if parts:
        if parts<7:
            title_text = '{t} {p} part'.format(t=title_text, p=parts)
        else:
            title_text = '{t} {p}'.format(t=title_text, p='greater than 6-part')
    context = {'oeuvres_list': oeuvres_list, 'title_text' : title_text}
    return render(request, 'piecelist.html', context)

def show_piece( request, piece_id):
    piece = Piece.objects.get(id = piece_id)
    return render(request, 'piece.html', {'piece' :piece})

def index(request):
    piece_list = Piece.objects.all()
    n=0
    composer_list=[]
    for piece in piece_list:
        n+=1
        composer=piece.composer_id
        composer_list.append(composer)
    composers=len(set(composer_list))
    context = {'pieces' : n, 'composers' : composers}
    return render(request, 'index.html', context)

def composer_index(request):
	composer_list = Person.objects.order_by('surname', 'names')
	context = {'composers' : composer_list}
	return render(request, 'composers.html', context)

def show_composer(request, composer_id):
	composer = Person.objects.get(shortname = composer_id)
	pieces= Piece.objects.filter(composer_id = composer.id)
	return render(request, 'composer.html', {'composer' : composer, 'pieces' : pieces})
	
