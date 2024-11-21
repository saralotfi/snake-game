import random
import os
import time

class SnakeGame:
    def __init__(self):
        self.width = 5
        self.height = 4
        self.snake = [(2, 2)]
        self.direction = "RIGHT"
        self.food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
        self.score = 0

    def draw_cell(self, y, x):
        if (y, x) == self.snake[0]:
            return " O "
        elif (y, x) in self.snake:
            return " () "
        elif (y, x) == self.food:
            return " * "
        else:
            return " - "

    def draw_row(self, y):
        return "".join(self.draw_cell(y, x) for x in range(self.width))

    def draw(self):
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(self.height):
            print(self.draw_row(y))
        print(f"Score: {self.score}")

    def move(self):
        head_y, head_x = self.snake[0]
        if self.direction == "UP":
            return (head_y - 1, head_x)
        elif self.direction == "DOWN":
            return (head_y + 1, head_x)
        elif self.direction == "LEFT":
            return (head_y, head_x - 1)
        elif self.direction == "RIGHT":
            return (head_y, head_x + 1)

    def is_invalid_move(self):
        head_y, head_x = self.move()
        return (
            head_y < 0 or head_y >= self.height or 
            head_x < 0 or head_x >= self.width or 
            (head_y, head_x) in self.snake
        )

    def handle_food_collision(self):
        if self.snake[0] == self.food:
            self.score += 1
            self.spawn_food()
            return True
        return False

    def spawn_food(self):
        self.food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))

    def move_snake(self):
        new_head = self.move()
        self.snake.insert(0, new_head)
        if not self.handle_food_collision():
            self.snake.pop()

    def update(self):
        if self.is_invalid_move():
            return False
        self.move_snake()
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



