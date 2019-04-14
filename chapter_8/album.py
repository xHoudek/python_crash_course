def make_album(artist_name, album_title, track_number = ''):
    info = {'Artist': artist_name, 'Album': album_title}
    if track_number:
        info['Number of tracks:'] = track_number
    return info


animals = make_album('Pink Floyd', 'Animals', '5')
print(animals)

mmfood = make_album('MF Doom', 'Mm.. Food', '15')
print(mmfood)

tpab = make_album('Kendrick Lamar', 'To Pimp a Butterfly')
print(tpab)

print()


while True:
    print("Enter 'q' at any time to quit")
    artist = input('Enter artist name: ')
    if artist.lower() == 'q':
        break

    album = input('Enter album name: ')
    if album.lower() == 'q':
        break

    result = make_album(artist, album)
    print(result)