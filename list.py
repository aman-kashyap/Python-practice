movie_list=[ 'j', 'k', 'm',  ]
print('the first item is', movie_list[1])

movie_list[0]="h"
print(movie_list)
print(movie_list[1:3])

other_events =['Buy ticket','shopping','driving','visit']

my_list=[other_events, movie_list]
mylist1=other_events+movie_list

print(my_list)
print(mylist1)

print(my_list[1][1])

movie_list.append('f')
print(movie_list)
movie_list.insert(1,"D")

#movie_list.remove("2 st")
#print(movie_list.pop())
print(movie_list.pop(3))
del movie_list[2]

movie_list.sort()
print(movie_list)

movie_list.sort(reverse=1)
print(movie_list)

del movie_list[2]
print("After delete",my_list)

my_list = other_events+movie_list
print(my_list)

print(len(my_list))


print(max(my_list))

print(min(my_list))

