import sys
#import math

def circle_data (circle_file) :
    with open (circle_file, 'r') as file:
        dataLine=file.readlines()
        x,y=map(int, dataLine[0].split())
        radius=int(dataLine[1])
    return x,y,radius

def coords_data(coords_file):
    coords=[]
    with open (coords_file, 'r') as file: 
        for line in file:
            x1,y1=map(int,line.split())
            coords.append((x1,y1))
    return coords

def coords_pos(x,y,radius,x1,y1):
    distance=(x1-x)**2+(y1-y)**2
    radius_squared=radius**2
    if distance==radius_squared:
        return 0
    elif distance<radius_squared:
        return 1
    else :
        return 2

def main(circle_file, coords_file):
    center_x, center_y, radius = circle_data(circle_file)
    points = coords_data(coords_file)
    
    for point_x, point_y in points:
        position = coords_pos(center_x, center_y, radius, point_x, point_y)
        print(position)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Неверное количество аргументов")
        sys.exit(1)
    #Передаем в качестве аргументов
    circle_file = sys.argv[1]
    coords_file = sys.argv[2]
    
    main(circle_file, coords_file)