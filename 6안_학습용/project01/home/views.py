# 공부 지도: learning/files/home/views.py.md
# 역할: 메인 화면
# 요청에서 조건을 읽고 계산 결과를 HTML 또는 JSON으로 돌려줍니다.
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
