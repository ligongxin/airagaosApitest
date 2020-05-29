#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/5/2818:17
#文件     :
#IDE      :PyCharm

import requests,json

class HttpRequest:

    def http_request(self,url,http_method,param):
        param = json.dumps(param)
        if http_method.upper()=='POST':
            try:
                res=requests.post(url,param)

            except Exception as e:
                print(e)
        else:
            try:
                res = requests.get(url, param)
            except Exception as e:
                print(e)
        return res


if __name__=='__main__':
    func=HttpRequest()
    url='http://aos.gw.airag-inc.cn/user/login'
    param={
	"account": "10000000104",
	"password": "123456"
}
    headers = {
        'Content-Type': 'application/json',
        'Origin': 'http://aos.airag-inc.cn',
        'Referer': 'http://aos.airag-inc.cn/cn/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'

    }

    res=func.http_request(url,'post',param)
    print(res.json())
    print(res.json()['obj']['accessToken'])
