# create your SongList class in this file
from song import Song
from operator import attrgetter


class SongList(Song):
    def __init__(self):
        self.songs = []

    def get_title(self, title):
        for item in song_list:
            if item[0] == title:
                return item

        return title + " not in list"

    def add_song(self, title, artist, year, is_required):
        print(title)
        a_song = Song(title, artist, year, is_required)
        self.songs.append(a_song)

    def get_number_required(self):
        count = 0
        for item in self.songs:
            if item.is_required == 'n':
                count += 1
        return count

    def get_number_learned(self):
        number_learnt = 0
        for item in self.songs:
            if item.is_required == 'y':
                number_learnt += 1
        return number_learnt

    def load_songs(self, file_name):
        try:
            in_file = open(file_name, 'r')
            for line in in_file:
                a_song = line.strip('\n').split(',')
                self.add_song(a_song)
            in_file.close()
        except:
            print("Error - File empty no songs to load")

    def save_songs(self, file_name):
        out_file = open(file_name, 'w')
        for item in self.songs:
            print(item.title + ',' + item.artist + ',' + str(item.year) + ',' + item.is_required, file = out_file)
        out_file.close()

    def sort_list(self, sorting_key):
        sort(key=operator.attrgetter(sorting_key, self.title))
        pass

    def __str__(self):
        a_string = ''
        for i in range(len(self.songs)):
            a_string = a_string + self.songs[i].__str__() + '\n'
        return a_string