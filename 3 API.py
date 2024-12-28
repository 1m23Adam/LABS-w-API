import requests

def get_yandex_satellite_image(latitude, longitude, zoom=17, size=(650, 450), filename="yandex_satellite_image.png"):
    # Базовый URL Static API Яндекс.Карт
    base_url = "https://static-maps.yandex.ru/1.x/"

    # Параметры запроса
    params = {
        "ll": f"{longitude},{latitude}",
        "z": zoom,
        "size": f"{size[0]},{size[1]}",
        "l": "sat",  # Слой спутниковых снимков
    }

    # Запрос изображения
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Сохранение изображения в файл
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Спутниковый снимок сохранен как '{filename}'.")
    else:
        print(f"Ошибка получения изображения: {response.status_code} - {response.text}")

# Пример использования
latitude = 55.751244  # Координаты центра Москвы
longitude = 37.618423
get_yandex_satellite_image(latitude, longitude)
