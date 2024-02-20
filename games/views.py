from django.shortcuts import render
from .models import Game, GameScreenshot, GameReviews
from .utils import send_message_to_telegram
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator





from random import choice




def home_page(request):
    rand_game = choice(Game.objects.all())
    trending_games = Game.objects.all().order_by('-views')[:4]
    most_played_games = Game.objects.all().order_by('-downloaded')[:6]
    discount_math = int(rand_game.price - (rand_game.price * rand_game.discount / 100))
    
    trending_games_discount = []
    most_played_games_discount = []
    for item in trending_games:
        trending_games_discount.append(
            int(item.price - (item.price * item.discount / 100))
        )
    for item in most_played_games:
        most_played_games_discount.append(
            int(item.price - (item.price * item.discount / 100))
        )
    trending_games = zip(trending_games, trending_games_discount)
    most_played_games = zip(most_played_games, most_played_games_discount)

    context = {
        "rand_game": rand_game,
        "discount_math": discount_math,
        "trending_games": list(trending_games),
        "most_played_games": list(most_played_games),
    }
    return render(request, 'index.html', context=context)



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name='login_register.html', context={'error': 'Invalid username or password'})
    return render(request, 'login_register.html')





def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'login_register.html')



def check_username(request):
    username = request.GET.get('username')
    answer = 'true'
    if User.objects.filter(username=username).exists():
        answer = 'false'
    return HttpResponse(answer)



def shop_page(request):
    games = Game.objects.all()
    games_discount = []


    if 'q' in request.GET:
        games = Game.objects.filter(title__icontains=request.GET['q'])

    p = Paginator(games, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    for item in page_obj:
        games_discount.append(
            int(item.price - (item.price * item.discount / 100))
        )
    games = list(zip(page_obj, games_discount))
    context = {
        "games": games,
        "paginated_games": page_obj,
    }
    return render(request, 'shop.html', context=context)




def detail_page(request, game_id):
    game = Game.objects.get(id=game_id)
    game_screenshots = GameScreenshot.objects.filter(game=game)
    game.views +=1
    game.save()

    game_reviews = GameReviews.objects.filter(game=game).order_by('-created_at')

    context = {
        "game": game,
        "game_screenshots": game_screenshots,
        "game_reviews": game_reviews,
    }
    return render(request, 'detail_page.html', context=context)


def game_reviews(request, game_id):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        game = Game.objects.get(id=game_id)
        review_message = request.POST.get('review_message')
        GameReviews.objects.create(
            user=user,
            game=game,
            review=review_message
        )
        return redirect('detail', game_id=game_id)


def contact_page(request):
    if request.method == 'POST':
        your_name = request.POST.get('your_name')
        your_surname = request.POST.get('your_surname')
        your_email = request.POST.get('your_email')
        subject = request.POST.get('subject')
        your_message = request.POST.get('your_message')



        tg_message = f"Saytdan xabar keldi:\n\nIsm: {your_name}\nEmail: {your_surname}\nMessage: {your_email}\nwdwfddf:{subject}\nEmail1: {your_message}"
        send_message_to_telegram(tg_message)

    return render(request, 'contact.html')


def logout_page(request):
    logout(request)
    return redirect('home')




def download_count(request):
    game_id = request.GET.get('game_id')
    game = Game.objects.get(id=game_id)
    game.downloaded += 1
    game.save()
    return HttpResponse("ok")





def profile_page(request):
    user = User.objects.get(id=request.user.id)
    context = {}
    if request.method == 'POST':
        user.username = request.POST.get('username')
        if user.check_password(request.POST.get('password1')):
            user.set_password(request.POST.get('password2'))
            user.save()
        else:
            context['error'] = 'Password incorrect'
    context['user'] = user
    return render(request, 'profile.html', context=context)