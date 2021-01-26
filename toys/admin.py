from django.contrib import admin

from toys.models import *

admin.site.register(Toy)
admin.site.register(Tag)
admin.site.register(User)