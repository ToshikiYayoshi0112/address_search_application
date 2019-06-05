import requests


class AddressSearcher:
    def __init__(self):
        self.base_url = "http://zipcloud.ibsnet.co.jp/api/search"

    def search(self, postal_code):
        url = f"{self.base_url}?zipcode={postal_code}"

        response = requests.get(url)

        response_dict = response.json()

        if response_dict["results"] is None:
            return "該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。"

        prefacture = response_dict["results"][0]["address1"]

        city = response_dict["results"][0]["address2"]

        town = response_dict["results"][0]["address3"]

        return f"{prefacture}{city}{town}"
