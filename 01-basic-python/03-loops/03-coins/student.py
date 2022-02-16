# Write your code here
def coins(one,two,five,goal):

    for x in range(0, one):

        for y in range(0,two):

            for z in range(0,five):

                if (x)+(2*y)+(5*z) == goal:
                    return True

                    
    return False