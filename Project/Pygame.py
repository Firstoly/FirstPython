import pgzrun
from random import randint
import time
current_stage = 0

def draw():
    if Game_Over:
        screen.fill('black')
        screen.draw.text(f'Game Over!!!', center=(WIDTH/2, HEIGHT/2), fontsize=50, color='white')
        screen.draw.text(f'Your Score is {Score}', center=(WIDTH/2, 500), fontsize=50, color='white')
        screen.draw.text(f'Press R for MENU', center=(WIDTH/2, 600), fontsize=50, color='white')

    elif current_stage == 2:
        map.draw()
        screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
        screen.draw.text(f'HP:  {HP}', (690, 10), fontsize=30)
        screen.draw.text(f'Time: {Time}', (300, 10), fontsize=30)
        boy.draw()
        coin1.draw()
        coin2.draw()
        coin3.draw()
        potion.draw()
        clockitem.draw()
        slime1.draw()
        heart.draw()
    elif current_stage == 1:
        map.draw()
        screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
        screen.draw.text(f'Time: {Time}', (300, 10), fontsize=30)
        screen.draw.text(f'Level:  {level}', (690, 10), fontsize=30)
        boy.draw()
        coin1.draw()
        coin2.draw()
        coin3.draw()
    elif current_stage == 0:
        menu.draw()
        

def reset_boy():
    boy.pos = (boy.width/2, boy.height/2)


def place_coin1():
    coin1.x = randint(coin1.width, WIDTH - coin1.width)
    coin1.y = randint(coin1.height, HEIGHT - coin1.height)
def place_coin2():
    coin2.x = randint(coin2.width, WIDTH - coin2.width)
    coin2.y = randint(coin2.height, HEIGHT - coin2.height)
def place_coin3():
    coin3.x = randint(coin3.width, WIDTH - coin3.width)
    coin3.y = randint(coin3.height, HEIGHT - coin3.height)

def place_potion():
    potion.x = randint(potion.width, WIDTH - potion.width)
    potion.y = randint(potion.height, HEIGHT - potion.height)

def count_index():
    global index, walk

    if walk == "Down":
        index += 1
        if index == 10:
            index = 0
        boy.image = images_boy[index]

    elif walk == "Up":
        index += 1
        if index == 10:
            index = 0
        boy.image = images_boy_back[index]

    elif walk == "Left":
        index += 1
        if index == 10:
            index = 0
        boy.image = images_boy_left[index]

    elif walk == "Right":
        index += 1
        if index == 10:
            index = 0
        boy.image = images_boy_right[index]
    else:
        walk = "Not"
        index = 0


def update():
    global walk, index, Score, Game_Over, HP, slime_attack_timer, current_stage, countcoin, Time, potion_effect_time, speed_multiplier, potion_spawn_timer, game_in_progress,level

    if not game_in_progress:
        return

    if potion_effect_time > 0:
        speed_multiplier = 2
        potion_effect_time -= 1
    else:
        speed_multiplier = 1
        speed_multiplier = 1
    if keyboard.LEFT:
        boy.x -= 5 * speed_multiplier
        walk = "Left"
    elif keyboard.RIGHT:
        boy.x += 5 * speed_multiplier
        walk = "Right"
    elif keyboard.UP:
        boy.y -= 5 * speed_multiplier
        walk = "Up"
    elif keyboard.DOWN:
        boy.y += 5 * speed_multiplier
        walk = "Down"
    else:
        index = 0
        walk = "Not"
    current_time = time.time()
    if current_time - slime_attack_timer >= 1 and Score <= countcoin and current_stage == 2:
        if slime1.x < boy.x:
            slime1.x += 1.5
        elif slime1.x > boy.x:
            slime1.x -= 1.5
        if slime1.y < boy.y:
            slime1.y += 1.5
        elif slime1.y > boy.y:
            slime1.y -= 1.5
    boy.x = max(0, min(boy.x, WIDTH - 1))
    boy.y = max(0, min(boy.y, HEIGHT - 1))
    if (current_stage == 2 and current_time - slime_attack_timer >= 1) and not Game_Over:
        if boy.colliderect(slime1):
            sounds.hurt.play()
            print('You got HIT!!!')
            HP -= 1
            slime_attack_timer = current_time  # Reset the slime attack timer
            if HP <= 0:
                Game_Over = True
        
        if boy.colliderect(coin1):
            sounds.ping.play()
            Score += 1
            place_coin1()
        if boy.colliderect(coin2):
            sounds.ping.play()
            Score += 1
            place_coin2()
        if boy.colliderect(coin3):
            sounds.ping.play()
            Score += 1
            place_coin3()

        if boy.colliderect(potion):
            sounds.ping.play()
            potion_effect_time = 300
            place_potion()
    if current_stage == 1:
        if boy.colliderect(coin1):
            sounds.ping.play()
            Score += 1
            place_coin1()
        if boy.colliderect(coin2):
            sounds.ping.play()
            Score += 1
            place_coin2()
        if boy.colliderect(coin3):
            sounds.ping.play()
            Score += 1
            place_coin3()

    potion_spawn_timer -= 1
    if potion_spawn_timer <= 0:
        place_potion()  # Place the potion if the timer has expired
        potion_spawn_timer = 360

    if Score >= countcoin:
        countcoin *= 1.5
        level += 1
        print(f"Level UP!!!!{level}")

def count_time():
    global Time, Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)
    if Time <= 0:
        Time = 0
#play again
def on_key_down(key, mod, unicode):
    global Game_Over, Score, Time, current_stage, HP, game_in_progress
    if (key == keys.F1) and (current_stage==0 or Game_Over):
        reset_game()
        current_stage = 1
        clock.schedule_interval(count_time, 1.0)
        game_in_progress = True
    elif (key == keys.F2)  and (current_stage==0 or Game_Over):
        reset_game()
        current_stage = 2
        clock.schedule_interval(count_time, 1.0)
        game_in_progress = True
    elif key == keys.R and Game_Over:
        reset_game()
        game_in_progress = False
def reset_game():
    global Game_Over, Score, Time, current_stage, HP, game_in_progress,level
    Game_Over = False
    Score = 0
    Time = 0
    HP = 10
    level = 0
    current_stage = 0  # Change this to the desired starting stage
    game_in_progress = False
    clock.unschedule(count_time)
# Main Program
game_in_progress = False
TITLE = "Coin Collector Game"
WIDTH = 933
HEIGHT = 800
index = 0
walk = "Not"
Score = Time = 0
MAX_TIME = 60 #timelimit
Game_Over = False
HP = 10
countcoin = 5
level = 0
slime_attack_timer = time.time()
potion_effect_time = 0
speed_multiplier = 1
potion_spawn_timer = 0
# Animation for character
images_boy = ['boy', 'down(1)', 'down(2)', 'down(3)', 'down(4)','down(5)', 'down(6)', 'down(7)', 'down(8)', 'down(9)', 'down(10)']
images_boy_left = ['left(1)', 'left(2)', 'left(3)', 'left(4)','left(5)', 'left(6)', 'left(7)', 'left(8)', 'left(9)', 'left(10)']
images_boy_right = ['right(1)', 'right(2)', 'right(3)', 'right(4)','right(5)', 'right(6)', 'right(7)', 'right(8)', 'right(9)', 'right(10)']
images_boy_back = ['up(1)', 'up(2)', 'up(3)', 'up(4)', 'up(5)', 'up(6)', 'up(7)', 'up(8)', 'up(9)', 'up(10)']
actors = ['slime1']
# image
boy = Actor('boy', (WIDTH/2, HEIGHT/2))
boy1 = Actor('down(1)')
boy1 = Actor('down(2)')
boy1 = Actor('down(3)')
boy1 = Actor('down(4)')
coin1 = Actor('coin')
coin2 = Actor('coin')
coin3 = Actor('coin')
map = Actor('map')
clockitem = Actor('clock',(270,20))
potion = Actor('potion')
slime1 = Actor('slime')
menu = Actor('background')
heart = Actor('heart',(660,20))
# Clock
clock.schedule_interval(count_index, 0.090)
clock.schedule_interval(count_time, 1.0)
place_coin1()
place_coin2()
place_coin3()
place_potion()

pgzrun.go()
