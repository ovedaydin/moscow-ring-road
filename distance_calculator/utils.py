import haversine as hs

#Got these corners from Yandex API
#It is not ideal to make a request everytime for a dataset we need often so we have them here
#Corners of Moscow Ring Road
lowerCorner = [37.368775, 55.571826]
upperCorner = [37.843427, 55.911123]

def distance(point):
    #We're checking if by anychance this point is in moscow ring road
    #Is the first value between 37.368775 and 37.843427
    #Is the second value between 55.571826 and 55.911123
    if upperCorner[0] >= point[0] >= lowerCorner[0] and upperCorner[1] >= point[1] >= lowerCorner[1]:
        #If it is in return "you are inside"
        return "you are inside"
    #If not we should calculate
    #Here we're finding the closest corner points
    #for the first value of the point
    #if 37.368775 - first value is bigger than 37.843427 - first value, we pick 37.843427 because it closer
    #if not, we pick 37.368775 bc it closer
    #We do the same thing for the second values
    loc = (upperCorner[0] if lowerCorner[0]-point[0] > upperCorner[0]-point[0] else lowerCorner[0], upperCorner[1] if lowerCorner[1]-point[1] > upperCorner[1]-point[1] else lowerCorner[1])
    #using haversine library we can easily calculate the distance
    #then we turn it into a integer
    #then returning a string add " km" to display this on the page
    return str(int(hs.haversine(loc,point))) + " km"
