import requests
import concurrent.futures
import re
import json

base_url = "http://api.hclyz.com:81/mf"
response_url = "http://api.hclyz.com:81/mf/json.txt"
output_file = "output.m3u8"
address_file = "address.txt"
address_list = []

response = requests.get(response_url)
data = response.json()
pingtai_list = data.get("pingtai")

with open(address_file, 'w') as af:
    for item in pingtai_list:
        pingtai_address = item.get("address")
        group_title = item.get("Number")   
        af.write(f"{base_url}/{pingtai_address}\n")
        address_list.append((pingtai_address, f"{base_url}/{pingtai_address}"))

output_file = open('output.m3u8', 'a')

with open('address.txt', 'r') as file:
    addresses = file.readlines()

for address_url in addresses:
    address_url = address_url.strip()
    
    print(f"Fetching data from {address_url}...")
    
    response = requests.get(address_url)
    
    print(f"Data fetched from {address_url}")
    
    try:
        data = response.json()
        zhubo_list = data.get("zhubo")
        if zhubo_list:
            output_file.write(f"{address_url}:\n")
            print(f"Writing addresses from {address_url} to output.m3u8")
            for zhubo in zhubo_list:
                address = zhubo.get("address")
                output_file.write(f"#EXTINF:-1,tvg-logo=\"\" group-title=\"\"\n")
                output_file.write(f"{address}\n")

#        else:
#           output_file.write(f"# No zhubo list found at {address_url}\n")
#            print(f"No zhubo list found at {address_url}")
    except json.JSONDecodeError:
        output_file.write(f"# Error: Failed to decode JSON from {address_url}\n")
        print(f"Error: Failed to decode JSON from {address_url}")


output_file.close()
