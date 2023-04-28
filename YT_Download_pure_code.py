from pytube import YouTube

# link do filmu na YouTube
url = "https://youtu.be/axvcdVnt0Hs"

# utworzenie obiektu YouTube z podanym linkiem
video = YouTube(url)

# pobranie pliku w najwyższej jakości
stream = video.streams.get_highest_resolution()

# pobranie pliku
stream.download()
