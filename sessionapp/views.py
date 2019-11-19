from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def main(request):
    return render(request, "main.html")

def setos(request):
    if "favorite_os" in request.GET:
        print(request.GET["favorite_os"])
        request.session['f_os'] = request.GET["favorite_os"]  # session 생성
        return HttpResponseRedirect("/showos")
    else:
        return render(request, 'setos.html')
    
def showos(request):
    context = {}
    if "f_os" in request.session:
        context['f_os'] = request.session["f_os"]  # 세션값 읽기
        context['message'] = '당신이 선택한 운영체제는 %s'%request.session["f_os"]
    else:
        context['f_os'] = None
        context['message'] = '운영체제를 선택하지 않았습니다'
    
    request.session.set_expiry(5)  # 세션 해제(5초)
    return render(request, 'showos.html', context)