import requests


class AddressSearcher:

    def search(self, postal_code):
        url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"

        response = requests.get(url)
        response_dict = response.json()

        prefacture = response_dict["results"][0]["address1"]
        city = response_dict["results"][0]["address2"]
        town = response_dict["results"][0]["address3"]

        return f"{prefacture}{city}{town}"
