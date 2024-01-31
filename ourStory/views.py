from django.http import JsonResponse
from .models import Story
from .serializers import StorySerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def story_list(request):
    if request.method == 'GET':
        return get_stories(request)
    elif request.method == 'POST':
        return create_story(request)
    elif request.method == 'PUT':
        return update_story(request)

def get_stories(request):
    stories = Story.objects.all().order_by('create_date')
    serializer = StorySerializers(stories, many=True)
    return JsonResponse({"stories": serializer.data}, safe=False)

def create_story(request):
    data = JSONParser().parse(request)
    serializer = StorySerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def update_story(request):
    data = JSONParser().parse(request)
    try:
        story_id = data['id']
        story = Story.objects.get(pk=story_id)
    except (Story.DoesNotExist, KeyError):
        return JsonResponse({"error": "Story not found"}, status=404)

    serializer = StorySerializers(story, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)