import random
def euclideanDistance(coordinates1, coordinates2):
    return ((coordinates1[0] - coordinates2[0])**2 + (coordinates1[1] - coordinates2[1])**2)**(1/2)

points = [(random.randint(-100,100),random.randint(-100,100)) for _ in range(10)]  

distances = []
for i in range(len(points)):
    for y in range(i+1, len(points)):
        coor1 = points[i]
        coor2 = points[y]
        distances.append(euclideanDistance(coor1, coor2))

min_distance = min(distances)  
min_distance = round(min_distance, 2)
print(f"Points : {points}")
print(f"Minimum distance: {min_distance}") 
