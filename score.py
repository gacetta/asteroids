import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 20)
        self.position = (20, 20)

    def update(self, points):
        self.score += points

    def draw(self, screen):
        score_text = self.font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, self.position)