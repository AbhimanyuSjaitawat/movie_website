import webbrowser

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        '''it creates instance for movies and give them space in memory '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """it will play the trailer of Movie """
        webbrowser.open(self.trailer_youtube_url)
