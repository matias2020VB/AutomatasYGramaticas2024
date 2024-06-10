from music_manager import search_song_by_title_or_artist, load_songs, format_duration, mostrar_informacion_artista, list_top_songs_by_artist, addsong, find_last_index
from music_manager import validar_y_concatenar_csv

# PROFE! se ha resuelto el problema de que cuando se incertaba un registro manualmente no actualizaba el indice, eso YA! funciona.
# Implementamos la funcion de copiar de un archivo.csv a el original "spotify_and_youtube 2024.csv", actualizando el indice.
# El unico problema que no hemos podido solucionar es que cuando copia de un archivo los registros para escribirlo en el archivo original "spotify_and_youtube 2024.csv"
# Estos registros los copia escribiendo una coma luego del indice de esta manera:
# 20727,,Test Artist,Valid Test File,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,spotify:track:0d28khcov6AiegSCpG5TuT,188400,https://www.youtube.com/watch?v=dQw4w9WgXcQ,200,600
# 20728,,Test Artist,Valid Test File,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,spotify:track:1foMv2HQwfQ2vntFf9HFeG,280200,https://www.youtube.com/watch?v=dQw4w9WgXcQ,40,800
# 20729,,Test Artist,Valid Test File,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,spotify:track:64dLd6rVqDLtkXFYrEUHIU,228993,https://www.youtube.com/watch?v=dQw4w9WgXcQ,771,1023
# 20730,,Test Artist,Valid Test File,https://open.spotify.com/artist/3AA28KZvwAUcZuOKwyblJQ,spotify:track:0q6LuUqGLUiCPP1cbdwFs3,199931,https://www.youtube.com/watch?v=dQw4w9WgXcQ,7,213
# No hemos podido solucionar esto, pero el programa funciona correctamente, realizamos los testeos con los archivitos de prueba que nos brindaron por cátedra.

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
                    duration_ms = float(song.get('Duration_ms', 0))
                    duration = format_duration(duration_ms)
                    print(f"Artista: {artist}, Título: {track}, Duración: {duration}")
            else:
                print("No se encontraron resultados.")

        elif choice == '2':
            list_top_songs_by_artist(songs)
            pass
        
        elif choice == '3':
            print("Insertar un registro")
            print("1- Forma Manual")
            print("2- Formato .CSV")
            opcion =  input("Digite opcion: ")
            if opcion == '1':
                find_last_index(file_path)
                addsong(file_path)
            elif opcion =='2':
                new_path = input("Ingrese la ruta del archivo .csv que desea agregar: ")
                if not new_path.endswith('.csv'):
                    print("El archivo que ha proporcionado no es un archivo .csv")
                    return
                validar_y_concatenar_csv(new_path='01.csv', file_path_destino='spotify_and_youtube 2024.csv')
                

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

