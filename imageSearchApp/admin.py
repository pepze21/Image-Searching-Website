from django.contrib import admin

# Register your models here.


from imageSearchApp.models import Group, Name, Date, Image


admin.site.register(Group)
admin.site.register(Name)
admin.site.register(Date)
admin.site.register(Image)