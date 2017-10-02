# create your SongList class in this file
from song import Song


class SongList(Song):
    def __init__(self):
        self.songs = []

    def get_title(self, title):
        for item in song_list:
            if item[0] == title:
                return item

        return title + " not in list"

    def add_song(self, a_song):
        self.songs.append(a_song)

    def get_number_required(self):
        pass

    def get_number_learned(self):
        pass

    def load_songs(self, file_name):
        try:
            in_file = open(file_name, 'r')
            for line in in_file:
                songs = line.strip('\n').split(',')
                self.songs.append(songs)
        except:
            print("Error - File empty no songs to load")
        pass

    def save_songs(self):
        pass

    def sort_list(self):
        pass

    def __str__(self):
        count = -1
        for item in self.songs:
            count += 1
            return self.songs