import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = [['W'] * (width * 2 + 1) for _ in range(height * 2 + 1)]
        self.rooms = []
        self.exit = (width - 1, height - 1)

    def generate(self, difficulty=1.0):
        # Generate a random maze.
        for x in range(self.width):
            for y in range(self.height):
                if random.uniform(0, 1) > difficulty:
                    self.walls[y*2+1][x*2+1] = ' '

    def draw(self, player):
        for y, row in enumerate(self.walls):
            for x, cell in enumerate(row):
                if (x // 2, y // 2) == (player.x, player.y):
                    print('P', end='')
                else:
                    print(cell, end='')
            print()

    def is_wall(self, x, y):
        return self.walls[y*2+1][x*2+1] == 'W'

    def move_player(self, player, action):
        dx, dy = 0, 0
        if action == "up":
            dx, dy = 0, -1
        elif action == "down":
            dx, dy = 0, 1
        elif action == "left":
            dx, dy = -1, 0
        elif action == "right":
            dx, dy = 1, 0

        new_x, new_y = player.x + dx, player.y + dy
        # Move the player to the given coordinates if it's not a wall.
        if not self.is_wall(new_x, new_y):
            player.x = new_x
            player.y = new_y