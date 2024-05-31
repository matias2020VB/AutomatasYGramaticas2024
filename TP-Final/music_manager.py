import csv
from datetime import timedelta
import re

def load_songs(file_path):
    songs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                songs.append(row)
        return songs
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al cargar las canciones: {e}")
        return []

def search_song_by_title_or_artist(query, songs):
    matches = []
    for song in songs:
        if query.lower() in song['Artist'].lower():
            matches.append(song)

    # Ordenar por cantidad de reproducciones de manera descendente
    def get_stream_value(song):
        stream_value = float(song.get('Stream', '0') or '0')
        return int(stream_value)

    matches.sort(key=get_stream_value, reverse=True)
    return matches


def format_duration(ms):
    try:
        # Convertir la duración a milisegundos
        total_seconds = float(ms) * 1000
        # Convertir los milisegundos a formato HH:MM:SS
        duration = timedelta(milliseconds=int(total_seconds))
        return str(duration)
    except ValueError:
        return "Formato de duración inválido"



def mostrar_informacion_artista(artista, registros):
    """Muestra la cantidad de álbumes, nombres de álbumes, cantidad de canciones y duración total por álbum de un artista."""
    albums = {} # Diccionario para almacenar información de los álbumes
    
    for registro in registros:
        if registro['Artist'].lower() == artista.lower():  # Comparar artista en minúsculas
            album = registro['Album']
            duracion = int(float(registro['Duration_ms']))  # Convertir duración a milisegundos
            if album not in albums:
                albums[album] = {'canciones': 0, 'duracion_total': 0}
            albums[album]['canciones'] += 1
            albums[album]['duracion_total'] += duracion

    if not albums:
        print(f"No se encontraron álbumes para el artista '{artista}'.")
        return

   
    print(f"Artista: {artista}")

    print(f"Cantidad de álbumes: {len(albums)}")
    
    for album, info in albums.items():
    # Calcular la duración total del álbum en minutos y segundos
        duracion_total_minutos = info['duracion_total'] // 60000
        duracion_total_segundos = (info['duracion_total'] % 60000) // 1000
        
        # Imprimir información del álbum
        print(f"Álbum: {album}")
        print(f"  Canciones: {info['canciones']}")
        print(f"  Duración total: {duracion_total_minutos} minutos y {duracion_total_segundos} segundos")




def validar_uri_spotify(uri):
    """Valida la URI de Spotify usando una expresión regular."""
    regex = r"^spotify:[a-zA-Z0-9:]+$"
    return re.match(regex, uri) is not None

def convertir_a_milisegundos(duracion):
    """Convierte una duración en formato 'mm:ss' a milisegundos."""
    minutos, segundos = map(int, duracion.split(':'))
    return (minutos * 60 + segundos) * 1000

def validar_likes_views(likes, views):
    """Valida que el número de likes no sea mayor que el de views."""
    return likes <= views

def leer_csv(archivo):
    """Lee un archivo CSV y devuelve una lista de registros."""
    registros = []
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            registros.append(row)
    return registros

def escribir_csv(archivo, registros):
    """Escribe una lista de registros a un archivo CSV."""
    campos = ['artista', 'track', 'album', 'uri_spotify', 'duracion', 'url_spotify', 'url_youtube', 'likes', 'views']
    with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for registro in registros:
            writer.writerow(registro)

def insertar_registro_manualmente():
    """Solicita al usuario los detalles de un registro y lo devuelve como un diccionario."""
    artista = input("Artista: ")
    track = input("Track: ")
    album = input("Album: ")
    uri_spotify = input("URI de Spotify: ")
    while not validar_uri_spotify(uri_spotify):
        print("URI de Spotify no válida. Debe seguir el formato 'spotify:tipo:identificador'.")
        uri_spotify = input("URI de Spotify: ")

    duracion = input("Duración (mm:ss): ")
    duracion_ms = convertir_a_milisegundos(duracion)
    url_spotify = input("URL de Spotify: ")
    url_youtube = input("URL de YouTube: ")
    likes = int(input("Likes: "))
    views = int(input("Views: "))
    while not validar_likes_views(likes, views):
        print("El número de likes no puede ser mayor que el de views.")
        likes = int(input("Likes: "))
        views = int(input("Views: "))

    return {
        'artista': artista,
        'track': track,
        'album': album,
        'uri_spotify': uri_spotify,
        'duracion': duracion_ms,
        'url_spotify': url_spotify,
        'url_youtube': url_youtube,
        'likes': likes,
        'views': views
    }

def insertar_registros_desde_csv():
    """Solicita al usuario el nombre de un archivo CSV y devuelve una lista de registros."""
    archivo = input("Nombre del archivo CSV: ")
    return leer_csv(archivo)