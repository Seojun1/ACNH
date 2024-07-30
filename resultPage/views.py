from django.shortcuts import render
from django.http import JsonResponse
import base64
import json

def index(request):
    return render(request, 'results.html')

def result(request):
    encoded_data = request.GET.get('data', '')
    if encoded_data:
        try:
            # Base64 디코딩
            decoded_data = base64.b64decode(encoded_data).decode('utf-8')
            result = json.loads(decoded_data)
            character = result.get('resultCharacter', 'Unknown')
            description = result.get('description', 'No description available')
        except (ValueError, json.JSONDecodeError):
            character = 'Unknown'
            description = 'Invalid data'
    else:
        character = 'Unknown'
        description = 'No data provided'

    # 결과 페이지를 렌더링합니다.
    return render(request, 'results.html', {'character': character, 'description': description})
