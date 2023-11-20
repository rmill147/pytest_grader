# CS4412 : Data Mining
# Summer 2023
# Kennesaw State University
# Homework 1

# module for reading csv files
import csv

print("NAME -> JOE")

def read_csv_file(filename):
    """this function reads a .CSV file, and returns the dataset as a list"""
    with open(filename,'r',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=',', quotechar='"')
        dataset = [ line for line in reader ]
    return dataset

# read the datasets from file
movie_data = read_csv_file("./data/movies.csv")
rating_data = read_csv_file("./data/ratings.csv")

# skip the headers in the datasets
movie_data = movie_data[1:]
rating_data = rating_data[1:]

# produce a map from movie_id to the movie's title
def get_movie_titles(movie_data):
    movie_titles = dict()
    for movie in movie_data:
        # each line in the dataset has an ID, title, and list of genre's
        movie_id,title,genres = movie
        movie_titles[movie_id] = title

    return movie_titles

movie_titles = get_movie_titles(movie_data)

def get_movie_genres(movie_data):
    # produce a map from movie_id to the movie's genres
    movie_genres = dict()
    for movie in movie_data:
        movie_id,title,genres = movie
        # the list of genre is seperated by a | character
        genres = genres.split('|')
        movie_genres[movie_id] = genres

    return movie_genres

movie_genres = get_movie_genres(movie_data)

# next, we compute the average rating for each movie
# first, initialize counts and sums
counts = dict()  # number of ratings
sums = dict()    # sum of all ratings
for rating in rating_data:
    # each line in the dataset has a user-ID, movie-ID, score, and timestamp
    user_id,movie_id,score,timestamp = rating
    counts[movie_id] = 0
    sums[movie_id] = 0

# count and sum the ratings for each movie
for rating in rating_data:
    user_id,movie_id,score,timestamp = rating
    # in the dataset, all fields are strings, so convert the score to
    # a floating-point number first when we compute the average rating
    score = float(score)
    counts[movie_id] += 1
    sums[movie_id] += score

stats = dict()
min_ratings = 100
genre = "Action"

# FUNCTION 0 - EXAMPLE THAT RETURNS LIST OF TOP 10 COMEDY MOVIES
def topComedy(counts, sums, movie_genres,q0_genre):
    # move code here
    genre = q0_genre
    # compute the averages from the counts and sums

    for movie_id in counts:
        if counts[movie_id] < min_ratings: continue
        if genre not in movie_genres[movie_id]: continue
        average = sums[movie_id] / counts[movie_id]
        # each stat entry has the movie id, the average rating, and #-of-ratings
        stats[movie_id] = (movie_id, average, counts[movie_id])

    # sort the list of ratings
    key_function = lambda x: x[1]  # given x, return x[1]
    ranking = list(stats.values())
    ranking.sort(key=key_function, reverse=True)

    question0 = list()

    for line in ranking[:10]:
        # each stat entry has the movie id, the average rating, and #-of-ratings
        movie_id, average, count = line
        movie_title = movie_titles[movie_id]
        question0.append((movie_title,average,count))

    # return a list that contains answer
    return question0

#Print output for example
print("Q0: top 10 comedy movies with at least 100 ratings:")
part0 = topComedy(counts, sums, movie_genres, genre)
i = 1
for element in part0:
    print("%i: %s: %f stars with %i reviews" % (i, element[0],element[1],element[2]))
    i = i + 1

# QUESTION 1 - WHICH MOVIE HAS HIGHEST AVERAGE RATING MYSYERY GENRE AND HAS 100+ RATINGS
# Joe gets question 1 wrong
print("============================================")
print("== QUESTION 1 - WHICH MOVIE HAS HIGHEST AVERAGE RATING MYSTERY GENRE AND HAS 100+ RATINGS")
print("============================================")

def topMystery(counts, sums, movie_genres,genre):
    min_ratings = 80 #should be 100
    # compute the averages from the counts and sums
    for movie_id in counts:
        if counts[movie_id] < min_ratings: continue
        if genre not in movie_genres[movie_id]: continue
        average = sums[movie_id] / counts[movie_id]
        # each stat entry has the movie id, the average rating, and #-of-ratings
        stats[movie_id] = (movie_id, average, counts[movie_id])

    # sort the list of ratings
    key_function = lambda x: x[1]  # given x, return x[1]
    ranking = list(stats.values())
    ranking.sort(key=key_function, reverse=True)

    question1 = list()

    for line in ranking[:1]:
        # each stat entry has the movie id, the average rating, and #-of-ratings
        movie_id, average, count = line
        movie_title = movie_titles[movie_id]
        question1.append((movie_title, average, count))

    # return a list that contains answer
    return question1

#Print output for example
print("Q1: top Mystery movies with at least 100 ratings:")
part1 = topMystery(counts, sums, movie_genres, "Mystery")
print(part1)
for element in part1:
    print("%s: %f stars with %i reviews" % (element[0],element[1],element[2]))

# QUESTION 2 - WHICH MOVIE HAS HIGHEST AVERAGE RATING MYSTERY GENRE AND HAS 100+ RATINGS
print("============================================")
print("== QUESTION 2 - WHICH MOVIE HAS LOWEST AVERAGE RATING ACTION GENRE AND HAS 100+ RATINGS")
print("============================================")

def lowAction(counts, sums, movie_genres,genre):
    min_ratings = 100
    # compute the averages from the counts and sums
    for movie_id in counts:
        if counts[movie_id] < min_ratings: continue
        if genre not in movie_genres[movie_id]: continue
        average = sums[movie_id] / counts[movie_id]
        # each stat entry has the movie id, the average rating, and #-of-ratings
        stats[movie_id] = (movie_id, average, counts[movie_id])

    # sort the list of ratings
    key_function = lambda x: x[1]  # given x, return x[1]
    ranking = list(stats.values())
    ranking.sort(key=key_function, reverse=False)

    question2 = list()
    for line in ranking[:1]:
        # each stat entry has the movie id, the average rating, and #-of-ratings
        movie_id, average, count = line
        movie_title = movie_titles[movie_id]
        question2.append((movie_title, average, count))

    # return a list that contains answer
    return question2

#Print output for example
print("Q2: Bottom action movie with at least 100 ratings:")
part2 = lowAction(counts, sums, movie_genres, "Action")

for element in part2:
    print("%s: %f stars with %i reviews" % (element[0],element[1],element[2]))

# QUESTION 3 - FOR USERS WHO RATED  “Star Wars: Episode IV - A New Hope (1977)” 5.0, WHAT OTHER MOVIES DID THESE
# USERS RATE HIGHLY (MOVIE MUST HAVE 10+ REVIEWS FROM THESE USERS)
print("============================================")
print("== QUESTION 3 - RECOMMENDATIONS FOR STAR WARS FANS")
print("============================================")

def starWarsRecs(counts, sums, movie_genres,genre):

    #Make a set of the users we're looking at; people that rated movie 260 a score of 5.0
    wanted_users = set()
    for rating in rating_data:
        user_id,movie_id,score,timestamp = rating
        if movie_id == "260" and score == "5.0":
            wanted_users.add(user_id)

    #make a list of wanted ratings; iterate through ratings in rating_data, if the user ID was selected above add it to the list
    wanted_ratings = list()
    for rating in rating_data:
        user_id,movie_id,score,timestamp = rating
        if user_id in wanted_users:
            wanted_ratings.append(rating)

    counts = dict()  # number of ratings
    sums = dict()    # sum of all ratings

    #iterate through list of wanted ratings
    for rating in wanted_ratings:
        user_id,movie_id,score,timestamp = rating #all of the items on the left will be stored at rating in wanted ratings[i]
        counts[movie_id] = 0
        sums[movie_id] = 0

    # count and sum the ratings for each movie
    for rating in wanted_ratings:
        user_id,movie_id,score,timestamp = rating
        counts[movie_id] += 1
        sums[movie_id] += float(score)

    # compute the averages from the counts and sums
    stats = dict()
    min_ratings = 10
    for movie_id in counts:
        if counts[movie_id] < min_ratings: continue
        average = sums[movie_id]/counts[movie_id]
        # each stat entry has the movie id, the average rating, and #-of-ratings
        stats[movie_id] = (movie_id,average,counts[movie_id])

    # sort the list of ratings
    key_function = lambda x: x[1] # given x, return x[1]
    ranking = list(stats.values())
    ranking.sort(key=key_function,reverse=True)

    # print the top-10 movies
    question3 = list()

    for line in ranking[:10]:
        # each stat entry has the movie id, the average rating, and #-of-ratings
        movie_id, average, count = line
        movie_title = movie_titles[movie_id]
        question3.append((movie_title, average, count))

    # return a list that contains answer
    return question3

#Print output
print("Q3: top 10 reccommendations for Star Wars fans with at least 100 ratings:")
part3 = starWarsRecs(counts, sums, movie_genres, genre)
print(part3)
i = 1
#for element in part3:
 #   print("%i: %s: %f stars with %i reviews" % (i, element[0],element[1],element[2]))
  #  i = i + 1