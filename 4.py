from geopy.geocoders import Nominatim

def find_southernmost_city(cities):
    geolocator = Nominatim(user_agent="southernmost_city_finder")
    southernmost_city = None
    min_latitude = float('inf')

    for city in cities:
        location = geolocator.geocode(city.strip())
        if location:
            latitude = location.latitude
            print(f"{city.strip()}: Широта {latitude:.6f}")
            if latitude < min_latitude:
                min_latitude = latitude
                southernmost_city = city.strip()
        else:
            print(f"Город {city.strip()} не найден.")
    
    return southernmost_city

if __name__ == "__main__":
    # Ввод списка городов
    cities_input = input("Введите список городов через запятую: ")
    cities_list = cities_input.split(',')

    # Нахождение самого южного города
    southernmost_city = find_southernmost_city(cities_list)

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить самый южный город.")
