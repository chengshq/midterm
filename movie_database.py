import csv
import json
from urllib.request import urlopen

class Movie:


 def __init__(self, title, imdb_rating, director):
  self.title = title
  self.imdb_rating = imdb_rating
  self.director = director

  def find_highest_rated(self):
      with open("imdb_top250.csv") as file:
        reader = csv.reader(file)

        highest_score = 0.0
        for row in reader:
          if float(row[3]) > highest_score:
            best_movie.title = row[1]
            best_movie.director = row[2]
            best_movie.imdb_rating = float(row[3])


      return Movie(title, highest_score, director)


  def plot(movie_object):
    webservice_url = "http://www.omdbapi.com/?i=" + movie_object.imdb_id + "&plot=short&r=json"
    data = urlopen(webservice_url).read().decode("utf8")
    movie_data = json.loads(data)
    plot = movie_data["Plot"]

    return plot