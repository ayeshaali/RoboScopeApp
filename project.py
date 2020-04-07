import serialcomm 

def request_handler(request):
    extra = ""
    if request["method"]=='GET':
        if "serv" in request["values"]:
            return handle_get(request)
    elif request["method"]=='POST' or request["method"]=='post':
        extra = handle_post(request['form'])