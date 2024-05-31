import csv
from datetime import timedelta


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
