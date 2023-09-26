from bs4 import BeautifulSoup
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
response = response.text
soup = BeautifulSoup(response, "html.parser")
movie_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
with open("movie_lis.txt", mode="w", encoding="utf-8") as file:
    for mov in movie_list[::-1]:
        file.write(mov+"\n")
