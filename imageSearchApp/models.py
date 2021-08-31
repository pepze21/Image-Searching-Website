from django.db import models

# Create your models here.


class ImageData(models.Model):
    group = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    date = models.CharField(max_length=6) # YYMMDD 나중에 calendar를 터치하도록 ui 변경
    
    def __str__(self):
        return self.name

class Image(models.Model):
    imagedata = models.ForeignKey(ImageData, related_name='imagedata', \
        on_delete=models.CASCADE, null=True)
    image_path = models.ImageField(upload_to='image/', blank=True, null=True)
    image_url = models.URLField(max_length=512)


'''
class Group(models.Model):
    group = models.CharField(max_length = 32)

    def __str__(self):
        return self.group

class Name(models.Model): # 일대다 관계 설정시, ForeignKey의 on_delete 옵션은 필수.
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name


class Date(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length = 6) # YYMMDD

    def __str__(self):
        return self.date

class Image(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    image_url = models.URLField(max_length=512)

    def __str__(self):
        return self.image_url
'''

# 오마이걸 아린 210813 http://~~~/~~~
# 전소미 210813 http://~~~/~~~
# 동명이인이 있는 경우, 둘 다 출력(우선순위 : 검색결과 많은 사람부터)