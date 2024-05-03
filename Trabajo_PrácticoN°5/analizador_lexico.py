import csv
import os

# Ruta del archivo movies.csv

file_path = r'movies.csv'

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

    
def search_by_platform_and_category(plataform, category):
    print(plataform)
    print(category)
    
    movies = load_movies()
    matches = []
    for movie in movies:
        # Verificar si la película está disponible en la plataforma y coincide con la categoría
        if movie[plataform] == '1' and movie['Age'] == category:
            matches.append(movie) 
    return matches


def movie_insert(new_movie):
    fild_names = ['Title', 'Year', 'Age','Rating', 'Netflix', 'Hulu', 'Prime Video', 'Disney+']
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        #print(file)
        writer = csv.DictWriter(file, fieldnames=fild_names)
        writer.writerow(new_movie)
        #writer.save()
        
