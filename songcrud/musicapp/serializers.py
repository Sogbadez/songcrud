from rest_framework import serializers

from .models import Song,Artiste


class SongSerializer (serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['artiste_id','title','date_released','likes'] 
         

class Artisteserializer(serializers.ModelSerializer):
    class Meta:
        model=Artiste
        fields=['song_id','content']


