# Movie Management System with SQLAlchemy

This project demonstrates a simple movie management system using Python and SQLAlchemy. It allows you to create and manage movie records and their associated directors within a SQLite database.

## Project Structure

The project consists of the following key files:

- `methods.py`: Contains the functions to interact with the database (CRUD operations).
- `models.py`: Defines the database models for the `Director` and `Movie` entities.
- `config.py`: Sets up the database connection and session management.
- `Pipfile`: Manages project dependencies.

## Requirements

- Python 3.x
- SQLAlchemy

To install all dependencies, you can use `pipenv`:

```bash
pipenv install
```

## Running the project

- pipenv install
- pipenv shell
- python3 methods.py



## Database Configuration (config.py)

The `config.py` file sets up the database and SQLAlchemy session. It creates the SQLite database `movies.sqlite3` and initializes it with the required tables.

```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from director import Base

    Engine = create_engine('sqlite:///movies.sqlite3')

    # Creates all tables defined in models.py
    Base.metadata.create_all(Engine)

    Session = sessionmaker(bind=Engine)
    session = Session()

    def get_session():
        return session
```

- <b>Engine</b>: Establishes a connection to the SQLite database `movies.sqlite3`.
- <b>Base.metadata.create_all(Engine)</b>: Ensures all tables defined in the models are created.
- <b>get_session()</b>: Provides a new SQLAlchemy session for each database operation.


## Models (`models.py`)

This file defines the models for the two main entities: `Director` and `Movie`.

```python
    from sqlalchemy import Column, String, Integer, ForeignKey
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class Director(Base):
        __tablename__ = 'directors'
        id = Column(Integer(), primary_key=True)
        name = Column(String(32))
        movies = relationship('Movie', back_populates='director')

    class Movie(Base):
        __tablename__ = 'movies'
        id = Column(Integer(), primary_key=True)
        title = Column(String(55))
        genre = Column(String())
        director_id = Column(Integer(), ForeignKey('directors.id'))

        director = relationship('Director', back_populates='movies')
```
- <b>Director</b>: Represents a movie director, with columns for the director's ID and name. It has a one-to-many relationship with the `Movie` model.
- <b>Movie</b>: Represents a movie, with columns for movie ID, title, genre, and the foreign key `director_id` (which references a director). It has a many-to-one relationship with `Director`.
- `back_populates` attribute is used to establish a bidirectional relationship between the <i>`Director`</i> and <i>`Movie`</i> classes.  

    It allows SQLAlchemy to know that these two classes are related and that each one "points" to the other in a reciprocal way.
- The `Director` class has a relationship() with the Movie class, indicated by the movies attribute.
- The `movies` attribute in Director represents all the movies that a director is associated with.
- The `back_populates='director'` part means that the other side of the relationship (in the Movie class) refers to the Director as director.
- The `Movie` class has a relationship() with the Director class, indicated by the director attribute.
- The `director` attribute in Movie represents the director of a given movie.
- The `back_populates='movies'` part means that the other side of the relationship (in the Director class) refers to the Movie instances as movies.
- 

### How it Works Together:
- The `back_populates` attribute makes sure that changes to one side of the relationship are reflected on the other side.
    - For example, if you retrieve a Director from the database, the movies attribute will contain all the Movie objects associated with that director.
    - Similarly, if you retrieve a Movie, the director attribute will point to the associated Director object.
- This makes the relationship bidirectional: you can go from a Director to their movies, or from a Movie to its director.

    Example

    ```python
        # Create a new director and a movie
        director = Director(name="George Okumu")
        movie = Movie(title="Coding", genre="Software Engineer", director=director)

        # Access the movie from the director
        print(director.movies)  # [<Movie(title='Coding', genre='Software Engineer')>]

        # Access the director from the movie
        print(movie.director.name)  # "George Okumu"


## Usage

To use this project, you can uncomment and run the functions in `methods.py`. For example:

```python
if __name__ == '__main__':
    # create a new director
    # create_director("Otoyo")
    
    # Create movies
    # create_movie("Pengle part 2", "Luo Comedy", 1)
    # create_movie("Pengle part 1", "Luo Comedy", 2)
    
    # List all movies
    for movie in list_all_movies():
        print(f"title:{movie.title} genre:{movie.genre}")
```

## Pipfile

The Pipfile defines the project dependencies, including SQLAlchemy:


```python
    url = "https://pypi.python.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    sqlalchemy = "*"

    [requires]
    python_version = "3.1"

```

## Future Improvements

- Implement the `search_movie()` method to allow searching for movies by title.
- Add error handling for missing or incorrect data (e.g., when adding movies without valid director IDs).

## Conclusion

This project provides a simple foundation for managing movies and directors using SQLAlchemy and SQLite. You can extend it with more advanced functionality as needed, such as search features, pagination, or API integrations.
