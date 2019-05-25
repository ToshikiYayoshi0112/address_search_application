import requests
#岩手県八幡平市大更 の情報を requestsモジュールで取得

response = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287111")

print(response)

# 演習2;別の郵便番号で取得
response_01 = requests.get(url="http://zipcloud.ibsnet.co.jp/api/search?zipcode=8370926")

data = response.json()

