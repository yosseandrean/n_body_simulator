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

    # TODO: move this to the CelestialBody
    @staticmethod
    def accelerate_due_to_gravity(first: CelestialBody, second: CelestialBody):
        force = first.mass * second.mass / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y),
            )
            reverse = -1

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1 :]:
                self.accelerate_due_to_gravity(first, second)
