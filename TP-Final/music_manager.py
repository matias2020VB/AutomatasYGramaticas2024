import csv  # Importar módulo para manejo de archivos CSV
import re  # Importar módulo para expresiones regulares
from datetime import timedelta  # Importar timedelta para manejo de duraciones
import os


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
    title = input("Ingrese el título de la canción: ")  # Pedir título de la canción
    artist = input("Ingrese el nombre del artista: ")  # Pedir nombre del artista
    album = input("Ingrese el nombre del álbum: ")  # Pedir nombre del álbum
    url_spotify = input("Ingrese la URL de Spotify de la canción: ")  # Pedir URL de Spotify
    uri = input("Ingrese el URI de Spotify de la canción: ")  # Pedir URI de Spotify
    duration_ms = input("Ingrese la duración en milisegundos: ")  # Pedir duración en milisegundos
    url_youtube = input("Ingrese la URL de YouTube: ")  # Pedir URL de YouTube
    likes = input("Ingrese la cantidad de likes: ")  # Pedir cantidad de likes
    views = input("Ingrese la cantidad de views: ")  # Pedir cantidad de vistas

    if not re.match(r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$', url_spotify):  # Validar URL de Spotify
        print("URL de Spotify no válida.")
        return

    if not re.match(r'^\d+$', duration_ms):  # Validar duración
        print("Duración no válida.")
        return

    if not re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$', url_youtube):  # Validar URL de YouTube
        print("URL de YouTube no válida.")
        return
    
    if int(likes) > int(views):  # Validar que likes no sean mayores que vistas
        print("El número de likes no puede ser mayor que el de views.")
        return

    
    # Crea diccionario con la nueva canción
    new_song = {
        "Index": last_index,
        "Title": title,
        "Artist": artist,
        "Album": album,
        "Url_spotify": url_spotify,
        "Uri": uri,
        "Duration_ms": int(duration_ms),
        "Url_youtube": url_youtube,
        "Likes": likes,
        "Views": views,
        "Danceability": "0.0",
        "Energy": "0.0",
        "Key": "0",
        "Loudness": "0.0",
        "Speechiness": "0.0",
        "Acousticness": "0.0",
        "Instrumentalness": "0.0",
        "Liveness": "0.0",
        "Valence": "0.0",
        "Tempo": "0.0",
        "Channel": "0.0",
        "Comments": "0.0",
        "Licensed": "0.0",
        "Stream": "0.0",
        "official_video": "0.0",
        
    }
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as file: # Abrir archivo en modo append
            writer = csv.DictWriter(file, fieldnames=new_song.keys()) # Crear escritor de CSV
            # Write header if the file is empty
            file.seek(0, 2)  # Move the cursor to the end of the file
            if file.tell() == 0:  # Check if the file is empty
                writer.writeheader()
            writer.writerow(new_song)
        print("Canción agregada correctamente.")
    except Exception as e:
        print(f"Error al agregar la canción: {e}")


# Insercion de canciones por medio de otro archivo CSV.

def validar_y_concatenar_csv(new_path, file_path_destino):
    
    def validar_datos_registro(registro):
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

    last_index = find_last_index(file_path_destino)

    with open(file_path_destino, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ["Index", "Title", "Artist", "Album", "Url_spotify", "Uri", "Duration_ms", "Url_youtube", "Likes", "Views"]
        if not file_exists:
            file.write(','.join(fieldnames) + '\n')  # Escribir la cabecera del archivo
        for registro in registros_validos:
            registro_filtrado = {campo: registro.get(campo, '') for campo in fieldnames}
            registro_filtrado['Index'] = last_index
            last_index += 1
            file.write(','.join(str(registro_filtrado[campo]) for campo in fieldnames)+'\n')
    print("Archivos concatenados correctamente.")


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