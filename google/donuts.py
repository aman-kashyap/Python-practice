# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'


def donuts(count):
    return
  # +++your code here+++
  # LAB(begin solution)
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

#def donuts(count):
    #count=int(input("enter Number of donuts :"))
#    if count<10:
 #
 #        return 'number of donuts:'+str(count)
 #   else:
 #       return 'Number of donuts : many'

#    return