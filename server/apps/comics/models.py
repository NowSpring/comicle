import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ComicMaster(models.Model):
    
    ERA_TYPES = (
        ("1980", "1980"),
        ("1990", "1990"),
        ("2000", "2000"),
        ("2010", "2010"),
    )
    
    PUBLISHER_TYPES = (
        ("enikkisu", "エニックス"),
        ("gakushu", "学習研究科"),
        ("shogakukan", "小学館"),
        ("shonengaho", "少年画報社"),
        ("tokuma", "徳間書店"),
        ("asahi", "朝日ソラノマ"),
        ("tokyo", "東京三世社"),
        ("hakusen", "白泉社"),
        ("akita", "秋田書店"),
        ("takeshobo", "竹書房"),
        ("hobun", "芳文社"),
        ("kadokawa", "角川書店"),
        ("kodan", "講談社"),
        ("shuei", "集英社"),
    )
    
    TARGET_TYPES = (
        ("girl", "少女"),
        ("boy", "少年"),
        ("woman", "女性"),
        ("man", "男性"),
    )
    
    GENRE_TYPES = (
        ("four-panel", "4コマ"),
        ("sf", "SF"),
        ("gag", "ギャグ"),
        ("suspense", "サスペンス"),
        ("sport", "スポーツ"),
        ("battle", "バトル"),
        ("fantasy", "ファンタジー"),
        ("horor", "ホラー"),
        ("lovecome", "ラブコメ"),
        ("animal", "動物"),
        ("love", "恋愛"),
        ("history", "時代劇"),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name = "タイトル", max_length = 100)
    author = models.CharField(verbose_name = "作者", max_length = 100)
    era = models.CharField(verbose_name = "年代", max_length = 100, choices = ERA_TYPES)
    publisher = models.CharField(verbose_name = "出版社", max_length = 100, choices = PUBLISHER_TYPES)
    target = models.CharField(verbose_name = "対象", max_length = 100, choices = TARGET_TYPES)
    genre = models.CharField(verbose_name = "ジャンル", max_length = 100, choices = GENRE_TYPES)
    cover = models.ImageField(upload_to = "cover/master/", null = False, blank = True)
    # pdf = models.FileField(upload_to = "pdf/", validators = [FileExtensionValidator(['pdf'])])
    
    class Meta:
      
        verbose_name_plural = 'マスター'
    
    def __str__(self):
        
        return self.title
      

class ComicVersion(models.Model):
  
  title = models.ForeignKey(ComicMaster, on_delete = models.CASCADE)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  version_number = models.IntegerField(verbose_name = "巻数", validators=[MinValueValidator(0)])
  cover = models.ImageField(upload_to = "cover/version/", null = False, blank = True)
  
  class Meta:
      
        verbose_name_plural = 'バージョン'
    
  def __str__(self):
        
        return str(self.version_number)