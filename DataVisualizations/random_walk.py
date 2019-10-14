from get_step import get_step

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at 0,0.
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculating all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            x_step = get_step()
            y_step = get_step()

            # Calculate the next x and y values.
            try:
                next_x = self.x_values[-1] + x_step
                next_y = self.y_values[-1] + y_step
            except TypeError:
                next_x = self.x_values[-1] + 0
                next_y = self.y_values[-1] + 0

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def __repr__(self):
        return 'hello'


a = RandomWalk()
print(a)
