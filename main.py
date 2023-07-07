import maze
import player

def main():
    # Create a maze.
    my_maze = maze.Maze(20, 10)  # smaller maze for testing
    difficulty = 0.0  # Starting difficulty level
    my_maze.generate(difficulty)

    # Create a player.
    my_player = player.Player(0, 0)

    # Start the game loop.
    while True:
        # Draw the maze.
        for row in my_maze.walls:
            print(''.join(row))

        # Draw the player.
        print(f'Player is at ({my_player.x}, {my_player.y})')

        # Get the player's input.
        action = input("Move (up/down/left/right/quit): ")

        if action == "quit":
            print("Quitting the game. Goodbye!")
            break

        # Move the player.
        if action == "up" and my_maze.walls[my_player.y*2+1][my_player.x*2+2] != 'W':
            my_maze.move_player(my_player, 0, -1)
        elif action == "down" and my_maze.walls[my_player.y*2+3][my_player.x*2+2] != 'W':
            my_maze.move_player(my_player, 0, 1)
        elif action == "left" and my_maze.walls[my_player.y*2+2][my_player.x*2+1] != 'W':
            my_maze.move_player(my_player, -1, 0)
        elif action == "right" and my_maze.walls[my_player.y*2+2][my_player.x*2+3] != 'W':
            my_maze.move_player(my_player, 1, 0)

        # Check if the player has reached the exit.
        if (my_player.x, my_player.y) == my_maze.exit:
            print("You win!")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thank you for playing!")
                break
            difficulty += 0.1  # Increase difficulty
            if difficulty > 1.0:  # Keep difficulty within [0.0, 1.0]
                difficulty = 1.0
            my_maze = maze.Maze(20, 10)  # Create a new maze
            my_maze.generate(difficulty)  # Generate the new maze with the new difficulty
            my_player = player.Player(0, 0)  # Reset player position

if __name__ == "__main__":
    main()
