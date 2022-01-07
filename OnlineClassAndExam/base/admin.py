from django.contrib import admin

# Register your models here.
from .models import userAccount,discussionTopic,discussionRoom,messageOnTopic

admin.site.register(userAccount)
admin.site.register(discussionTopic)
admin.site.register(discussionRoom)
admin.site.register(messageOnTopic)