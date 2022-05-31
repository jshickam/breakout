from breakout import *
from turtle import Screen

BRICK_WIDTH = 2
PADDLE_WIDTH = 4
SCREEN_WIDTH = 770
SCREEN_HEIGHT = 600
SCREEN_Y_OFFSET = 50 # Blank space to leave at the top of the screen
BRICK_ROWS = 8

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

brick_width = BRICK_WIDTH * 20 # Brick width in pixels
left_brick_x = int(-SCREEN_WIDTH / 2 + brick_width / 2)
right_brick_x = int(SCREEN_WIDTH /2 - brick_width / 2)
top_brick_y = int(SCREEN_HEIGHT / 2  - 10 - SCREEN_Y_OFFSET)
bottom_brick_y = int(top_brick_y - BRICK_ROWS * 20)

for j in range (top_brick_y, bottom_brick_y, -20):
    for i in range(left_brick_x, right_brick_x, brick_width):
        brick = Brick(location=(i, j), width=BRICK_WIDTH)

paddle = Paddle((0, -SCREEN_HEIGHT / 2 + 20), width=PADDLE_WIDTH)
random_x = random.randint(int(-SCREEN_WIDTH / 2 + 10), int(SCREEN_WIDTH / 2 - 10))
ball = Ball((random_x, bottom_brick_y))

# Set up button controls for paddle
screen.listen()
screen.onkeypress(lambda: paddle.on_key_press("w"), "Left")
screen.onkeypress(lambda: paddle.on_key_press("e"), "Right")
screen.onkeyrelease(paddle.on_key_release, "Left")
screen.onkeyrelease(paddle.on_key_release, "Right")

while True:
    paddle.move()
    ball.move(paddle)
    screen.update()
    
screen.exitonclick()