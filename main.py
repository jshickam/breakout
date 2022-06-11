from breakout import *
from turtle import Screen
from brick_manager import BrickManager

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

brick_manager = BrickManager(
    brick_width=BRICK_WIDTH, 
    screen_width=SCREEN_WIDTH, 
    screen_height=SCREEN_HEIGHT,
    brick_rows=BRICK_ROWS,
    screen_y_offset=SCREEN_Y_OFFSET
    )
brick_manager.draw_screen()
paddle = Paddle((0, -SCREEN_HEIGHT / 2 + 20), width=PADDLE_WIDTH)
random_x = random.randint(int(-SCREEN_WIDTH / 2 + 10), int(SCREEN_WIDTH / 2 - 10))
ball = Ball((random_x, brick_manager.bottom_brick_y))

# Set up button controls for paddle
screen.listen()
screen.onkeypress(lambda: paddle.on_key_press("w"), "Left")
screen.onkeypress(lambda: paddle.on_key_press("e"), "Right")
screen.onkeyrelease(paddle.on_key_release, "Left")
screen.onkeyrelease(paddle.on_key_release, "Right")

while True:
    paddle.move()
    ball.move(paddle)
    # Check for brick collision if in brick range
    if ball.ycor >= brick_manager.bottom_brick_y:
        brick_manager.check_collision(ball)
    screen.update()
    
screen.exitonclick()