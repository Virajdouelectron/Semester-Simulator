import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Semester Simulator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)

# Sounds
click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
error_sound = pygame.mixer.Sound("assets/sounds/error.wav")
background_music = "assets/sounds/background.mp3"
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)

# Images
background_img = pygame.image.load("assets/images/background.png")
energy_icon = pygame.image.load("assets/images/energy.png")
caffeine_icon = pygame.image.load("assets/images/caffeine.png")
mental_health_icon = pygame.image.load("assets/images/mental_health.png")
money_icon = pygame.image.load("assets/images/money.png")
gpa_icon = pygame.image.load("assets/images/gpa.png")

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.caffeine = 0
        self.mental_health = 100
        self.money = 100
        self.gpa = 4.0
        self.time = 0  # in minutes
        self.project_progress = 0

    def consume_item(self, item):
        if item == "energy drink":
            self.energy += 20
            self.caffeine += 10
        elif item == "coffee":
            self.energy += 10
            self.caffeine += 5
        elif item == "mystery leftovers":
            effect = random.choice(["good", "bad"])
            if effect == "good":
                self.energy += 15
                self.mental_health += 10
            else:
                self.energy -= 10
                self.mental_health -= 10

    def manage_time(self, activity):
        if activity == "coding":
            self.energy -= 20
            self.time += 120
            self.project_progress += 10
        elif activity == "attending classes":
            self.energy -= 10
            self.time += 60
            self.gpa += 0.1
        elif activity == "napping":
            self.energy += 30
            self.time += 30
        elif activity == "working part-time":
            self.energy -= 15
            self.time += 180
            self.money += 50

    def social_event(self, event):
        if event == "tech meetup":
            self.mental_health += 20
        elif event == "gaming night":
            self.mental_health += 15
            self.energy -= 10
        elif event == "internship":
            self.mental_health -= 10
            self.money += 100

    def random_event(self):
        event = random.choice(["blue screen of death", "good group member", "bad group member"])
        if event == "blue screen of death":
            print("Random system crash! You lost some progress.")
            self.project_progress -= 5
        elif event == "good group member":
            print("A good group member helped you out!")
            self.project_progress += 10
        elif event == "bad group member":
            print("A bad group member caused trouble!")
            self.project_progress -= 10

    def draw_stats(self):
        # Draw stats on the screen
        stats = [
            ("Energy", self.energy, energy_icon),
            ("Caffeine", self.caffeine, caffeine_icon),
            ("Mental Health", self.mental_health, mental_health_icon),
            ("Money", self.money, money_icon),
            ("GPA", round(self.gpa, 2), gpa_icon),
        ]

        y_offset = 10
        for stat_name, stat_value, icon in stats:
            screen.blit(icon, (10, y_offset))
            stat_text = font.render(f"{stat_name}: {stat_value}", True, BLACK)
            screen.blit(stat_text, (50, y_offset))
            y_offset += 50

    def check_status(self):
        print(f"Energy: {self.energy}, Caffeine: {self.caffeine}, Mental Health: {self.mental_health}, Money: {self.money}, GPA: {self.gpa}, Project Progress: {self.project_progress}")

    def endgame_goal(self):
        if self.gpa >= 3.0 and self.project_progress >= 100:
            return "Congratulations! You passed the semester with a high GPA and completed your capstone project!"
        else:
            return "You didn't make it. Better luck next semester."

# Main Game Loop
def main():
    player = Player("Viraj")
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        screen.blit(background_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.draw_stats()
        pygame.display.flip()
        clock.tick(30)  # Limit to 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
