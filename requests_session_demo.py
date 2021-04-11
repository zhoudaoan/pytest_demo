import requests

if __name__ == '__main__':
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/sessioncookie/iTestingIsGood')
    r = s.get('https://httpbin.org/cookies')
    print(r.text)
