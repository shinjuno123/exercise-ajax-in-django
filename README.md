# 💪 Exercise Ajax in Django


## Technical Stack
- HTML
- Javascript
- Django
- Django RESTful API


## Overview

I practiced for how to use Ajax in Django

## Code Review

### Input


![django ajax](https://user-images.githubusercontent.com/72008909/208451726-d9011c1b-625e-41ca-b9f7-55143a253e5f.png)


Let's write something in the input tag. This page is at root.


### Send a request
```js
// ./ajapp/templates/ajapp/index.html

 text.onkeyup = (e)=>{
     if(e.keyCode === 13){
         request.open('POST','',true);
         request.setRequestHeader('Content-Type','application/x-www-form-urlencoded; charset=UTF-8');
         var myObject = {value :text.value}
         request.send(JSON.stringify(myObject));
     }
 }

```

Once you push enter button in keyboard, This code sends the input value you wrote in the tag to server with POST signal.


### Catch a request in server and Respond to client
```python
# ./ajapp/views.py
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

```

If the request has POST signal, It changes the body of the response into python dictionary and extract string only. and finally It sends the string to the client side again with JSON format.


### Catch the response and Display the response data


![django ajax2](https://user-images.githubusercontent.com/72008909/208451858-6ce4b8fd-25cf-430a-87a6-c2f42dbf4c91.png)


```js
// ./ajapp/templates/ajapp/index.html
 request.onload = (json)=>{
       if(request.status === 200){
           var a = JSON.parse(json.currentTarget.response);
           var body = document.getElementById('body');
           var newDIV = document.createElement("div");
           newDIV.innerHTML = `${a['value']}`;
           body.appendChild(newDIV);
           console.log(`you did ajax successfully ${a['value']}`);
       }else{
           console.log(request.status);
       }
   }
```

This code catches the response from server and display the response data to screen


