from address_searcher import AddressSearcher


def main():
    # ユーザーからの郵便番号をうけとる
    postal_code = input("郵便番号は? >")

    # 郵便番号を使って地名をとってくる
    address_searcher = AddressSearcher()

    location = address_searcher.search(postal_code)

    # 地名をprintする
    print(location)


if __name__ == "__main__":
    main()
