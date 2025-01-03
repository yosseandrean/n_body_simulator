import math
import turtle
from typing import List


class CelestialBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0),
        velocity=(0, 0),
        color="red",
    ):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.color(color)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.penup()
        self.hideturtle()
        solar_system.add_body(self)

    def draw(self):
        self.clear()  # Clear the existing drawing before drawing.
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

    def accelerate_due_to_gravity(self, body) -> None:
        force = self.mass * body.mass / self.distance(body) ** 2
        angle = self.towards(body)
        acceleration = force / self.mass

        acc_x = acceleration * math.cos(math.radians(angle))
        acc_y = acceleration * math.sin(math.radians(angle))

        # Update the velocity
        self.velocity = (
            self.velocity[0] + acc_x,
            self.velocity[1] + acc_y,
        )


class SolarSystem:

    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        self.bodies: List[CelestialBody] = []

    def add_body(self, body: CelestialBody):
        self.bodies.append(body)

    def remove_body(self, body: CelestialBody):
        self.bodies.remove(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    def calculate_all_body_interactions(self):
        for first in self.bodies:
            for second in self.bodies:
                if first is second:
                    continue
                first.accelerate_due_to_gravity(second)
