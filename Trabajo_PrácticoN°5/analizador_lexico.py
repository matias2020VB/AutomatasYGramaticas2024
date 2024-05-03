import csv
import os

# Ruta del archivo movies.csv
file_path = r'movies.csv'

# Funcion para cargar peliculas desde el archivo csv.
def load_movies():
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        movies = list(csv_reader)
    return movies

# Creamos una funcion para buscar peliculas por el titulo.
def search_movie_by_title(title):
    movies = load_movies()
    matches = []
    for movie in movies:
        if title.lower() in movie['Title'].lower():
            matches.append(movie)   
    return matches

# Funcion de búsqueda por plataforma y categoria.
def search_by_platform_and_category(plataform, category):
    print(plataform)
    print(category)
    movies = load_movies()
    matches = []
    for movie in movies:
        # Este condicional verifica con '1' si la película está disponible en la plataforma.
        # Luego se realiza una verificacion si la pelicula es de la categoria seleccionada.
        if movie[plataform] == '1' and movie['Age'] == category:
            matches.append(movie) 
    return matches

# Función para insertar una nueva película en el archivo: movies.csv
def movie_insert(new_movie):
    fild_names = ['Title', 'Year', 'Age','Rating', 'Netflix', 'Hulu', 'Prime Video', 'Disney+']
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fild_names)
        writer.writerow(new_movie)

