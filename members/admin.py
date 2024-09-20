from django.contrib import admin
from .models import Members



class MemberAdmin(admin.ModelAdmin):
    list_display=("name", "age")


admin.site.register(Members,MemberAdmin)


# Register your models here.
