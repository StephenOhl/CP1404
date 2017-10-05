"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
assert len(song_list.songs) > 0  # assuming CSV file is not empty
print(song_list)


# TODO: add tests below to show the various required methods work as expected
# test sorting songs

# test adding a new Song

# test get_song()

# test getting the number of required and learned songs (separately)

# test saving songs (check CSV file manually to see results)
song_list.save_songs("songs.csv")