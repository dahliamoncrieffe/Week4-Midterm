from django.contrib import admin
from moncrieffeLTS.models import Media, User
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn')
    prepopulated_fields = {'slug': ('title',)}

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name', ('last_name'))

admin.site.register(Media, MediaAdmin)
admin.site.register(User, UserAdmin)

