import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grammar Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_width, player_height = 50, 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 5

# Bullet properties
bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullets = []

# Answer option properties
option_width, option_height = 100, 30
option_speed = 2
options = []

# Question properties
question_font = pygame.font.Font(None, 36)
question_text = ""

# Game properties
stage = 1
question_count = 0
score = 0

# Grammar questions and answer options
grammar_questions = [
{
"question": "She _____ her homework every day.",
"options": ["do", "does", "is doing", "did"],
"answer": "does"
},
{
"question": "The cat _____ on the mat.",
"options": ["sit", "sits", "sat", "is sitting"],
"answer": "sits"
},
{
"question": "They _____ to the party last night.",
"options": ["go", "goes", "went", "have gone"],
"answer": "went"
},
{
"question": "I _____ a book when she called.",
"options": ["was reading", "am reading", "have read", "read"],
"answer": "was reading"
},
{
"question": "She _____ in London for five years.",
"options": ["lives", "has lived", "is living", "lived"],
"answer": "has lived"
},
{
"question": "By the time he arrives, we _____ dinner.",
"options": ["will have finished", "will finish", "would finish", "finish"],
"answer": "will have finished"
},
{
"question": "If I _____ rich, I would travel the world.",
"options": ["am", "was", "were", "had been"],
"answer": "were"
},
{
"question": "The project _____ by the end of the month.",
"options": ["will complete", "will have completed", "would be completed", "will be completed"],
"answer": "will be completed"
},
{
"question": "She _____ the piano since she was a child.",
"options": ["plays", "has been playing", "played", "had played"],
"answer": "has been playing"
},
{
"question": "If he _____ harder, he would have passed the exam.",
"options": ["studies", "studied", "had studied", "would study"],
"answer": "had studied"
},
{
"question": "I wish I _____ more time to read.",
"options": ["have", "had", "would have", "will have"],
"answer": "had"
},
{
"question": "The movie was so boring that I _____ asleep.",
"options": ["fall", "fell", "had fallen", "have fallen"],
"answer": "fell"
},
{
"question": "She _____ to the store after she finishes work.",
"options": ["will go", "would go", "goes", "will have gone"],
"answer": "will go"
},
{
"question": "I _____ my keys. Can you help me find them?",
"options": ["lose", "lost", "have lost", "had lost"],
"answer": "have lost"
},
{
"question": "By the time we got to the stadium, the game _____.",
"options": ["had already started", "has already started", "would already start", "will have already started"],
"answer": "had already started"
},
{
"question": "If I _____ you, I would apologize.",
"options": ["was", "were", "am", "had been"],
"answer": "were"
},
{
"question": "She _____ the report by tomorrow.",
"options": ["will submit", "would submit", "will have submitted", "submits"],
"answer": "will have submitted"
},
{
"question": "I _____ TV when the phone rang.",
"options": ["watched", "was watching", "had watched", "have watched"],
"answer": "was watching"
},
{
"question": "He _____ in the library for three hours.",
"options": ["has been studying", "is studying", "studied", "had studied"],
"answer": "has been studying"
},
{
"question": "If she _____ the lottery, she would buy a new house.",
"options": ["wins", "won", "had won", "would win"],
"answer": "won"
},
{
"question": "I _____ my best friend since childhood.",
"options": ["know", "have known", "knew", "had known"],
"answer": "have known"
},
{
"question": "She _____ the piano beautifully.",
"options": ["play", "plays", "is playing", "has played"],
"answer": "plays"
},
{
"question": "If I _____ more time, I would learn a new language.",
"options": ["have", "had", "would have", "will have"],
"answer": "had"
},
{
"question": "By the time we arrive, the movie _____.",
"options": ["will have started", "will start", "would start", "starts"],
"answer": "will have started"
},
{
"question": "He _____ his car since last year.",
"options": ["has", "has had", "had", "would have"],
"answer": "has had"
},
{
"question": "If she _____ harder, she would have won the race.",
"options": ["tried", "had tried", "would try", "tries"],
"answer": "had tried"
},
{
"question": "I wish I _____ more money to donate to charity.",
"options": ["have", "had", "would have", "will have"],
"answer": "had"
},
{
"question": "She _____ her favorite book when the power went out.",
"options": ["read", "was reading", "had read", "has read"],
"answer": "was reading"
},
{
"question": "He _____ at that company for over a decade.",
"options": ["works", "has been working", "had worked", "will work"],
"answer": "has been working"
},
{
"question": "If I _____ the chance, I would travel to space.",
"options": ["have", "had", "would have", "will have"],
"answer": "had"
}
]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y - bullet_height
                bullets.append((bullet_x, bullet_y))

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move the bullets
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y = bullet
        bullet_y -= bullet_speed
        bullets[i] = (bullet_x, bullet_y)

        # Remove bullets that go off-screen
        if bullet_y < 0:
            bullets.pop(i)

    # Move the answer options
    for i, option in enumerate(options):
        option_text, option_x, option_y = option
        option_y += option_speed
        options[i] = (option_text, option_x, option_y)

        # Check for collision with bullets
        for bullet in bullets:
            bullet_x, bullet_y = bullet
            if (
                option_x < bullet_x < option_x + option_width and
                option_y < bullet_y < option_y + option_height
            ):
                if option_text == grammar_questions[question_count]["answer"]:
                    score += 1
                    options.clear()
                    bullets.clear()
                    question_count += 1
                    if question_count == len(grammar_questions):
                        stage += 1
                        question_count = 0
                else:
                    option_speed += 1

        # Check if options reach the bottom of the screen
        if option_y > height:
            running = False

    # Clear the screen
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, GREEN, (player_x, player_y, player_width, player_height))

    # Draw the bullets
    for bullet_x, bullet_y in bullets:
        pygame.draw.rect(window, RED, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Draw the answer options
    for option_text, option_x, option_y in options:
        pygame.draw.rect(window, WHITE, (option_x, option_y, option_width, option_height))
        option_surface = pygame.font.Font(None, 24).render(option_text, True, BLACK)
        window.blit(option_surface, (option_x + 10, option_y + 5))

    # Draw the question
    question_surface = question_font.render(question_text, True, WHITE)
    question_rect = question_surface.get_rect(center=(width // 2, height - 50))
    window.blit(question_surface, question_rect)

    # Generate a new question if needed
    if len(options) == 0:
        if question_count < len(grammar_questions):
            question_text = grammar_questions[question_count]["question"]
            answer_options = grammar_questions[question_count]["options"]
            correct_answer = grammar_questions[question_count]["answer"]

            random.shuffle(answer_options)
            for i, option_text in enumerate(answer_options):
                option_x = i * (option_width + 20) + (width - len(answer_options) * (option_width + 20)) // 2
                option_y = -option_height
                options.append((option_text, option_x, option_y))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
