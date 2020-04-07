import serialcomm

def handle_get(request):
    return ""

def handle_post(req):
    return "" 
    
def request_handler(request):
    if request["method"]=='POST' or request["method"]=='post':
        handle_post(request['form'])
    
    html = '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1>Lamp Control</h1>
                <form action="/sandbox/sc/ayesha23/dex04/design_ex4.py" method="post">
                    <label for="red">Red (between 0 and 255):</label>
                    <input type="range" id="red" name="red" min="0" max="255">
                    <br>
                    <label for="green">Green (between 0 and 255):</label>
                    <input type="range" id="green" name="green" min="0" max="255">
                    <br>
                    <label for="blue">Blue (between 0 and 255):</label>
                    <input type="range" id="blue" name="blue" min="0" max="255">
                    <br>
                    <input type="submit">
                </form>
            </body>
        </html>
    '''
    return html
    
