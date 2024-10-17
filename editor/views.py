from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Text
import json

@csrf_exempt
def save_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text_id = data.get('id')
        content = data.get('content')
        Text.objects.update_or_create(id=text_id, defaults={'content': content})
        return JsonResponse({'status': 'success'})

def get_text(request, text_id):
    try:
        text_entry = Text.objects.get(id=text_id)
        return JsonResponse({'id': text_entry.id, 'content': text_entry.content})
    except Text.DoesNotExist:
        return JsonResponse({'error': 'Not Found'}, status=404)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
