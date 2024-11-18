# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import nvkey


# 오류 발생 추가 소스
import ssl 

def blog(keyword):
    ssl._create_default_https_context = ssl._create_unverified_context
    client_id = nvkey.CLIENT_KEY
    client_secret = nvkey.CLIENT_SECRET
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        res = response_body.decode('utf-8')
        print(type(res)) # 자료형(data type)을 확인
        dic_res = json.loads(res)  # json 문자열을 파이썬에 딕셔너리 자료형으로 변경
        print(type(dic_res)) # 자료형(data type)을 확인
        # print(dic_res['items'])
        return dic_res['items']
        
    else:
        print("Error Code:" + rescode)