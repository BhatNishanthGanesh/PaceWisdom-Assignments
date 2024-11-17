# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]


def getcoordinates():
    input_str = input("Enter the list of coordinates (e.g., [(1,-2), (-2, 4), (-1,-1)]): ")
    coordinates = eval(input_str)
    return coordinates

def main():
    coordinates = getcoordinates()
    x_coords = [x for x, y in coordinates]
    y_coords = [y for x, y in coordinates]

    min_x = min(x_coords)
    min_y = min(y_coords)

    shift_x = abs(min_x) if min_x < 0 else 0
    shift_y = abs(min_y) if min_y < 0 else 0

    shifted_coordinates = [(x+shift_x, y+shift_y)for x,y in coordinates]
    
    print(shifted_coordinates)

if __name__ == "__main__":
    main()            
    


