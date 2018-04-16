movie=("k",2,"v","2")
movie2="s","a","j"
a=()
a=(10)
print(type(a))
b=(10,)
print(type(b))
print(movie)
print(movie2)

print(movie[1:3])
print(movie[-2:])
print(movie[0:4:2])

movie_concate=(movie + movie2)
print(movie_concate)

movie_repeat = movie*3
print(movie_repeat)

print("hello "*3)