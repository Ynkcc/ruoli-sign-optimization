import requests
from time import sleep

#百度的api(通用图像识别)
API_KEY = ""
SECRET_KEY = ""

def main(imgurl):
        
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token=" + get_access_token()
    payload = {"url":imgurl}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)
    return response.text
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

#我写的
def captchaHandler(capCode):
    a=[]
    for x in capCode["result"]["imageInfos"]:
        #别太快了，休息一下
        sleep(1)
        if capCode["result"]["name"] in main(x["path"]):
            a.append(x["code"])
    return {"right":a}