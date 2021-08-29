from django.contrib import admin

# Register your models here.


from imageSearchApp.models import ImageData, Image
# from .models import *

# Image 클래스를 inline으로 나타내기
class ImageInline(admin.TabularInline):
    model = Image

# ImageAdmin 클래스는 Image 객체를 리스트로 관리(?)
class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

admin.site.register(ImageData)
admin.site.register(Image)