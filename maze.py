import numpy as np
import argparse
import sys
import os

class maze_laser:
    def __init__(self, grid_width, grid_height, start_x, start_y, mirror_list=None):
        self.maze = np.zeros((grid_height, grid_width), dtype=str)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.start_coordinates =(start_x, start_y)
        if mirror_list != None:
            for mirror in mirror_list:
                y = grid_height - int(mirror[1]) - 1
                self.maze[int(y)][int(mirror[0])] = mirror[2]
        self.visited = []

    def check_loop(self, x, y, direction):
        # Check for existence of loop in laser travers path

        if (x, y, direction) not in self.visited :
            self.visited.append((x, y, direction))
            return False
        return True

    def laser(self, x, y, direction, tile = 1):

        if self.check_loop(x, y, direction):
            return -1, " ", " "

        else:
            # South direction
            if direction.upper() == 'S':
                if self.start_coordinates == (x, y) and x + 1 <= self.grid_height:
                    if tile != 1:
                        return self.laser(x + 1, y, 'S', tile + 1)
                    else:
                        return self.laser(x + 1, y, 'S')
                elif x >= self.grid_height - 1 and self.maze[x][y] == '':
                    return tile, get_quadrant1_coordinates(self.grid_height, x), y
                elif self.maze[x][y] == '':
                    tile += 1
                    return self.laser(x + 1, y, 'S',tile)
                elif self.maze[x][y] == '/':
                    tile += 1
                    return self.laser(x, y - 1, 'W', tile)
                elif self.maze[x][y] == '\\':
                    tile += 1
                    return self.laser(x, y + 1, 'E', tile)

            # East direction
            elif direction.upper() == 'E':
                if self.start_coordinates == (x, y) and y + 1 <= self.grid_width:
                    if tile == 1 : return self.laser(x, y + 1, 'E')
                    return self.laser(x, y + 1, 'E', tile + 1)
                elif y >= self.grid_width - 1 and self.maze[x][y] == '':
                    return tile, get_quadrant1_coordinates(self.grid_height, x), y
                elif self.maze[x][y] == '':
                    tile += 1
                    return self.laser(x, y + 1, 'E', tile)
                elif self.maze[x][y] == '/':
                    tile += 1
                    return self.laser(x - 1, y, 'N', tile)
                elif self.maze[x][y] == '\\':
                    tile += 1
                    return self.laser(x + 1, y, 'S', tile)

            # West direction
            elif direction.upper() == 'W':
                if self.start_coordinates == (x, y) and y - 1 >= 0 :
                    if tile == 1 :return self.laser(x, y - 1, 'W')
                    return self.laser(x, y - 1, 'W', tile + 1)
                elif y <= 0 and self.maze[x][y] == '':
                    return tile, get_quadrant1_coordinates(self.grid_height, x), y
                elif self.maze[x][y] == '':
                    tile += 1
                    return self.laser(x, y - 1, 'W', tile)
                elif self.maze[x][y] == '/':
                    tile += 1
                    return self.laser(x + 1, y, 'S', tile)
                elif self.maze[x][y] == '\\':
                    tile += 1
                    return self.laser(x - 1, y ,'N', tile)

            # North direction
            elif direction.upper() == 'N':
                if self.start_coordinates == (x, y) and x - 1 >= 0:
                    if tile == 1 : return self.laser(x - 1, y, 'N')
                    return self.laser(x - 1, y, 'N', tile + 1)
                elif x <= 0 and self.maze[x][y] == '':
                    return tile, get_quadrant1_coordinates(self.grid_height, x), y
                elif self.maze[x][y] == '':
                    tile += 1
                    return self.laser(x - 1, y, 'N', tile)
                elif self.maze[x][y] == '/':
                    tile += 1
                    return self.laser(x, y + 1, 'E', tile)
                elif self.maze[x][y] == '\\':
                    tile += 1
                    return self.laser(x, y - 1, 'W', tile)

            return tile, get_quadrant1_coordinates(self.grid_height, x), y


def create_arg_parser():
    parser = argparse.ArgumentParser(description = 'Welcome to Maze Laser')
    parser.add_argument('inputDirectory', help = 'Path to the input directory.')
    parser.add_argument('outputDirectory', help = 'Path to the output that contains the resumes.')
    return parser


def get_quadrant1_coordinates(grid_height, y):
    # Converting 4th quadrant to 1st.
    y = grid_height - 1 - y
    return y

if __name__ == '__main__':
    # Parse input output directories.
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    input_file = open(parsed_args.inputDirectory,'r')
    mirror_list = []
    array = []

    # Read file to get grid parameters, start point and mirror list.
    for line in input_file:
        array.append(line.rstrip('\n'))
    grid_param = map(int, array[0].split())
    start_point = array[1].split()
    for mirror in array[2:]:
        mirror_list.append(mirror.split())

    # Convert a maze into 1st quadrant.
    y_coordinate= get_quadrant1_coordinates(grid_param[1],int(start_point[1]))
    x_coordinate = int(start_point[0])
    m1 = maze_laser(grid_param[0], grid_param[1], y_coordinate, x_coordinate, mirror_list)

    # Start traversal from start point
    tile, x, y = m1.laser(int(y_coordinate),int(start_point[0]),start_point[2])

    # Check output directory exits, if not create one.
    output_dir, output_file = os.path.split(parsed_args.outputDirectory)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Print output to output directory.
    with open(parsed_args.outputDirectory, 'w') as f:
        f.write(str(tile))
        if tile != -1: f.write('\n'+str(y)+" "+str(x))
