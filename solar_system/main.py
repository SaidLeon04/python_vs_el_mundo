from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle
from pyglet.graphics import Batch
from pyglet import clock
import math


def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Solar System")
        self.batch = Batch()
        self.sun = Circle(320, 320, 25, color=hex_to_rgb("#ffcc00"), batch=self.batch)
        self.planets = [
            (70, 0.4, Circle(390, 320, 7, color=hex_to_rgb("#ff0000"), batch=self.batch), []), #venus
            (100, 0.3, Circle(420, 320, 10, color=hex_to_rgb("#0000ff"), batch=self.batch), [
                (15, 1.5, Circle(0,0,3, color=hex_to_rgb("#ffffff"), batch=self.batch)), # luna
            ]), # tierra
            (140, 0.2, Circle(460, 320, 6, color=hex_to_rgb("#00ff00"), batch=self.batch), [
                (12, 1.5, Circle(0,0,2, color=hex_to_rgb("#ffffff"), batch=self.batch)), # luna
                (15, 1.5, Circle(0,0,2, color=hex_to_rgb("#ffffff"), batch=self.batch)) # luna
            ]), # marte
            (280, 0.1, Circle(600, 320, 16, color=hex_to_rgb("#ff00ff"), batch=self.batch), [
                (20, 1.5, Circle(0,0,4, color=hex_to_rgb("#ffffff"), batch=self.batch)), # luna
                (25, 1.2, Circle(0,0,3, color=hex_to_rgb("#ffffff"), batch=self.batch)), # luna
                (30, 0.9, Circle(0,0,2, color=hex_to_rgb("#ffffff"), batch=self.batch)), # luna
                (35, 0.8, Circle(0,0,5, color=hex_to_rgb("#ffffff"), batch=self.batch)) # luna
            ]), # jupiter
        ]
        self.angle = 0
    
    def on_update(self, deltatime):
        self.angle += deltatime
        for distance, speed, planet, moons in self.planets:
            planet.x = 320 + distance * math.cos(self.angle * speed)
            planet.y = 320 + distance * math.sin(self.angle * speed)
            for moon_distance, moon_speed, moon in moons:
                moon.x = planet.x + moon_distance * math.cos(self.angle * moon_speed)
                moon.y = planet.y + moon_distance * math.sin(self.angle * moon_speed)

    def on_draw(self):
        self.clear()
        self.batch.draw()
    
renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1/60)
run()
