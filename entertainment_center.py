import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
"A story of a boy and his toys that come to life",
"http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
"A marine on an alien planet",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
"https://www.youtube.com/watch?v=5PSNL1qE6VY")
harry_potter = media.Movie("harry Potter",
"A story of harry son of a magician",
"http://vignette3.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest/scale-to-width-down/270?cb=20101208171110",
"https://www.youtube.com/watch?v=ACNzq06azSw")
the_avengers = media.Movie("The Avengers",
"The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team",
"http://blogs-images.forbes.com/larissafaw/files/2012/04/Marvels-The-Avengers.jpg",
"https://www.youtube.com/watch?v=NPoHPNeU9fc")
iron_man = media.Movie("Iron Man 3",
"Iron Man 3 (stylized onscreen as Iron Man Three) is a 2013 American[4] superhero film featuring the Marvel Comics character Iron Man.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_UY1200_CR105,0,630,1200_AL_.jpg",
"https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
the_dark_knight = media.Movie("The Dark Knight",
"A gang of criminals rob a Gotham City mob bank, double-crossing and murdering each other until there is only one left: The Joker, who escapes with the money.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=EXeTwQWrcwY")
#the Movie instances are being added to the movies list here.
movies = {toy_story,avatar,harry_potter,the_avengers,iron_man,the_dark_knight}
fresh_tomatoes.open_movies_page(movies)
