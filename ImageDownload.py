import urllib.request
import os
import requests

def download_img(url, place, name):
    full_name = str(name) + ".jpg"
    path = "d:/images/naver/"+place
    name = os.path.join(path, full_name)
    print("파일 다운 시작" + name)
    urllib.request.urlretrieve(url, name)
    print("파일 전송 시작"+name)
    send_img(place)
    print("파일 전송 완료"+name)
    return "/resources/naver/" + place + "/" + full_name

def send_img(place):
    path = "d:/images/naver/"+place
    filenames = os.listdir(path)
    for i in filenames:
        files = open(path+'/'+i, 'rb')
        upload = {'file': files}
        obj = {'place': 'naver/'+place}
        #requests.post('http://ghckss.cafe24.com/rel/images', files=upload, data=obj)
        requests.post('http://203.247.240.40:8080/rel/images', files=upload, data=obj)
        files.close()
        os.remove(path + '/' + i)