from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Artiste
from .models import Song
from .models import Lyric

# Create your views here.
class musicAppArtiste(APIView):
    
    def get(self, request):
        content = Artiste.objects.all().values()
        return JsonResponse({"data": list(content)})

class musicAppSongs(APIView):
    
    def get(self, request):
        content = Song.objects.all().values()
        return JsonResponse({"data": list(content)})
    
    def put(self, request, *args, **kwargs):
        model_id = kwargs.get("id", None)
        if not model_id:
            return JsonResponse({"error": "method /PUT/ not allowed"})
        
        try:
            instance = Song.objects.get(id=model_id)
        except:
            return JsonResponse({"error": "object does not exist"})
            


class musicAppLyric(APIView):
    
    def get(self, request):
        content = Lyric.objects.all().values()
        return JsonResponse({"data": list(content)})
