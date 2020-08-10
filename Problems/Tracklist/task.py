def tracklist(**kwargs):
    for artist, album in kwargs.items():
        print(artist)
        for album_name, song in album.items():
            print(f'ALBUM: {album_name} TRACK: {song}')
