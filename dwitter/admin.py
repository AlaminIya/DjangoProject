from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet, Profile



class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]



admin.site.register(Dweet)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

# Register your models here.
