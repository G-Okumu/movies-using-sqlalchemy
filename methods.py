from config import get_session
from models import Director, Movie

def create_director(name):
    session = get_session()
    new_director = Director(name=name)
    session.add(new_director)
    session.commit()
    
    print(f"Director {name} added")
    
def create_movie(title, genre, director_id):
    sess = get_session()
    new_movie = Movie(title=title, genre= genre, director_id=director_id)
    sess.add(new_movie)
    sess.commit()
    
    print(f"Movie {title} creatd")

def list_all_movies():
    sess = get_session()
    all_movies = sess.query(Movie).all()
    return all_movies

def search_movie(name):
    pass

if __name__ == '__main__':
    # create_director("Otoyo")
    
    # create_movie("Pengle part 2", "Luo Comedy", 1)
    # create_movie("Pengle part 1", "Luo Comedy", 2)
    
    for movie in list_all_movies():
        print(f"title:{movie.title} genre:{movie.genre}")