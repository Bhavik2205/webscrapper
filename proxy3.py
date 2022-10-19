import requests, json

class Proxy3:
    def __init__(self):
        pass

    def proxy(self):
        r = requests.get('https://spys.me/proxy.txt')
        output = json.loads(r)
        print(output);
        PROXY = output['ipPort']
        return [r]

proxy = Proxy3()
print(proxy.proxy())