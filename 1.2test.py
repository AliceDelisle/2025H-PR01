import random
BALL_SPEED_X = 5
BALL_SPEED_Y = 5


def random_in_range(min_value, max_value):
    return min_value + (max_value - min_value) * random.random()
ball_velocity_x = random_in_range(-BALL_SPEED_X, BALL_SPEED_X)
ball_velocity_y = random_in_range(-BALL_SPEED_Y, BALL_SPEED_Y)
