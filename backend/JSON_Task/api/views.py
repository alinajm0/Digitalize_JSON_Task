import json
from django.http import JsonResponse, HttpResponseRedirect, HttpRequest, HttpResponse, request, response
from django.shortcuts import render


json_load = []
with open('json_data.json', 'r', encoding='utf-8') as json_file:
	json_load = json.load(json_file)
print(json_load)

def api_v1_fruits(request):
    if request.method == 'GET':
        return render(request, "temp.html", {'context': json_load})
    if request.method == 'POST':
        request_body = json.loads(request.body)
        print(request_body)
        for ele in json_load:
            if str(ele['id']) == str(request_body['id']):
                return render(request, "error.html", {'context' : 'id_exist', 'id': request_body['id']})
        json_load.append({
            'id':request_body['id'],
            'name': request_body['name'],
            'description':request_body['description']
        })
        with open('json_data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(json_load))
        return render(request, "temp.html", {'context': json_load})
    else:
        return render(request, "error.html", {'context' : 'method_error'}) 

def api_v1_fruits_getId(request, id):
    print(request.method)
    if request.method == 'GET':
        for ele in json_load:
            if str(ele['id']) == str(id):
                context =[{
                    'id':ele['id'],
                    'name': ele['name'],
                    'description': ele['description']
                }]
                return render(request, "temp.html", {'context': context})
        return render(request, "error.html", {'context' : 'id_error', 'id': id}) 
    # elif request.method == 'POST':
    #     return HttpResponseRedirect(api_v1_fruits)
    elif request.method == 'DELETE':
        print(id)
        for ele in json_load:
            if str(ele['id']) == str(id):
                json_load.remove(ele)
                with open('json_data.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(json_load))
                return render(request, "temp.html", {'context': json_load})
        return render(request, "error.html", {'context' : 'id__not_exist', 'id': request.POST.get('id')})
    else:
        return render(request, "error.html", {'context' : 'method_error'})




# def api_home(request, *args, **kwargs):
#     # print(dir(request))
#     print('____________')
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     # data['headers'] = request.headers
#     print(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
