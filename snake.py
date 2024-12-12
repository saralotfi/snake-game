import random
import time
import curses

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.width = 10
        self.height = 8
        self.snake = [(4, 4)]
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
        self.stdscr.clear()
        for y in range(self.height):
            self.stdscr.addstr(y, 0, self.draw_row(y))
        self.stdscr.addstr(self.height, 0, f"Score: {self.score}")
        self.stdscr.refresh()

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
        while True:
            new_food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if new_food not in self.snake:
                self.food = new_food
                break

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
            key = self.stdscr.getch()
            if key == ord('m'):  
                choice = self.show_menu()
                if choice == "Exit":
                    break
            elif key == curses.KEY_UP and self.direction != "DOWN":
                self.direction = "UP"
            elif key == curses.KEY_DOWN and self.direction != "UP":
                self.direction = "DOWN"
            elif key == curses.KEY_LEFT and self.direction != "RIGHT":
                self.direction = "LEFT"
            elif key == curses.KEY_RIGHT and self.direction != "LEFT":
                self.direction = "RIGHT"

            if not self.update():
                self.stdscr.addstr(self.height + 1, 0, "Game Over!")
                self.stdscr.refresh()
                time.sleep(1)
                break
            time.sleep(0.2)

    def show_menu(self):
        menu_items = ["Continue", "Exit"]
        current_row = 0
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        while True:
            self.stdscr.clear()
            for idx, item in enumerate(menu_items):
                if idx == current_row:
                    self.stdscr.addstr(idx, 0, item, curses.color_pair(1))
                else:
                    self.stdscr.addstr(idx, 0, item)
            self.stdscr.refresh()

            key = self.stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
                current_row += 1
            elif key == 10:  
                if current_row == 0:  
                    return "Continue"
                elif current_row == 1:  
                    return "Exit"

def main(stdscr):
    game = SnakeGame(stdscr)
    game.play()

curses.wrapper(main)   