import folium

# Координаты стадионов
stadiums_location = {
    "Лужники": [55.715551, 37.554191],
    "Спартак": [55.818015, 37.440262],
    "Динамо": [55.791540, 37.559809]
}

# Создаем карту с центром в Москве
moscow_map = folium.Map(location=[55.751244, 37.618423], zoom_start=11)

# Добавляем метки стадионов
for name, coords in stadiums_location.items():
    folium.Marker(location=coords, popup=name, tooltip=name).add_to(moscow_map)

# Сохраняем карту в файл
moscow_map.save("moscow_stadiums_map.html")

print("Карта создана и сохранена как 'moscow_stadiums_map.html'. Откройте этот файл в браузере.")
