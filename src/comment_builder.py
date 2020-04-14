from imdb import IMDb

base_url = "https://www.imdb.com/title/tt"


def search_movie(title):
    try:
        movies = IMDb().search_movie(title)
        return IMDb().get_movie(movies[0].movieID)
    except:
        return "Error, title cannot be found."


def build_comment(movie):
    line_1 = "##__[" + movie["title"] + " (" + get_year(movie) + ")](" + base_url + str(movie.getID()) + "/)__"
    line_2 = "#####Directed by: " + get_director(movie)
    line_3 = "^(Rating: " + get_rating(movie) + "    | Genres: " + get_genre(movie) + "| Runtime: " + get_runtime(movie) \
             + " min)"
    return line_1 + "\n" + line_2 + "\n" + line_3


def get_runtime(movie):
    try:
        return str(movie["runtime"][0])
    except:
        return "N/A"


def get_rating(movie):
    try:
        return str(movie['rating'])
    except:
        return "N/A"


def get_year(movie):
    try:
        return str(movie['year'])
    except:
        return "TBD"


def get_director(movie):
    try:
        temp = ""
        for x in movie["director"]:
            if temp == "":
                temp += x["name"]
            else:
                temp += ", " + x["name"]
        return temp
    except:
        return "Unknown"


def get_genre(movie):
    try:
        temp = ""
        for x in movie["genres"]:
            if temp == "":
                temp += x
            else:
                temp += ", " + x
        return temp
    except:
        return "Unknown"
