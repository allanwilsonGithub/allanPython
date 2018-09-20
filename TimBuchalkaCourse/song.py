class Song:
    """Class to represent a song

    Attributes:
        title(str): The title of the song
        artist (Artist): An artist object representing the song's creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method
        Args:
            title (str): initialises the 'title' attribute
            artist (Artist): the creator of the song
            duration: Default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration