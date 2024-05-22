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

