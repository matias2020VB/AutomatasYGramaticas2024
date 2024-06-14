import csv  # Importar módulo para manejo de archivos CSV
import re  # Importar módulo para expresiones regulares
from datetime import timedelta  # Importar timedelta para manejo de duraciones
import pathlib
from dataclasses import dataclass

#Codigo para abrir y manejar el archivo CSV
@dataclass
class SongsDto:
    track: str
    artist: str
    album: str
    duration_ms: int
    views: int
    likes: int
    uri: str
    url: str

def parse_csv() -> list:
    songs = []
    try:
        with open(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                song = SongsDto(
                    row['Track'],
                    row['Artist'],
                    row['Album'],
                    row['Duration_ms'],
                    row['Views'],
                    row['Likes'],
                    row['Url_spotify'],
                    row['Url_youtube'],
                )
                songs.append(song)
        return songs
    except (FileNotFoundError):
        print("File not found")
        exit(1)

# Punto 1: Cargar canciones desde un archivo CSV
def load_songs(file_path):
    songs = []  # Lista para almacenar las canciones
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Abrir el archivo en modo lectura
            csv_reader = csv.DictReader(file)  # Crear un lector de CSV que devuelve diccionarios
            for row in csv_reader:  # Iterar sobre cada fila del CSV
                songs.append(row)  # Agregar la fila a la lista de canciones
        return songs  # Devolver la lista de canciones
    except FileNotFoundError:  # Manejar error si el archivo no se encuentra
        print(f"El archivo '{file_path}' no fue encontrado.")
        return []
    except Exception as e:  # Manejar cualquier otro error
        print(f"Error al cargar las canciones: {e}")
        return []

# Buscar canciones por título o artista y ordenar por reproducciones
def search_song_by_title_or_artist(query, songs):
    matches = []  # Lista para almacenar coincidencias
    for song in songs:  # Iterar sobre cada canción
        if query.lower() in song['Artist'].lower():  # Verificar si el artista coincide con la búsqueda
            matches.append(song)  # Agregar la canción a las coincidencias

    # Ordenar por cantidad de reproducciones de manera descendente
    def get_stream_value(song):
        stream_value = float(song.get('Stream', '0') or '0')  # Obtener el valor de reproducciones
        return int(stream_value)  # Devolver el valor como entero

    matches.sort(key=get_stream_value, reverse=True)  # Ordenar coincidencias por reproducciones
    return matches  # Devolver la lista de coincidencias

# Convertir milisegundos a formato HH:MM:SS
def format_duration(ms):
    """Convierte milisegundos a formato HH:MM:SS."""
    try:
        duration = timedelta(milliseconds=int(ms))  # Convertir milisegundos a timedelta
        hours, remainder = divmod(duration.seconds, 3600)  # Calcular horas y resto
        minutes, seconds = divmod(remainder, 60)  # Calcular minutos y segundos
        return f"{hours:02}:{minutes:02}:{seconds:02}"  # Formatear como HH:MM:SS
    except ValueError:  # Manejar error de conversión
        return "00:00:00"

# Punto 2: Listar las 10 canciones más reproducidas de un artista
def list_top_songs_by_artist(songs):
    """Muestra los 10 temas con mayor reproducciones de un artista."""
    artist_name = input("Ingrese el nombre del artista: ").strip()  # Pedir nombre del artista

    top_songs = []  # Lista para almacenar las canciones del artista
    for song in songs:  # Iterar sobre cada canción
        if song.get('Artist', '').strip().lower() == artist_name.lower():  # Comparar nombre del artista
            track_name = song.get('Track', 'Unknown')  # Obtener nombre del tema
            duration_ms = float(song.get('Duration_ms', 0))  # Obtener duración en milisegundos
            duration = format_duration(duration_ms)  # Formatear duración
            views_str = song.get('Views', '0')  # Obtener número de vistas
            views = float(views_str) if views_str else 0.0  # Convertir vistas a número
            top_songs.append({
                'artist': artist_name,
                'track': track_name,
                'duration': duration,
                'views': views
            })  # Agregar canción a la lista

    top_songs.sort(key=lambda x: x['views'], reverse=True)  # Ordenar canciones por vistas

    print(f"\nTop 10 temas de {artist_name} por reproducciones:")  # Mostrar título
    for i, song in enumerate(top_songs[:10], start=1):  # Iterar sobre las 10 primeras canciones
        artist = song['artist']  # Obtener nombre del artista
        track = song['track']  # Obtener nombre del tema
        duration = song['duration']  # Obtener duración
        views = song['views'] / 1_000_000  # Convertir vistas a millones
        print(f"{i}. Artista: {artist}, Tema: {track}, Duración: {duration}, Reproducciones: {views:.2f} millones")  # Mostrar información de la canción
    input("Presiona una tecla para continuar...")  # Pausar la ejecución

# Punto 3: Agregar una canción de forma manual al archivo CSV

# Función para determinar el siguiente Indice disponible
def find_last_index(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            last_index = []
            for row in reader:
                try:
                    last_index.append(int(row['Index']))
                except ValueError:
                    print(f"Valor no válido en la columna 'Index': {row['Index']}")
            if last_index:
                return max(last_index) + 1
            else:
                return 1
    except FileNotFoundError:
                return 1

def addsong(file_path):
    last_index = find_last_index(file_path)
    title = input("Ingrese el título de la canción: ")  
    artist = input("Ingrese el nombre del artista: ")  
    album = input("Ingrese el nombre del álbum: ")  
    url_spotify = input("Ingrese la URL de Spotify de la canción: ")  
    uri = input("Ingrese el URI de Spotify de la canción: ")  
    duration_ms = input("Ingrese la duración en milisegundos: ")  
    url_youtube = input("Ingrese la URL de YouTube: ")  
    likes = input("Ingrese la cantidad de likes: ")  
    views = input("Ingrese la cantidad de views: ")  

    # Funciones para validar las URL
    
    def validate_spotify_url(url_spotify):
        pattern = r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$'
        return re.match(pattern, url_spotify) is not None
        
    def validate_youtube_url(url_youtube):
        pattern = r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$'
        return re.match(pattern, url_youtube) is not None
    
    def validate_duration(duration_ms):
        pattern = r'^\d+$'
        return re.match(pattern, duration_ms) is not None
    
    def validate_spotify_uri(uri):
        pattern = r'spotify:track:[a-zA-Z0-9]{22}'
        return re.match(pattern, uri) is not None
    
    def validate_likes(likes, views):
        if int(likes) > int(views):  
            print("El número de likes no puede ser mayor que el de views.")
            return


    # Crea diccionario con la nueva canción
    new_song =  {"Index": last_index, "Title": title, "Artist": artist, "Album": album, "Url_spotify": url_spotify,
                "Uri": uri, "Duration_ms": int(duration_ms), "Url_youtube": url_youtube, "Likes": likes, "Views": views,
                # Valores por defecto
                "Danceability": "0.0", "Energy": "0.0", "Key": "0", "Loudness": "0.0", "Speechiness": "0.0", "Acousticness": "0.0",
                "Instrumentalness": "0.0", "Liveness": "0.0", "Valence": "0.0", "Tempo": "0.0", "Channel": "0.0",
                "Comments": "0.0", "Licensed": "0.0", "Stream": "0.0", "official_video": "0.0",
                    
    }
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file: # Abrir archivo en modo append
            # Creamos un escritor de CSV
            writer = csv.DictWriter(file, fieldnames=new_song.keys()) 
            # Escribe la cabecera si el archivo está vacío
            # Moviendo el cursor al final del archivo y verificando si está vacío
            # Chequeamos si el archivo esta vacio 
            file.seek(0, 2)  
            if file.tell() == 0:  
                writer.writeheader()
            writer.writerow(new_song)
        print("Canción agregada correctamente.")
    except Exception as e:
        print(f"Error al agregar la canción: {e}")

# Punto 3 (Continuación): Agregar una canción desde un archivo CSV

def manager_csv(new_path, main_path):
    # Funciones en las que validamos cada URL, duración, URI y likes.
    def validate_spotify_url(url_spotify):
        pattern = r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$'
        return re.match(pattern, url_spotify) is not None

    def validate_youtube_url(url_youtube):
        pattern = r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$'
        return re.match(pattern, url_youtube) is not None

    def validate_duration(duration_ms):
        pattern = r'^\d+$'
        return re.match(pattern, duration_ms) is not None

    def validate_spotify_uri(uri):
        pattern = r'spotify:track:[a-zA-Z0-9]{22}'
        return re.match(pattern, uri) is not None

    def validate_likes(likes, views):
        try:
            likes = int(likes)
            return likes <= int(views)
        except ValueError:
            return False

    # Encontrar el último índice
    def find_last_index(path):
        try:
            with open(path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                if rows:
                    return int(rows[-1]['Index'])
                else:
                    return -1
        except FileNotFoundError:
            return -1

    # Leemos el archivo .csv
    with open(new_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        # Verificamos que las columnas solicitadas estén dentro del archivo subido.
        requested_columns = ['Artist','Url_spotify', 'Track', 'Album', 'Uri', 'Duration_ms',
                            'Url_youtube', 'Views', 'Likes']

        for column in requested_columns:
            if column not in fieldnames:
                print(f"La columna '{column}' no se ha encontrado en el archivo subido.")
                return

        # Validación de datos del archivo subido
        for row in reader:
            last_index = find_last_index(main_path) + 1
            new_song = [last_index]

            artist = row['Artist']
            new_song.append(artist)

            track = row['Track']
            new_song.append(track)

            album = row['Album']
            new_song.append(album)

            # Validación para la URL de Spotify
            url_spotify = row['Url_spotify']
            if not validate_spotify_url(url_spotify):
                print(f"URL de Spotify no válida: {url_spotify}")
                continue
            new_song.append(url_spotify)

            # Validación para la URI de Spotify
            uri = row['Uri']
            if not validate_spotify_uri(uri):
                print(f"URI de Spotify no válida: {uri}")
                continue
            new_song.append(uri)

            # Validación para la duración de la canción.
            duration_ms = row['Duration_ms']
            if not validate_duration(duration_ms):
                print(f"Duración no válida: {duration_ms}")
                continue
            new_song.append(duration_ms)

            # Añadir valores por defecto para campos adicionales
            defaults = {
                "Danceability": "0.0", "Energy": "0.0", "Key": "0", "Loudness": "0.0",
                "Speechiness": "0.0", "Acousticness": "0.0", "Instrumentalness": "0.0",
                "Liveness": "0.0", "Valence": "0.0", "Tempo": "0.0", "Channel": "0.0",
                "Comments": "0.0", "Licensed": "0.0", "Stream": "0.0", "official_video": "0.0",
            }
            new_song.extend(defaults.values())

            # Validación para la URL de YouTube
            url_youtube = row['Url_youtube']
            if not validate_youtube_url(url_youtube):
                print(f"URL de YouTube no válida: {url_youtube}")
                continue
            new_song.append(url_youtube)

            # Comprobación de que los likes no sean mayores que las vistas
            likes = row['Likes']
            views = row['Views']
            if not validate_likes(likes, views):
                print(f"Likes no pueden ser mayores que Views: {likes} > {views}")
                continue
            new_song.append(likes)
            new_song.append(views)

            # Inserción de la nueva canción en el archivo
            with open(main_path, 'a', newline='', encoding='utf-8') as music_file:
                music_writer = csv.writer(music_file)
                if last_index == 0:
                    headers = ["Index", "Artist", "Url_spotify", "Track", "Album","Uri", "Danceability", "Energy",
                                "Key", "Loudness","Speechiness","Acousticness","Instrumentalness","Liveness","Valence",
                                "Tempo","Duration_ms", "Url_youtube", "Title", "Channel", "Views", "Likes", "Comments", 
                                "Licensed", "official_video", "Stream"]
                    music_writer.writerow(headers)
                music_writer.writerow(new_song)
            print("Canciones agregadas con éxito!")
            
                
# Punto 4: Mostrar información de un artista

def mostrar_informacion_artista(artista, registros):
        """Muestra la cantidad de álbumes, nombres de álbumes, cantidad de canciones y duración total por álbum de un artista."""
        albums = {}  # Diccionario para almacenar información de los álbumes
        
        for registro in registros:  # Iterar sobre cada registro
            if registro['Artist'].lower() == artista.lower():  # Comparar artista en minúsculas
                album = registro['Album']  # Obtener el nombre del álbum
                duracion = int(float(registro['Duration_ms']))  # Convertir duración a milisegundos
                if album not in albums:  # Inicializa un nueva entrada para el album
                    albums[album] = {'canciones': 0, 'duracion_total': 0}  
                albums[album]['canciones'] += 1  # Incrementar contador de canciones
                albums[album]['duracion_total'] += duracion  # Sumar duración total de la cancion al album

        if not albums:  # Si no se encontraron álbumes
            print(f"No se encontraron álbumes para el artista '{artista}'.")
            return

        print(f"Artista: {artista}")  # Mostrar nombre del artista
        print(f"Cantidad de álbumes: {len(albums)}")  # Mostrar cantidad de álbumes
        
        #Mostrar informacion detallada de cada album
        for album, info in albums.items():  # Iterar sobre cada álbum y su información
            duracion_total_minutos = info['duracion_total'] // 60000  # Calcula minutos de la duracion total de cada album
            duracion_total_segundos = (info['duracion_total'] % 60000) // 1000  # Calcular segundos restantes de la duracion total de cada album
            
            print(f"Álbum: {album}")  # Mostrar nombre del álbum
            print(f"  Canciones: {info['canciones']}")  # Mostrar cantidad de canciones
            print(f"  Duración total: {duracion_total_minutos} minutos y {duracion_total_segundos} segundos")  # Mostrar duración total
            print("-" * 50)