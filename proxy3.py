import requests, json

class Proxy3:
    def __init__(self):
        pass

    def proxy(self):
        r = requests.get('https://gimmeproxy.com/api/getProxy?post=true&protocol=http&maxCheckPeriod=3600')
        output = json.loads(r.text)
        #print(output);
        PROXY = output['ipPort']
        return [r]

proxy = Proxy3()
print(proxy.proxy())