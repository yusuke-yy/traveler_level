from accounts.models import CustomUser
from django.db import models

class Photo(models.Model):
    """写真モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    photo1 = models.ImageField(verbose_name='写真１',upload_to='media')
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'Photo'

    def __str__(self):
        return self.title

class Diagnosis(models.Model):
    """診断モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー',on_delete=models.PROTECT)
    prefectures = models.CharField(verbose_name='今までに訪れた都道府県の数',max_length=2)
    countries = models.CharField(verbose_name='今までに訪れた国の数',max_length=3)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural = 'Diagnosis'

    def __str__(self):
        return self.prefectures