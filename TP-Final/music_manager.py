import csv
import re
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
    """Convierte milisegundos a formato HH:MM:SS."""
    try:
        duration = timedelta(milliseconds=int(ms))
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    except ValueError:
        return "00:00:00"

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




def list_top_songs_by_artist(songs):
    """Muestra los 10 temas con mayor reproducciones de un artista."""
    artist_name = input("Ingrese el nombre del artista: ").strip()

    top_songs = []
    for song in songs:
        if song.get('Artist', '').strip().lower() == artist_name.lower():
            track_name = song.get('Track', 'Unknown')
            duration_ms = float(song.get('Duration_ms', 0))
            duration = format_duration(duration_ms)
            views_str = song.get('Views', '0')
            views = float(views_str) if views_str else 0.0
            top_songs.append({
                'artist': artist_name,
                'track': track_name,
                'duration': duration,
                'views': views
            })

    top_songs.sort(key=lambda x: x['views'], reverse=True)

    print(f"\nTop 10 temas de {artist_name} por reproducciones:")
    for i, song in enumerate(top_songs[:10], start=1):
        artist = song['artist']
        track = song['track']
        duration = song['duration']
        views = song['views'] / 1_000_000
        print(f"{i}. Artista: {artist}, Tema: {track}, Duración: {duration}, Reproducciones: {views:.2f} millones")
    input("Presiona una tecla para continuar...")






def addsong(file_path):
    title = input("Ingrese el título de la canción: ")
    artist = input("Ingrese el nombre del artista: ")
    album = input("Ingrese el nombre del álbum: ")
    url_spotify = input("Ingrese la URL de Spotify de la canción: ")
    uri = input("Ingrese el URI de Spotify de la canción: ")
    duration_ms = input("Ingrese la duración en milisegundos: ")
    url_youtube = input("Ingrese la URL de YouTube: ")
    likes = input("Ingrese la cantidad de likes: ")
    views = input("Ingrese la cantidad de views: ")

    if not re.match(r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$', url_spotify):
        print("URL de Spotify no válida.")
        return

    if not re.match(r'^\d+$', duration_ms):
        print("Duración no válida.")
        return

    if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$', url_youtube):
        print("URL de YouTube no válida.")
        return
    
    if int(likes) > int(views):
        print("El número de likes no puede ser mayor que el de views.")
        return
    
    new_song = {
        "Title": title,
        "Artist": artist,
        "Album": album,
        "Url_spotify": url_spotify,
        "Uri": uri,
        "Duration_ms": int(duration_ms),
        "Url_youtube": url_youtube,
        "Likes": likes,
        "Views": views,
    }

    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=new_song.keys())
            # Write header if the file is empty
            file.seek(0, 2)  # Move the cursor to the end of the file
            if file.tell() == 0:  # Check if the file is empty
                writer.writeheader()
            writer.writerow(new_song)
        print("Canción agregada correctamente.")
    except Exception as e:
        print(f"Error al agregar la canción: {e}")







def validar_y_concatenar_csv(new_path, file_path_destino):
    """Valida los datos de un archivo CSV y los concatena al archivo destino."""

    def validar_datos_registro(registro):
        """Valida los datos de un registro de canción."""
        if not re.match(r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$', registro.get('Url_spotify', '')):
            print(f"URL de Spotify no válida: {registro.get('Url_spotify', '')}")
            return False
        if not re.match(r'^\d+$', registro.get('Duration_ms', '')):
            print(f"Duración no válida: {registro.get('Duration_ms', '')}")
            return False
        if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$', registro.get('Url_youtube', '')):
            print(f"URL de YouTube no válida: {registro.get('Url_youtube', '')}")
            return False
        if int(registro.get('Likes', 0)) > int(registro.get('Views', 0)):
            print(f"Likes no pueden ser mayores que Views: {registro.get('Likes', 0)} > {registro.get('Views', 0)}")
            return False
        return True

    def leer_y_validar_csv(new_path):
        """Lee un archivo CSV y devuelve los registros válidos."""
        registros_validos = []
        try:
            with open(new_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if validar_datos_registro(row):
                        registros_validos.append(row)
        except FileNotFoundError:
            print(f"El archivo '{new_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return registros_validos

    registros_validos = leer_y_validar_csv(new_path)
    
    if not registros_validos:
        print("No hay registros válidos para concatenar.")
        return
    
    try:
        file_exists = False
        with open(file_path_destino, mode='r', newline='', encoding='utf-8') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_path_destino, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ["Title", "Artist", "Album", "Url_spotify", "Uri", "Duration_ms", "Url_youtube", "Likes", "Views"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(registros_validos)

    print(f"{len(registros_validos)} registros válidos han sido concatenados exitosamente.")
