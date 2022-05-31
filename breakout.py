from turtle import Turtle, Screen, pendown, penup, width
import random


class Brick(Turtle):
    def __init__(self, location:tuple, width:int) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.width = width
        self.location = location
        self.draw()
        self.set_color()

    def set_color(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        color = random.choice(colors)
        self.color(color)
        self.pencolor("black")
        self.fillcolor(color)

    def draw(self):
        x, y = self.location
        self.goto(self.location)
        self.shapesize(stretch_len=self.width, outline=5)
        

class Paddle(Turtle):
    def __init__(self, location:tuple, width:int) -> None:
        super().__init__()  
        self.penup() 
        self.location = location    
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=width)
        self.goto(self.location)
        self.moving = False
        self.direction = "w"
        self.width = width

    def on_key_press(self, direction):
        self.direction = direction
        self.moving = True

    def on_key_release(self):
        self.moving = False

    def move(self):
        """Moves the paddle left or right
        direction: string object 'w' for left, 'e' for right"""
        # Stop the paddle when it reaches the edge of the screen
        if self.direction == "e":
            upper_bound = self.getscreen().window_width() / 2 - self.width * 14
            if self.xcor() >= upper_bound:
                self.moving = False
            else:
                self.setheading(0)
        elif self.direction == "w":
            lower_bound = -(self.getscreen().window_width() / 2 - self.width * 12)
            if self.xcor() <= lower_bound:
                self.moving = False
            else:
                self.setheading(180)
        # Move the paddle if not at the edge of the screen.
        if self.moving:
            self.forward(10)
            
    def stop(self):
        self.moving = False

class Ball(Turtle):
    def __init__(self, location:tuple) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(location)
        self.setheading(random.randint(200, 340))
        self.screen = self.getscreen()

    def wall_hit(self):
        # Check if ball has struck the wall
        boundary = self.screen.window_width() / 2 - 10
        if abs(self.xcor()) >= boundary:
            return True
        return False
    
    def paddle_hit(self, paddle:Paddle):
        x, y = self.position()
        boundary_y = paddle.ycor() + 20
        if self.ycor() <= boundary_y:
            if self.xcor() >= paddle.xcor() - paddle.width * 20 / 2:
                if self.xcor() <= paddle.xcor() + paddle.width * 20 / 2:
                    return True
        return False

    def move(self, paddle):
        if self.wall_hit():
            self.setheading(180 + (360 - self.heading()))
        if self.paddle_hit(paddle):
            self.setheading(90 - (self.heading() - 270))
        self.forward(5)

    