import webbrowser

class Movie():
    # using this """ syntax we can add the value of the __doc__ in-built class variable to the class
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # here '_' are a way for python to tell us that name 'init' is essentialy
    # reserved in python and this is a special function/method.
    # __init__ initializes or creates space in memory.
    # here "self" refers to the object being created. "self" is just the name of
    # the object and could be anything like udacity, akshit etc. It's not a
    # keyword.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
