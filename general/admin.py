from django.contrib import admin
from .models import Feed, Room
from .models import Message
# Register your models here.

admin.site.register(Feed)
admin.site.register(Message)
admin.site.register(Room)