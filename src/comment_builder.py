from imdb import IMDb

base_url = "https://www.imdb.com/title/tt"


def search_movie(title):
    movies = IMDb().search_movie(title)
    return IMDb().get_movie(movies[0].movieID)


def build_comment(movie):
    line_1 = "##__[" + movie["title"] + " (" + str(movie['year']) + ")](" + base_url + str(movie.getID()) + "/)__"
    line_2 = "#####Directed by: " + director_to_string(movie)
    line_3 = "^(Rating: " + str(movie["rating"]) + "    | Genres: " + genre_to_string(movie) + "| Runtime: " + str(
        movie["runtime"][0]) + " min)"
    return line_1+"\n"+line_2+"\n"+line_3




def director_to_string(movie):
    temp = ""
    for x in movie["director"]:
        if temp == "":
            temp += x["name"]
        else:
            temp += ", " + x["name"]
    return temp


def genre_to_string(movie):
    temp = ""
    for x in movie["genres"]:
        if temp == "":
            temp += x
        else:
            temp += ", " + x
    return temp
