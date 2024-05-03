from analizador_lexico import *

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Buscar por título")
        print("2 - Buscar por plataforma y categoría")
        print("3 - Insertar una nueva película")
        print("4 - Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            title = input("Ingrese el título de la película: ")
            results = search_movie_by_title(title)
            if results:
                print("\nResultados:")
                for movie in results:
                    print(movie['Title'])
            else:
                print("No se encontraron resultados.")

        elif choice == '2':
            platform = input("Ingrese la plataforma (Netflix, Hulu, Prime Video, Disney+): ")
            category = input("Ingrese la categoría (7+, 13+, 16+, etc.): ")
            results = search_by_platform_and_category(platform, category)
            if results:
                print("\nResultados:")
                for movie in results:
                    print(movie['Title'], "- Rating:", movie['Rating'])
            else:
                print("No se encontraron resultados.")

        elif choice == '3':
            title = input("Ingrese el título de la película: ")
            year = input("Ingrese el año: ")
            age = input("Ingrese la categoría (7+, 13+, 16+, etc.): ")
            rating = input("Ingrese el rating de su pelicula: ")
            netflix = input("Disponible en Netflix (1: Sí, 0: No): ")
            hulu = input("Disponible en Hulu (1: Sí, 0: No): ")
            prime_video = input("Disponible en Prime Video (1: Sí, 0: No): ")
            disney_plus = input("Disponible en Disney+ (1: Sí, 0: No): ")
            new_movie = {
                'Title': title,
                'Year': year,
                'Age': age,
                'Rating': rating,
                'Netflix': netflix,
                'Hulu': hulu,
                'Prime Video': prime_video,
                'Disney+': disney_plus
                
            }
            movie_insert(new_movie)
            print("Película insertada correctamente.")

        elif choice == '4':
            print("¡Adios!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            
if __name__ == '__main__':
    menu()
