import folium
from geopy.distance import geodesic

# Последовательность точек (координаты)
path_points = [
    (55.751244, 37.618423),  # Точка 1 (центр Москвы)
    (55.715551, 37.554191),  # Точка 2 (Лужники)
    (55.818015, 37.440262),  # Точка 3 (Спартак)
    (55.791540, 37.559809)   # Точка 4 (Динамо)
]

# Вычисление длины пути
total_distance = 0
for i in range(len(path_points) - 1):
    total_distance += geodesic(path_points[i], path_points[i + 1]).kilometers

# Средняя точка пути
middle_index = len(path_points) // 2
middle_point = path_points[middle_index]

# Создание карты
moscow_map = folium.Map(location=path_points[0], zoom_start=11)

# Добавление пути на карту
folium.PolyLine(locations=path_points, color="blue", weight=5).add_to(moscow_map)

# Добавление точек на карту
for idx, coords in enumerate(path_points):
    folium.Marker(location=coords, popup=f"Точка {idx + 1}", tooltip=f"Точка {idx + 1}").add_to(moscow_map)

# Добавление метки средней точки
folium.Marker(
    location=middle_point,
    popup="Средняя точка",
    tooltip="Средняя точка",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(moscow_map)

# Сохранение карты
moscow_map.save("path_map.html")

print(f"Длина пути: {total_distance:.2f} км")
print("Карта создана и сохранена как 'path_map.html'. Откройте этот файл в браузере.")
