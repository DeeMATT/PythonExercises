from random import choice

def get_step():
    """Calculating the direction and distance for each random step."""

    # Decide which direction to go and how far to go in that direction.
    direction = choice([1, -1])
    distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    step = direction * distance

    # Reject moves that go nowhere.
    if step == 0:
        get_step()
    else:
        return step

