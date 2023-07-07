class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, maze):
        # Move the player to the given coordinates if it's not a wall.
        if not maze.is_wall(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
