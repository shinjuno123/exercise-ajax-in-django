from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import ast
# Create your views here.

@csrf_exempt
def index(request):
    print("requst: "+request.method)
    if(request.method == "POST"):
        pv = request.POST.dict()
        #print(json.dumps(pv))
        value = getValueFromJson(pv)
        context = {'value':value['value']}
        print(context)
        return JsonResponse(context)
    else:
        print('nothing still')
        return render(request,'ajapp/index.html',{})


def getValueFromJson(value):
    valueToStr = str(value)
    return ast.literal_eval(valueToStr[2:-6])
