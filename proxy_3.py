import requests, json

class Proxy3:
    def __init__(self):
        pass

    def proxy(self):
        r = requests.get('https://gimmeproxy.com/api/getProxy?post=true&protocol=http&maxCheckPeriod=3600')
        output = json.loads(r.text)
        PROXY = output['ip']
        country = output['country']
        print(PROXY, country)
        return [PROXY, country]
proxy = Proxy3()
print(proxy.proxy())