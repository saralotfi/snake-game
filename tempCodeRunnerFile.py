import random
import os
import time
width, height = 5, 4
snake = [(2, 2)]
direction = "RIGHT"
food = (random.randint(1, height - 1), random.randint(1, width - 1))
score = 0
def draw():
    os.system("cls" if os.name == "nt" else "clear") 
    for y in range(height):
        row = " "
        for x in range(width):
            if (y, x) == snake[0]:
                row += " O "  
            elif (y, x) in snake:
                row += " () " 
            elif (y, x) == food:
                row += " * "  
            else:
                row += " - "  
        print(row)
    print(f"Score: {score}")

def update():
    global food, score 
    head_y, head_x = snake[0]
    if direction == "UP":
        new_head = (head_y - 1, head_x)
    elif direction == "DOWN":
        new_head = (head_y + 1, head_x)
    elif direction == "LEFT":
        new_head = (head_y, head_x - 1)
    elif direction == "RIGHT":
        new_head = (head_y, head_x + 1)

    if new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
        return False
    
    if new_head in snake:
        return False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (random.randint(1, height - 1), random.randint(1, width - 1))  
    else:
        snake.pop()  

    return True


try:
    while True:
        draw()
        command = input("Move (U/D/L/R): ").upper()
        if command == "U" and direction != "DOWN":
            direction = "UP"
        elif command == "D" and direction != "UP":
            direction = "DOWN"
        elif command == "L" and direction != "RIGHT":
            direction = "LEFT"
        elif command == "R" and direction != "LEFT":
            direction = "RIGHT"

        if not update():
            print("Game Over!")
            break

        time.sleep(0.2) 
except KeyboardInterrupt:
    print("\nGame interrupted!")