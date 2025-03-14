import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from weather_api.settings import KEY_FORECAST, URL_CITIES_RESERVAMOS, URL_ICON_WEATHER, URL_WEATHER
from django.core.cache import cache

from datetime import datetime

def GroupedData(extern_data): 
    datos_agrupados = []
    data = extern_data.get('list', [])
    fechas_vistas = set()

    for item in data:
        fecha_completa = item.get('dt_txt')
        
        if fecha_completa:
            # Extraer solo la parte de la fecha (YYYY-MM-DD)
            fecha = fecha_completa.split(" ")[0]

            if fecha not in fechas_vistas:  # Solo agregar si no se ha visto antes
                fechas_vistas.add(fecha)  # Marcar la fecha como vista

                temp_actual = item.get('main', {}).get('temp')
                temp_max = item.get('main', {}).get('temp_max')
                temp_min = item.get('main', {}).get('temp_min')
                weather_description = item.get('weather', [{}])[0].get('description')
                icon = item.get('weather', [{}])[0].get('icon')

                # Crear el diccionario con la información agrupada
                datos_agrupados.append({
                    'fecha': fecha,
                    'temperatura_actual': temp_actual,
                    'temperatura_maxima': temp_max,
                    'temperatura_minima': temp_min,
                    'clima': weather_description,
                    'icon': f"{URL_ICON_WEATHER}{icon}@2x.png"
                })
    
    return datos_agrupados


def GetCitiesByPopularity(data): 
    try:
        # Asegúrate de que 'data' sea una lista
        if not isinstance(data, list):
            raise ValueError("Los datos proporcionados no son una lista válida.")

        process_data = [
            item for item in data
            if item.get('result_type') == 'city' and float(item.get('popularity', 0)) > 0.1
        ]

        return process_data
    except Exception as e:
        print("Error en GetCitiesByPopularity: ", e)
        return []


def get_weather_for_city(lat, long):
    # Generamos una clave única para el cache basada en la latitud y longitud
    cache_key = f"weather_{lat}_{long}"

    # Intentamos obtener los datos del clima desde el caché
    cached_weather = cache.get(cache_key)
    if cached_weather:
        print("Datos obtenidos desde el caché")
        return cached_weather

    try:
        # Si no está en caché, hacer la solicitud a la API externa
        params = f"{URL_WEATHER}?lat={lat}&lon={long}&units=metric&lang=es&appid={KEY_FORECAST}"
        print("url: ", params)

        response = requests.get(params)
        print("response: ", response)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            datos_externos = response.json()  # Convertir la respuesta en formato JSON
            data_group = GroupedData(datos_externos)  # Agrupar los datos meteorológicos

            # Guardar los datos en caché por 15 minutos
            cache.set(cache_key, data_group, timeout=60*15)

            return data_group
        else:
            return None  # Si no se pudo obtener el clima, devolver None
    except Exception as e:
        print("Error al obtener el clima:", e)
        return None




@api_view(['GET'])
def GetCitiesFavorites(request):
    try:
        #URL de la API externa
        params = f"{URL_CITIES_RESERVAMOS}"

        # Hacer la solicitud GET con los parámetros
        response = requests.get(params)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 201:
            datos_externos = response.json()  # Convertir la respuesta en formato JSON

            # Filtrar las ciudades favoritas por popularidad
            favorite_cities = GetCitiesByPopularity(datos_externos)

            # Aquí almacenamos los datos combinados de las ciudades favoritas y el clima
            cities_with_weather = []

            for city in favorite_cities:
                # Extraer lat y long de cada ciudad (suponiendo que las ciudades tienen estos datos)
                lat = city.get('lat')
                long = city.get('long')

                # Si no tiene latitud o longitud, lo ignoramos
                if lat and long:
                    # Llamar a la función de clima con latitud y longitud
                    weather_data = get_weather_for_city(lat, long)
                    # Añadir los datos del clima a la ciudad
                    city['weather'] = weather_data
                    cities_with_weather.append(city)
                    # print("cities_with_weather: ", cities_with_weather)
            return Response(cities_with_weather, status=200)
        else:
            return Response({'error': f'No se pudo obtener los datos de la API externa {response}'}, status=500)
    except Exception as e: 
        print("Error: : ", e)
        return Response({'error': str(e)}, status=500)
