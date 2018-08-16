# Import useful libraries
from statistics import mean


def terrain():

    # Initialise corner values
    set_corners(height_map)

    diamond_square(size)



def set_corners(height_map):

    size = len(height_map)
    height_map[0][0] = 5.0
    height_map[0][size-1] = 5.0
    height_map[size-1][0] = 5.0
    height_map[size-1][size-1] = 5.0

    return


def print_height_map(height_map):
    if height_map:
        for row in height_map:
            print("[ ", end='')
            for num in row:
                print("{:6.2f} ".format(num), end='')
            print("]")

    return


def diamond_square(size):
    """Recursive implementation of 'Diamond-square algorithm'"""

    print("\n================ NEW RECURSIVE CALL ================\n")

    size = int(size)
    half = int(size / 2)
    max_height = 4 #size - 1

    print("SIZE = {0} HALF = {1} MAX = {2}".format(size, half, max_height))

    if half < 1:
        return

    print("\n-----STARTING DIAMOND STEP------\n")
    # Perform 'diamond' steps
    for y in range(half, max_height, size):
        for x in range(half, max_height, size):
            print("(x,y) = ({0},{1})".format(x,y))
            diamond(x, y, half, 4.0)


    print_height_map(height_map)

    print("\n-----STARTING SQUARE STEP------\n")
    # Perform 'square' steps
    for y in range(0, max_height + 1, half):
        for x in range((y + half) % max_height, max_height + 1, max_height):
            print("(x,y) = ({0},{1})".format(x,y))
            square(x, y, half, 4.0)


    print_height_map(height_map)

    # Recurse
    diamond_square(size / 2)



def diamond(x, y, size, offset):

    # Get the average height values of 4 corners of the 'square'
    print(x-size, y-size)
    print(x+size, y-size)
    print(x-size, y+size)
    print(x+size, y+size)

    a = get_value(x-size, y-size)
    b = get_value(x+size, y-size)
    c = get_value(x-size, y+size)
    d = get_value(x+size, y+size)

    avg = mean([a, b, c, d])

    # Set new value for midpoint of 'square'
    height_map[x][y] = avg + offset

    return


def square(x, y, size, offset):

    print(x, y-size)
    print(x, y+size)
    print(x-size, y)
    print(x+size, y)

    # Get the average height values of 4 corners of the 'diamond'
    a = get_value(x, y-size) # height_map[x][y-size]
    b = get_value(x, y+size) # height_map[x][y+size]
    c = get_value(x-size, y) # height_map[x-size][y]
    d = get_value(x+size, y) # height_map[x+size][y]

    avg = mean([a, b, c, d])

    # Set new value for midpoint of 'diamond'
    height_map[x][y] = avg + 3.0

    return


def get_value(x, y):
    """Returns a value from the 'height_map' array
    if both 'x' and 'y' are valid, otherwise returns zero"""

    # If array indices are out of bound, return zero
    if x < 0 or x >= size or y < 0 or y >= size:
        return False

    # Otherwise, return true value
    return height_map[x][y]


###############################################################################
### GLOBAL VARIABLES XD

# Enter 'n', i.e. the level of detail
n = int(input("Please enter n: "))

# Define parameters of height map
size = (2 ** n) + 1
height_map = [[0.0] * size for n in range(size)]


# Driver function
def main():
    terrain()
    print_height_map(height_map)

    



if __name__ == '__main__':
    main()