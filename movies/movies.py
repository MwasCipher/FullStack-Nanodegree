from imdb import IMDb


class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_url = movie_poster
        self.youtube_trailer_url = movie_trailer

        # https://www.youtube.com/watch?v=S8obCz5NSog





# # create an instance of the IMDb class
# ia = IMDb()
#
# # get a movie
# movie = ia.get_movie('0133093')
#
# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])
#
# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)
#
# # search for a person name
# people = ia.search_person('Mel Gibson')
# for person in people:
#    print(person.personID, person['name'])