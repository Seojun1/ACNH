from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'results.html')

def result(request):
    character = request.GET.get('character', 'Unknown')  # 기본값을 'Unknown'으로 설정
    
    # 결과 페이지를 렌더링합니다.
    return render(request, 'results.html', {'character': character})
