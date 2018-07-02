import requests
import json

USERNAME = '438300986201'

url = 'http://www.worlduc.com/platformSys/space/SpaceHandler.ashx'
headers = {
        'Cookie': 'UM_distinctid=160d10c404051-0ce7423cadd888-3c604504-144000-160d10c40413ba; CNZZDATA1693849=cnzz_eid%3D1645265848-1515331368-http%253A%252F%252Fwww.worlduc.com%252F%26ntime%3D1515331368; ASP.NET_SessionId=bthnfrjy3koogw5ymf1zlzmz; BIGipServerweb_80=318967980.0.0000; WorldUC_ClientIdentity=7b4c8e8713fc47b8a2ce34c02cce9c42; SnsUserToken=token=+wYrCJ8vFjGv3zFSj9ncCiUE8xPRiVrx2r8irhRQ55QTn6xCm5YyVjeTp7H/3lioeEO21zlExrU=&headpic=201751116324DK3wg.png; LastLoginUser=%7B%22userid%22%3A1315555%2C%22username%22%3A%22%u6E58%u6F6D%u5927%u5B66%22%2C%22email%22%3A%22xtdx@worlduc.com%20%22%2C%22headpic%22%3A%22/uploadImage/head/x0/201751116324DK3wg.png%22%2C%22isenterprise%22%3A%22true%22%2C%22enterprisetype%22%3A1%7D; LastLoginEUser=%7B%7D'
    }


def pase_page(username):
    if  '@' in username and username.strip() != '':
        data = {'op': 'pwdSearch','t': '1','n': username}
    else:
        data = {'op': 'pwdSearch','t': '0','n': username}

    response_parse = requests.post(url,headers=headers,data=data)
    return restart_pwd(json.loads(response_parse.text))


def restart_pwd(response_parse):
    if response_parse.get('id') == -1:
        return '-1'   #该账号不存在
    else:
        print(response_parse)
        data = {'op': 'pwdReset','u': response_parse.get('id'),'p': 'Xiao2018'}
        response_restart = requests.post(url,headers=headers,data=data)
        return {'账号信息：':response_parse,'修改密码为':response_restart.text}
         
def reset_pwd(username):
    return pase_page(username)
