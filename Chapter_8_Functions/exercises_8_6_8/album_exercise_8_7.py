def make_album(artist_name, album_title, songs=None):
    """Return a dictionary with the artist name, album title, and optional number of songs."""
    if songs:
        return {'artist': artist_name, 'album': album_title, 'songs': songs}
    else:
        return {'artist': artist_name, 'album': album_title}


while True:
    print("\nPlease enter the information about your favorite artist:")
    print("(Enter 'q' to exit the form)")

    artist_name_input = input("Artist name: ")
    if artist_name_input.lower() == 'q':
        break

    album_name_input = input("Album name: ")
    if album_name_input.lower() == 'q':
        break

    songs_input = input("Please enter the number of songs in the album (or press Enter to skip): ")
    if songs_input.lower() == 'q':
        break

    if songs_input:  # if not empty
        songs_input_integer = int(songs_input)
        formatted_make_album = make_album(artist_name_input, album_name_input, songs_input_integer)
    else:
        formatted_make_album = make_album(artist_name_input, album_name_input)

    print(formatted_make_album)
