import requests

def find_nearest_pharmacy_overpass(latitude, longitude, radius=5000):
    """
    Находит ближайшую аптеку с использованием Overpass API.
    
    :param latitude: Широта точки
    :param longitude: Долгота точки
    :param radius: Радиус поиска в метрах (по умолчанию 5000 метров)
    :return: Название аптеки и координаты
    """
    url = "https://overpass-api.de/api/interpreter"
    
    # Создаем запрос для поиска аптек в указанном радиусе
    query = f"""
    [out:json];
    node["amenity"="pharmacy"](around:{radius},{latitude},{longitude});
    out body;
    """
    
    # Отправляем запрос в Overpass API
    response = requests.get(url, data=query)
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()
        
        # Проверяем, есть ли результаты
        if data["elements"]:
            pharmacy = data["elements"][0]
            name = pharmacy.get("tags", {}).get("name", "Неизвестно")  # Получаем название аптеки
            coords = (pharmacy["lat"], pharmacy["lon"])  # Координаты аптеки
            return name, coords
        else:
            print("Аптеки не найдены в указанном радиусе.")
            return None
    else:
        print(f"Ошибка API Overpass: {response.status_code}")
        return None

# Пример использования
if __name__ == "__main__":
    # Заданные координаты для поиска аптек (центр Москвы)
    latitude, longitude = 55.751244, 37.618423
    
    # Ищем ближайшую аптеку в радиусе 5 км
    pharmacy = find_nearest_pharmacy_overpass(latitude, longitude, radius=5000)
    
    if pharmacy:
        name, coords = pharmacy
        print(f"Ближайшая аптека: {name}")
        print(f"Координаты аптеки: {coords}")
