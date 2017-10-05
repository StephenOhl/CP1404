# create your Song class in this file


class Song:
    def __init__(self, artist='', title='', year=0, is_required='n'):
        self.artist = artist
        self.title = title
        self.year = year
        self.is_required = is_required

    def __str__(self):
        return "{} by {} ({:4}) {}".format(self.artist, self.title, self.year, self.is_required)
