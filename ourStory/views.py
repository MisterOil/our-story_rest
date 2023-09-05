from django.http import JsonResponse
from .models import Story
from .serializers import StorySerializers

def story_list(request):

    stoy = Story.objects.all()
    serializer = StorySerializers(stoy, many=True)
    return JsonResponse({"stoy": serializer.data}, safe=False)