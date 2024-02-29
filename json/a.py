import requests

base_url = "http://api.hclyz.com:81/mf"
response_url = "http://api.hclyz.com:81/mf/json.txt"

# 获取response_url中的JSON数据
response = requests.get(response_url)
data = response.json()

# 获取"pingtai"列表
pingtai_list = data["pingtai"]

for item in pingtai_list:
    address = item["address"]
    full_url = f"{base_url}/{address}"
    print(full_url)
