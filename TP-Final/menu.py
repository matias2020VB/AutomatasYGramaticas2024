from music_manager import search_song_by_title_or_artist, load_songs, format_duration, mostrar_informacion_artista


def menu():
    file_path = 'spotify_and_youtube 2024.csv'
    songs = load_songs(file_path)

    while True:
        print("\n--- MENÚ ---")
        print("1 - Buscar por título o artista")
        print("2 - Mostrar los 10 temas con mayor reproducciones de un artista")
        print("3 - Insertar un registro")
        print("4 - Mostrar la cantidad de álbumes de un artista")
        print("5 - Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            query = input("Ingrese el título de la canción o el nombre del artista: ")
            # Buscar canciones por título o artista
            results = search_song_by_title_or_artist(query, songs)
            if results:
                print("\nResultados:")
                for song in results:
                    artist = song.get('Artist', 'Desconocido')
                    track = song.get('Track', 'Desconocido')
                    duration = format_duration(song.get('Duration_ms', 0))
                    print(f"Artista: {artist}, Título: {track}, Duración: {duration}")
            else:
                print("No se encontraron resultados.")

        elif choice == '2':
            
            pass

        elif choice == '3':
            
            pass

        elif choice == '4':
            artista = input("Nombre del artista: ")
            mostrar_informacion_artista(artista, songs)

        elif choice == '5':
            print("¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()

