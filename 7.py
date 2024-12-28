import requests

YANDEX_GEOCODE_API_KEY = "0d997e8f-b415-4fd0-91b1-c9547916c893"

def find_district(address):
    geocode_url = f"https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": address,
        "format": "json",
        "kind": "district",
        "apikey": YANDEX_GEOCODE_API_KEY
    }
    response = requests.get(geocode_url, params=geocode_params).json()
    try:
        district = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['SubAdministrativeAreaName']
        print(f"Район: {district}")
    except (KeyError, IndexError):
        print("Не удалось определить район.")

# Вводим адрес через пользователя
address = input("Введите адрес (например, улица, город): ")
find_district(address)