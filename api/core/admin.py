from django.contrib import admin
from .models import *


admin.site.register(Test)
admin.site.register(Question)
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
