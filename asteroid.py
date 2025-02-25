import pygame
import random
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            offSetAngle = random.uniform(20, 50)

            splitVelocity1 = self.velocity.rotate(offSetAngle)
            splitVelocity2 = self.velocity.rotate(-offSetAngle)

            newRadius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid1.velocity = splitVelocity1 * 1.2  

            asteroid2 = Asteroid(self.position.x, self.position.y, newRadius) 
            asteroid2.velocity = splitVelocity2 * 1.2
           
            

