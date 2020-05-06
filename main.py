import pygame
import time
import random


class Attack():
    def __init__(self, img, ranged, type, name, sound):
        self.sound = sound
        self.img = img
        self.name = name
        self.ranged = ranged
        self.type = type
        self.x = 0
        self.y = 0


class Enemy():
    def __init__(self, img, hp, attk):
        self.img = img
        self.hp = hp
        self.attk = attk
        self.x = 0
        self.y = 0
        self.alive = True


class Character():
    def __init__(self, bio, stats, img, attack_class, talk):
        self.talk = talk
        self.attack_class = attack_class
        self.img = img
        self.bio = bio
        self.stats = stats
        self.hp = 100
        self.mp = 100
        self.attk = 100
        self.mgattk = 100
        self.critchance = 50
        self.critscale = 100
        self.defense = 100
        self.x = 0
        self.y = 0

    def attack(self):
        return [self.attack_class.img, self.attack_class.ranged]

    def walk(self):
        pass


def main():
    running = True

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("TTN")

    # sound
    pygame.mixer.music.load('Music/mainmenu.mp3')
    pygame.mixer.music.play(-1)

    # images
    ttn = pygame.image.load('Images/ttn.png')
    screen.blit(ttn, (0, 0))

    left = pygame.image.load('Images/left.png')
    screen.blit(left, (400, 300))
    right = pygame.image.load('Images/right.png')
    screen.blit(right, (700, 300))

    chrispic = pygame.image.load('Images/chris.png')
    garypic = pygame.image.load('Images/gary.png')
    anthonypic = pygame.image.load('Images/anthony.png')
    navpic = pygame.image.load('Images/nav.png')
    zacpic = pygame.image.load('Images/zac.png')
    danielpic = pygame.image.load('Images/daniel.png')
    ibpic = pygame.image.load('Images/ib.png')

    attkchrispic = pygame.image.load('Images/attkchris.png')
    attkgarypic = pygame.image.load('Images/attkgary.png')
    attkdanielpic = pygame.image.load('Images/attkdaniel.png')
    attkanthonypic = pygame.image.load('Images/attkanthony.png')
    attkzacpic = pygame.image.load('Images/attkzac.png')

    attk1sound = pygame.mixer.Sound("Music/1.wav")
    attk2sound = pygame.mixer.Sound("Music/2.wav")
    attk3sound = pygame.mixer.Sound("Music/3.wav")

    talk1sound = pygame.mixer.Sound("Music/voice1.wav")
    talk2sound = pygame.mixer.Sound("Music/voice2.wav")
    talk3sound = pygame.mixer.Sound("Music/voice3.wav")
    talk4sound = pygame.mixer.Sound("Music/voice4.wav")
    talk5sound = pygame.mixer.Sound("Music/voice5.wav")

    talklist = [talk1sound,talk2sound,talk3sound,talk4sound,talk5sound]

    trueshot = Attack(attkchrispic, True, 'ATTK', 'TRUESHOT', attk1sound)
    heal = Attack(attkgarypic, False, 'MGATTK', 'HEAL', attk1sound)
    samuraidash = Attack(attkanthonypic, False, 'ATTK', 'SAMURAI DASH', attk3sound)
    simpstrike = Attack(attkzacpic, False, 'ATTK', 'SIMP STRIKE', attk2sound)
    flamebolt = Attack(attkdanielpic, True, 'MGATTK', 'FLAME BOLT', attk3sound)

    chris = Character(['Chris'], ['Low Defense', 'High Attack', 'Marksman'], chrispic, trueshot, talklist)
    gary = Character(['Gary'], ['Low Defense', 'High Mana', 'Healer'], garypic, heal, talklist)
    anthony = Character(['Anthony'], ['Low Defense', 'High Attack', 'High Crit', 'Samurai'], anthonypic, samuraidash, talklist)
    nav = Character(['Nav'], ['Low Everything', 'Noob'], navpic, simpstrike, talklist)
    zac = Character(['Zac', 'The SIMP'], ['High Defense', 'Low Attack', 'Simp Knight'], zacpic, simpstrike,talklist)
    daniel = Character(['Daniel'], ['Low Defense', 'High Magic Attack', 'Fire Mage'], danielpic, flamebolt, talklist)
    ib = Character(['IB'], ['Low Defense', 'High Attack', 'Assassin'], ibpic, trueshot, talklist)

    char_list = [chris, gary, anthony, nav, zac, daniel,ib]

    # keeps track of which character in the list is selected
    ind = random.randint(0, len(char_list)-1)

    # tracks the currently selected character
    current = char_list[ind]
    screen.blit(current.img, (550, 300))

    font = pygame.font.Font("c.ttf", 24)

    biotop = 150
    for k in current.bio:
        bio = font.render(k, True, (0, 0, 0))
        screen.blit(bio, (130, biotop))
        biotop += 50
    statstop = 150
    for i in current.stats:
        stats = font.render(i, True, (0, 0, 0))
        screen.blit(stats, (1000, statstop))
        statstop += 50

    left_area = pygame.Rect(400, 300, 100, 100)
    right_area = pygame.Rect(700, 300, 100, 100)

    play_rect = pygame.Rect(550, 500, 300, 150)

    pygame.display.flip()
    while running:
        # check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checks if left and right arrows are pressed and changes the character
                if left_area.collidepoint(event.pos):
                    screen.blit(ttn, (0, 0))
                    screen.blit(right, (700, 300))
                    screen.blit(left, (400, 300))
                    if ind - 1 >= 0:
                        current = char_list[ind - 1]
                        ind -= 1
                    screen.blit(current.img, (550, 300))
                    biotop = 150
                    for k in current.bio:
                        bio = font.render(k, True, (0, 0, 0))
                        screen.blit(bio, (130, biotop))
                        biotop += 50
                    statstop = 150
                    for i in current.stats:
                        stats = font.render(i, True, (0, 0, 0))
                        screen.blit(stats, (1000, statstop))
                        statstop += 50

                if right_area.collidepoint(event.pos):
                    screen.blit(ttn, (0, 0))
                    screen.blit(right, (700, 300))
                    screen.blit(left, (400, 300))
                    if ind + 1 <= 6:
                        current = char_list[ind + 1]
                        ind += 1
                    screen.blit(current.img, (550, 300))
                    biotop = 150
                    for k in current.bio:
                        bio = font.render(k, True, (0, 0, 0))
                        screen.blit(bio, (130, biotop))
                        biotop += 50
                    statstop = 150
                    for i in current.stats:
                        stats = font.render(i, True, (0, 0, 0))
                        screen.blit(stats, (1000, statstop))
                        statstop += 50
                if play_rect.collidepoint(event.pos):
                    game(screen, current)
                    break
        pygame.display.flip()


def game(screen, chracter):
    running = True

    first = 1
    while running:
        if first == 1:
            val = map0(screen, chracter, 100)
        first = 0
        if val is not None:
            if val[0] == 0:
                val = map0(screen, chracter, val[1])
            elif val[0] == 1:
                val = map1(screen, chracter, val[1])
            elif val[0] == 2:
                val = map2(screen, chracter, val[1])
            elif val[0] == 3:
                val = map3(screen, chracter, val[1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def mechanics(screen, character, img, song, left_map, right_map, enemy):
    image = pygame.image.load(img)
    screen.blit(image, (0, 0))
    Clock = pygame.time.Clock()
    screen.blit(character.img, (character.x, character.y))
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
    running = True

    enemy_list = []

    enemy_mover = [-40, 40, 0]
    attack_list = []

    cd = 0
    jumpcd = 0
    voice_cd = 0
    last_direct = 'r'
    slowattk = 0
    melee_stay = 0
    enemymovement = 0
    comedowncd = 0
    font = pygame.font.Font("c.ttf", 72)

    while running:
        Clock.tick(60)
        keyinput = pygame.key.get_pressed()
        # check for all events
        if character.y != 500:
            if comedowncd == 15:
                comedowncd = 0
                character.y = 500
            elif comedowncd != 15:
                comedowncd += 1
        if len(enemy_list) == 0:
            if enemy is not None:
                num_enemy = random.randint(1, 5)
                for i in range(num_enemy):
                    enemy_list.append(Enemy(enemy.img, enemy.hp, enemy.attk))
                for k in enemy_list:
                    k.y = 550
                    mylst = [400, 600, 440, 640, 680, 720]
                    k.x = mylst[random.randint(0, 5)]
                    screen.blit(k.img, (k.x, k.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if keyinput[pygame.K_LEFT] and character.x >= 0:
            last_direct = 'l'
            character.x -= 12
        if keyinput[pygame.K_RIGHT] and character.x <= 1200:
            last_direct = 'r'
            character.x += 12
        if keyinput[pygame.K_UP] and 0 < character.x < 100:
            return [left_map, 1100]
        if keyinput[pygame.K_UP] and 1180 < character.x < 1280:
            return [right_map, 100]
        if keyinput[pygame.K_v] :
            if voice_cd ==0:
                voice_cd = 80
                num = random.randint(0,len(character.talk)-1)
                character.talk[num].play()

        if keyinput[pygame.K_LALT]:
            if jumpcd ==30:
                jumpcd = 0
                character.y -= 150

        if keyinput[pygame.K_LCTRL]:
            if cd == 0:
                cd = 50
                character.attack_class.sound.play()
                if last_direct == 'r':
                    attack_list.append(character.attack() + [[character.x + 75, character.y + 50], last_direct])
                if last_direct == 'l':
                    attack_list.append(character.attack() + [[character.x - 75, character.y + 50], last_direct])


        screen.blit(image, (0, 0))
        screen.blit(character.img, (character.x, character.y))

        for i in enemy_list:
            if enemymovement == 20:
                units_moved = random.randint(0, 2)
                if 0 < i.x + enemy_mover[units_moved] < 1200:
                    i.x += enemy_mover[units_moved]
                elif i.x + enemy_mover[units_moved] < 0:
                    i.x += enemy_mover[1]
                elif i.x + enemy_mover[units_moved] >1200:
                    i.x -= enemy_mover[0]
            screen.blit(i.img, (i.x, i.y))
        if enemymovement == 20:
            enemymovement = 0

        for k in attack_list:
            screen.blit(k[0], (k[2][0], k[2][1]))

        for enmy in enemy_list:
                for attk in attack_list:
                    for x in range(enmy.x,enmy.x+60):
                        if attk[2][0] == x:
                            dmg = random.randint(character.attk-20,character.attk+20)
                            enmy.hp -= dmg
                            dmg = font.render(str(dmg), True, (0, 0, 0))
                            screen.blit(dmg, (enmy.x, enmy.y - 120))
                            if enmy.hp <=0:
                                enemy_list.remove(enmy)

        pygame.display.flip()

        for l in attack_list:
            if not l[1]:
                if melee_stay == 60:
                    melee_stay = 0
                    attack_list.remove(l)
            else:
                if slowattk == 3:
                    if l[3] == 'r':
                        l[2][0] += 40
                    if l[3] == 'l':
                        l[2][0] -= 40

        if cd != 0:
            cd -= 1
        if voice_cd !=0:
            voice_cd -=1
        if slowattk != 3:
            slowattk += 1
        else:
            slowattk = 0
        if melee_stay !=60:
            melee_stay+=1
        if jumpcd != 30:
            jumpcd+=1
        if enemymovement != 20:
            enemymovement+=5

def map0(screen, character, charx):
    character.x = charx
    character.y = 500
    return mechanics(screen, character, 'Images/sqr1.png', 'Music/map0.mp3', 3, 1, None)


def map1(screen, character, charx):
    character.x = charx
    character.y = 500
    return mechanics(screen, character, 'Images/foodcourt.png', 'Music/map1.mp3', 0, 2, Enemy(pygame.image.load('Images/teeth.png'), 500, (50, 100)))


def map2(screen, character, charx):
    character.x = charx
    character.y = 500
    return mechanics(screen, character, 'Images/cele.png', 'Music/map1.mp3', 1, 3, Enemy(pygame.image.load('Images/lol.png'), 500, (50, 100)))


def map3(screen, character, charx):
    character.x = charx
    character.y = 500
    return mechanics(screen, character, 'Images/movie.png', 'Music/map3.mp3', 2, 0, Enemy(pygame.image.load('Images/egirl.png'), 500, (50, 100)))


if __name__ == "__main__":
    main()
