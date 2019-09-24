from matplotlib import pyplot




##Bar Charts
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

##Label X-axis with [0-4]
pyplot.bar(range(len(movies)), num_oscars)

pyplot.title("My Favorite Movies")     # add a title
pyplot.ylabel("# of Academy Awards")   # label the y-axis

## label X-axis
pyplot.xticks(range(len(movies)), movies)

pyplot.show()