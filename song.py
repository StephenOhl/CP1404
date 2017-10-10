# create your Song class in this file


class Song:
    def __init__(self, title='', artist='', year=0, is_required='y'):
        self.artist = artist
        self.title = title
        self.year = int(year)
        if is_required == 'y' or is_required == 'Y':
            self.is_required = True
        elif is_required == 'n' or is_required == 'N':
            self.is_required = False
        else:
            self.is_required = is_required

    def __str__(self):
        return "{} by {} ({:4}) {}".format(self.artist, self.title, self.year, self.is_required)
