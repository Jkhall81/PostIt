from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Post

# Unregister Groups
admin.site.unregister(Group)


# mix profile info into user section
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # just display username fields on admin page
    fields = ['username']
    inlines = [ProfileInline]


# unregister initial user
admin.site.unregister(User)

# register and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

# Register Posts
admin.site.register(Post)
