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

    def set_learnt(self):
        self.is_required = True

    def set_not_learnt(self):
        self.is_required = False

    def __str__(self):
        return "\'{}\' by {} ({:4}) {}".format(self.title, self.artist, self.year, (('', '(learned)')[self.is_required]))
