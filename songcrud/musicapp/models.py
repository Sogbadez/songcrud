from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()


class Song(models.Model): 
    artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    artiste_id=models.SmallIntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    date_released=models.DateField('Date Released')
    likes=models.IntegerField()
    # artiste_id=models.AutoField(unique=True)
   



class Lyric(models.Model):
    song=models.ForeignKey(Song, on_delete=models.CASCADE)
    content=models.TextField(max_length=250)
    # song_id=models.IntegerField(primary_key=True)

