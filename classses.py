from settings import *

class Car(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.pos = V2(HW, HH)  # Position
        self.direction = V2()  # Input direction
        self.drift_direction = V2()  # Smoothed drift direction
        self.drift_speed = 5  # Drift interpolation speed
        self.speed = 400  # Movement speed
        self.angle = 0  # Angle (future use?)

        # Car visuals
        self.image = pygame.Surface((40, 65))
        self.image.fill('maroon')
        self.rect = self.image.get_frect(center=self.pos)

    def check_collision(self, dt):
        # Get directional input from keys
        keys = pygame.key.get_pressed()
        self.direction.update(keys[pygame.K_d] - keys[pygame.K_a], 
                              keys[pygame.K_s] - keys[pygame.K_w])

        # Normalize direction if it has a magnitude
        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()

        # Smooth drift direction using linear interpolation (LERP)
        self.drift_direction += (self.direction - self.drift_direction) * self.drift_speed * dt

        # Clamp very small drift values to zero for precision stability
        self.drift_direction.update(
            0 if abs(self.drift_direction.x) < 1e-2 else self.drift_direction.x,
            0 if abs(self.drift_direction.y) < 1e-2 else self.drift_direction.y,
        )

    def move(self, dt):
        # Move position based on drift and speed
        self.pos += self.drift_direction * self.speed * dt
        self.rect.center = self.pos  # Update rect position
        # Debug drift output (optional for debugging)
        print(f"Drift Direction: {self.drift_direction}")

    def update(self, dt):
        self.check_collision(dt)
        self.move(dt)
