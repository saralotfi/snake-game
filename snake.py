import random
import os
import time

class SnakeGame:
    def __init__(self):
        self.width = 5
        self.height = 4
        self.snake = [(2, 2)]
        self.direction = "RIGHT"
        self.food = (random.randint(1, self.height - 1), random.randint(1, self.width - 1))
        self.score = 0

    def draw(self):
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) == self.snake[0]:
                    print(" O ", end="")
                elif (y, x) in self.snake:
                    print(" () ", end="")
                elif (y, x) == self.food:
                    print(" * ", end="")
                else:
                    print(" - ", end="")
            print()
        print("Score:", self.score)

    def move(self):
        head_y, head_x = self.snake[0]
        if self.direction == "UP":
            new_head = (head_y - 1, head_x)
        elif self.direction == "DOWN":
            new_head = (head_y + 1, head_x)
        elif self.direction == "LEFT":
            new_head = (head_y, head_x - 1)
        elif self.direction == "RIGHT":
            new_head = (head_y, head_x + 1)
        return new_head

    def update(self):
        new_head = self.move()
        if (new_head[0] < 0 or new_head[0] >= self.height or
            new_head[1] < 0 or new_head[1] >= self.width or
            new_head in self.snake):
            return False

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = (random.randint(1, self.height - 1), random.randint(1, self.width - 1))
        else:
            self.snake.pop()

        return True

    def play(self):
        while True:
            self.draw()
            command = input("Move (U/D/L/R): ").upper()
            if command == "U" and self.direction != "DOWN":
                self.direction = "UP"
            elif command == "D" and self.direction != "UP":
                self.direction = "DOWN"
            elif command == "L" and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif command == "R" and self.direction != "LEFT":
                self.direction = "RIGHT"

            if not self.update():
                print("Game Over!")
                break
            time.sleep(0.2)

game = SnakeGame()
game.play()