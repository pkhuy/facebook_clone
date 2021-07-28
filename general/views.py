from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import Feed, Message, Room
from django.http import HttpResponse, JsonResponse


# Create your views here.

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "iNVALID CREDENTIALS")
            return redirect('/')
    else:
        return render(request, 'login.html')


def homepage(request):
    #user = request.POST["username"]
    userq = User.objects.filter().values('username')
    users = []
    for user in userq:
        users.append(str(user)[14: len(str(user))-2])

    feeds = Feed.objects.order_by('-date')
    return render(request, 'homepage.html', {'feeds': feeds, 'users': users})


def logout(request):

    return render(request, 'login.html')


def message(request):
    cur_user = request.user
    userq = User.objects.filter().values('username')
    users = []
    for user in userq:
        users.append(str(user)[14: len(str(user))-2])

    return render(request, 'homechat.html', {'user': cur_user, 'users': users})

def newfeed(request):
    if request.method == "POST":
        cur_user = request.user 
        cur_feed = request.POST["feed"]
        feed = Feed(user=cur_user, feed=cur_feed, like=0)
        feed.save()
        return redirect('homepage')
    
    else:
        return render(request, 'newfeed.html')

def like(request):
    feed_id = request.POST["feed_id"]
    feed_obj = Feed.objects.get(id=feed_id)
    
    feed_obj.like = feed_obj.like + 1
    feed_obj.save()
    return redirect('homepage')


def room(request, room):
    username = request.GET.get('username')
    
    room_details = str(Room.objects.filter(name=room).values('name'))
    room_details = room_details[21:len(room_details)-4]
    messages_query = Message.objects.filter(
        roomid =room_details).values('message').order_by('-date')
    messages = []
    for message in messages_query:
        messages.append(message) 
    
    return render(request, 'roomchat.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'messages': messages
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    roomid = request.POST['roomid']
    room = request.POST['room']
    new_message = Message.objects.create(
        message=message, user=username, roomid=room)
    new_message.save()

   
    
    
    return redirect('/'+room+'/?username='+username, {'messages': messages })


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    room = request.POST['room_name']
    username = request.POST['username']
    messages = Message.objects.filter(roomid=room_details.id)
    return redirect('/'+room+'/?username='+username, {'messages': messages })
