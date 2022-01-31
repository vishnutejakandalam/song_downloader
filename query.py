import requests
from Song import Song


def get_song_urls(song_obj):
    """Fetch song download url."""
    req = requests.get(headers=headers,
                       url=f"https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in\
        &_marker=0%3F_marker%3D0&_format=json&pids={song_obj.token}")
    raw_json = req.json()[song_obj.token]
    if 'media_preview_url' in raw_json.keys():
        song_obj.url = raw_json['media_preview_url'].\
            replace('https://preview.saavncdn.com/', 'https://aac.saavncdn.com/').\
            replace('_96_p.mp4', '_320.mp4')
        song_obj.img_url = raw_json['image'].replace(
            '-150x150.jpg', '-500x500.jpg')
    return song_obj

def write_song(title, url):
    res = requests.get(url, allow_redirects=True)
    with open(title+".mp3", 'wb') as file:
        file.write(res.content)




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;' +
    ' WOW64; rv:39.0) Gecko/20100101 Firefox/75.0',
}

def search_songs(query_text):
    """This method sends request and gets the song details. """
    req = requests.get(
        headers=headers,
        url=f"https://www.jiosaavn.com/api.php?p=1&q={query_text.replace(' ', '+')}\
            &_format=json&_marker=0&api_version=4&ctx=wap6dot0\
            &n={10}&__call=search.getResults")
    query_json = req.json()
    song_list = []
    # print(len(query_json["results"]))
    for sng_raw in query_json['results']:
        song_id = sng_raw['id']
        song_title = sng_raw['title']
        song_year = sng_raw['year']
        song_album = sng_raw['more_info']['album']
        song = Song(song_id, song_title, song_year, song_album)
        song_list.append(song)

    for i in song_list:
        i.print_all()
    return song_list

if __name__ == '__main__':
    query_text = "dheera dheera kgf"
    songs_list = search_songs(query_text)
    urls = []
    for i in songs_list:
        urls.append(get_song_urls(i))
    write_song(songs_list[0].name, songs_list[0].url)


