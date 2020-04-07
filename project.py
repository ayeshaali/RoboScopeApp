import serialcomm

def handle_get(request):
    return ""

def handle_post(req):
    return "hi" 
    
def request_handler(request):
    if request["method"]=='POST' or request["method"]=='post':
        return handle_post(request['form'])
    
    html = '''
        
    '''
    return html
    
