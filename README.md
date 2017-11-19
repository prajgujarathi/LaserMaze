# LaserMaze

This application builds and solves a simple "laser maze". A laser maze is a grid of squares, with a single solution. The player has a starting position from which he fires a laser in a specific direction (north, south, east, or west). The laser beam travels through the grid one square at a time. As square can be one of the following different 'states':

### Player starting position
	* This is the square where the maze begins
	* A beam will pass through a square in this state as if it were empty
### Empty
	* The laser beam passes through an empty square in the same direction as it entered
### Mirror
	* Changes the direction of the laser beam. For instance, a mirror represented by “\” would change a beam traveling east to a beam traveling south. A mirror represented by “/” would change a beam traveling north to traveling east.
	
'Solving' the maze means letting the laser beam travel through the grid until it hits a wall, or gets stuck in a loop.

## Running the application

The command line application can be run as follows:

```python
$ python maze.py input_data/inputmaze.txt output_data/outputmaze.txt
```

The output file will be in the following format:

```
9    # number of squares traversed, -1 if a wall is never hit
0 0  # coordinate of the final square (unnecessary if a wall is never hit
```

## Running the tests

For running the test, please run the following command:

```python
$ python maze_test.py
```

## Author

- **Prajakta Gujarathi** [LinkedIn](https://www.linkedin.com/in/prajakta-gujarathi/)

## Licence

LaserMaze is available under the MIT License. See the `LICENSE` file for more info.
