from turtle import width
from breakout import Ball, Brick

class BrickManager():
    def __init__(self, brick_width, screen_width, screen_height, screen_y_offset, brick_rows):
        self.rows = brick_rows
        self.brick_width = brick_width * 20 # Brick width in pixels
        self.left_brick_x = int(-screen_width / 2 + self.brick_width / 2)
        self.right_brick_x = int(screen_width /2 - self.brick_width / 2)
        self.top_brick_y = int(screen_height / 2  - 10 - screen_y_offset)
        self.bottom_brick_y = int(self.top_brick_y - brick_rows * 20)
        self.bricks = []

    def draw_screen(self):
        for j in range (self.top_brick_y, self.bottom_brick_y, -20):
            for i in range(self.left_brick_x, self.right_brick_x, self.brick_width):
                self.bricks.append(Brick(location=(i, j), width=self.brick_width/20))
        self.columns = int(len(self.bricks) / self.rows)      

    def check_collision(self, ball:Ball):
        """Checks whether the ball collided with any brick(s) and changes heading"""
        heading = ball.heading()
        
        # Check for colision from right
        if ball.heading > 90 and ball.heading < 270:
            pass


        # Check for collision from bottom
        if heading < 180: #ball direction is upward
            start = self.top_brick_y - 10 # bottom y coord of top row
            for i in range (0, self.rows): # Collides with row?
                if int(ball.ycor()) + 15 == self.bottom_brick_y + 20 * i:
                    row = self.rows - i
                    for brick in self.bricks[row * self.columns:row * self.columns + self.columns]:
                        if ball.xcor() < brick.xcor() + self.brick_width / 2 and ball.xcor() > brick.xcor() - self.brick_width / 2:
                            if brick.isvisible()
                                brick.hideturtle()
                                ball.setheading(360 - ball.heading())


       
        