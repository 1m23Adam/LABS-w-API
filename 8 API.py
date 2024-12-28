import math

# Функция для вычисления расстояния между двумя точками по координатам
def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 1 градус = 111 км = 111 000 м
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю широту и считаем коэффициент для долготы
    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    # Вычисляем смещения по долготе и широте
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками
    distance = math.sqrt(dx * dx + dy * dy)
    return distance

# Главная функция программы
def main():
    print("Введите координаты дома (долгота и широта):")
    home_lon = float(input("Долгота: "))
    home_lat = float(input("Широта: "))
    
    print("Введите координаты университета (долгота и широта):")
    university_lon = float(input("Долгота: "))
    university_lat = float(input("Широта: "))
    
    # Вычисляем расстояние между домом и университетом
    distance = lonlat_distance((home_lon, home_lat), (university_lon, university_lat))
    
    print(f"Расстояние между вашим домом и университетом: {distance / 1000:.2f} км")

if __name__ == "__main__":
    main()
