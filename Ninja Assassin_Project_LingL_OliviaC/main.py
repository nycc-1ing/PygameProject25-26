from gamelib import *

# Game Functions(Modular Programming)

def positionObjects(objects):
    for i in range(len(objects)):
        x = randint(50,750)
        y = -randint(100,5000)
        objects[i].moveTo(x,y)
        objects[i].setSpeed(4,180)

def fruits_update():

    for i in range(len(apple)):
        apple[i].move()
        if crosshair.collidedWith(apple[i]) and mouse.LeftClick:
            game.score += 5
            apple[i].visible = False
            shoot.play()

    for i in range(len(bomb)):
        bomb[i].move()
        if crosshair.collidedWith(bomb[i]) and mouse.LeftClick:
            crosshair.health -= 10
            bomb[i].visible = False
            shoot.play()
            explosion.visible = True
            explosion.moveTo(mouse.x, mouse.y)
            boom.play()

# Main Program
game = Game(800,600, "Fruit Sniper")
forest = Image("forest.webp", game)
forest.resizeTo(game.width, game.height)
game.setBackground(forest)

# Crosshair Image
crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-93)

# Explosion
explosion = Animation("explosion2.png", 14, game, 512/4, 512/4, 1)

# Fruit Lists
apple = []
for i in range(20):
    a = Animation("apple.png", 1, game, 1440, 360)
    a.resizeBy(-75)
    apple.append(a)
positionObjects(apple)

orange = []
for i in range(10):
    o = Animation("orange.png", 1, game, 1400, 350)
    o.resizeBy(-75)
    orange.append(o)
positionObjects(orange)

lemon = []
for i in range(10):
    l = Animation("lemon.png", 1, game, 3200, 800)
    l.resizeBy(-89)
    lemon.append(l)
positionObjects(lemon)

cherry = []
for i in range(10):
    c = Animation("cherry.png", 1, game, 3360, 966)
    c. resizeBy(-89)
    cherry.append(c)
positionObjects(cherry)

# Obstacles
bomb = []
for i in range(15):
    b = Animation("bomb.png", 1, game, 1440, 360)
    b.resizeBy(-70)
    bomb.append(b)
positionObjects(bomb)

poisonapple = []
for i in range(10):
    pa = Animation("poisonousapple.png", 1, game, 1860, 465)
    pa.resizeBy(-81)
    poisonapple.append(pa)
positionObjects(poisonapple)

# game ending screen
youwin = Image("youwin.png", game)
youwin.resizeBy(-40)

youlose = Image("youlose.png", game)
youlose.resizeBy(-40)

# game starting screen images
title = Image("title.png", game)
title.resizeBy(-10)
title.y = 150

howto = Image("howtoplay1.png", game)
howto.x = 535
howto.y = 510
howto_off = Image("howtoplay1.png", game)
howto_on = Image("howtoplay2.png", game)
howto_off.resizeBy(-63)
howto_on.resizeBy(-63)

play = Image("play1.png", game)
play.x = 529
play.y = 610
play_off = Image("play1.png", game)
play_on = Image("play2.png", game)
play_off.resizeBy(-70)
play_on.resizeBy(-70)

story = Image("story1.png", game)
story.x = 540
story.y = 400
story_off = Image("story1.png", game)
story_on = Image("story2.png", game)
story_off.resizeBy(-65)
story_on.resizeBy(-65)

howtoText = Image("howto.png", game)
howtoText.visible = False
howtoText.resizeTo(800,600)

storyText = Image("story.png", game)
storyText.visible = False
storyText.resizeTo(800,600)

# sounds
shoot = Sound("gun.wav", 1)
boom = Sound("explosion_other.wav", 2)
lose = Sound("losing.mp3", 3)
win = Sound("winning.mp3", 4)

#----------------**------------------**------------------
# Game Start Screen
while not game.over:
    game.processInput()
    forest.draw()

    title.draw()
    howto.draw()
    play.draw()
    story.draw()

    storyText.draw()
    howtoText.draw()

    if mouse.collidedWith(howto, "rectangle"):
        howto.setImage(howto_on.image)
    else:
        howto.setImage(howto_off.image)

    if mouse.collidedWith(play, "rectangle"):
        play.setImage(play_on.image)
    else:
        play.setImage(play_off.image)

    if mouse.collidedWith(story, "rectangle"):
        story.setImage(story_on.image)
    else:
        story.setImage(story_off.image)
                        
    if mouse.collidedWith(story, "rectangle") and mouse.LeftClick:
        storyText.visible = True
        
    if mouse.collidedWith(howto, "rectangle") and mouse.LeftClick:
        howtoText.visible = True

    if mouse.collidedWith(play, "rectangle") and mouse.LeftClick:
        game.over = True

    if keys.Pressed[K_SPACE]:
        storyText.visible = False
        howtoText.visible = False
                    
    game.update(30) # end of start screen

# ----------------------- LEVEL 1 -----------------------

mouse.visible = False
game.over = False

# Level 1 Game Loop
while not game.over:
    game.processInput()
    forest.draw()

    for i in range(len(apple)):
        apple[i].move()
        if crosshair.collidedWith(apple[i]) and mouse.LeftClick:
            game.score += 5
            apple[i].visible = False
            shoot.play()

    for i in range(len(orange)):
        orange[i].move()
        if crosshair.collidedWith(orange[i]) and mouse.LeftClick:
            game.score += 5
            orange[i].visible = False
            shoot.play()

    for i in range(len(bomb)):
        bomb[i].move()
        if crosshair.collidedWith(bomb[i]) and mouse.LeftClick:
            crosshair.health -= 10
            bomb[i].visible = False
            shoot.play()
            explosion.visible = True
            explosion.moveTo(mouse.x, mouse.y)
            boom.play()
        
    crosshair.draw()
    crosshair.moveTo(mouse.x, mouse.y)

    if game.score >= 100 or crosshair.health <= 0:
        game.over = True

    game.drawText("score:" + str(game.score), 10,10)
    game.drawText("health:" + str(crosshair.health), 10,30)

    game.update(30) # End of Level 1

# ----------------------- LEVEL 2 -----------------------

game.over = False
game.score = 0

# Level 2 Game Loop
while not game.over and crosshair.health >= 0:
    game.processInput()
    forest.draw()

    fruits_update()

    for i in range(len(lemon)):
        lemon[i].move()
        if crosshair.collidedWith(lemon[i]) and mouse.LeftClick:
            game.score += 5
            lemon[i].visible = False
            shoot.play()

    for i in range(len(cherry)):
        cherry[i].move()
        if crosshair.collidedWith(cherry[i]) and mouse.LeftClick:
            game.score += 5
            cherry[i].visible = False
            shoot.play()

    for i in range(len(poisonapple)):
        poisonapple[i].move()
        if crosshair.collidedWith(poisonapple[i]) and mouse.LeftClick:
            game.score -= 10
            poisonapple[i].visible = False
            shoot.play()
               
    crosshair.move()
    crosshair.moveTo(mouse.x, mouse.y)

    if game.score >= 100 or crosshair.health <= 0:
        game.over = True

    game.drawText("score:" + str(game.score), 10, 25)
    game.drawText("health:" + str(crosshair.health), 10,40)
    game.drawText("level 2", 10, 5)
    
    game.update(30)

game.over = False
# Game Ending Screen
while not game.over:
    game.processInput()
    forest.draw()

    if game.score >= 100:
        youwin.draw()
        win.play()

    if game.score <= 0 or crosshair.health <= 0:
        youlose.draw()
        lose.play()

    game.update(30)
game.quit()
