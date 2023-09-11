import pgzrun
from pgzhelper import * # for image scaling
import random
import pygame

WIDTH = 1200
HEIGHT = 800
black = (0,0,0)
card_suit_names=('cardspades','cardhearts','carddiamonds','cardclubs')
card_rank_names=('a','2','3','4','5','6','7','8','9','10','j','q','k')
clicked = False
first_card=None
second_card=None
game_over=True
class Card:
    cover_image='cardback_blue5'
    def __init__(self,number, pos):
        self.number=number
        self.pos = pos
        self.dead=False
        self.actor = Actor(Card.cover_image)
        self.actor.pos=pos
        self.actor.scale=0.6
    def getRank(self):
        return self.number%13
    def showCard(self):
        self.actor.image = f'{card_suit_names[self.number%4]}{card_rank_names[self.number%13]}'
    def hideCard(self):
        self.actor.image = Card.cover_image

def generateCards():
    global cards, score, clicks
    cards = []
    clicks=0
    score = 0
    pos_start_x, pos_start_y = 45,150
    x_gap, y_gap = 90,120
    for n in random.sample(list(range(52)),52):
        card = Card(n, (pos_start_x, pos_start_y))
        cards.append(card)
        pos_start_x+=x_gap
        if pos_start_x>WIDTH:
            pos_start_x=45
            pos_start_y+=y_gap
def update():
    pass

def draw():
    screen.fill(black)
    screen.draw.text(f"Score: {score}, clicks: {clicks}", (470,50), color="orange",fontsize=60)
    if game_over:
        screen.draw.text(f"Game over!", (450,500), color="orange",fontsize=100)
        screen.draw.text(f"Restart press r. Stop press q.", (450,600), color="blue",fontsize=60)
        return
    for card in cards:
        if not card.dead:
            card.actor.draw()
  
def check_match():
    global score, clicked, first_card, second_card,game_over
    if first_card.getRank() == second_card.getRank():
        score+=1
        first_card.dead=True
        second_card.dead=True
        if score == 26:
            game_over=True
    else:
        first_card.hideCard()
        second_card.hideCard()
    first_card=None
    second_card=None
    clicked=False
def on_key_down(key):
    global game_over
    if key == keys.R and game_over:
        generateCards()
        game_over=False
    elif key == keys.Q and game_over:
        pygame.quit()
        sys.exit()
    
def on_mouse_down(pos):
    if game_over:
        return
    global clicked, first_card, second_card, clicks
    if clicked == True :
        return
    clicked = True
    for card in cards:
        if (not card.dead) and card.actor.collidepoint(pos):
            if not first_card:
                first_card = card
                card.showCard()
                clicked=False
                return
            elif (not second_card) and card!=first_card:
                second_card = card
                card.showCard()
                clicks+=1
                clock.schedule_unique(check_match, 1.0)
                return    
    clicked=False
    
generateCards()
pgzrun.go()

    
