# подключаем модули
import pygame
import sys
from random import randint
from const import *
from ship import Ship
from bg import Background
from meteor import Meteor
from bullet import Bullet
from text import TextObject
from bonus import Bonus

#НАСТРОЙКА ИГРЫ (ИНИЦИАЛИЗАЦИЯ)
#инициализация библиотеки
pygame.init()
#создание экрана, указываем ширину и высоту в кортеже
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# создаем часы для отслеживания FPS
clock = pygame.time.Clock()
shoot_sound = pygame.mixer.Sound('res/sfx_laser1.ogg')
# ПЕРЕМЕННЫЕ
# переменная для управления циклом
run = True
# счет
score = 0
#здоровье

#СПРАЙТЫ И ГРУППЫ
#создание групп
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
bonus_sprites = pygame.sprite.Group()
#создание игровых объектов
player_ship = Ship()
bg1 = Background(0,0)
bg2 = Background(0,-SCREEN_HEIGHT)
meteors = []
text_score = TextObject(10,10,lambda: str(score),YELLOW,"courier",20)
for i in range(15):
    meteor = Meteor()
    meteors.append(meteor)
#добавление в группы
all_sprites.add(bg1)
all_sprites.add(bg2)
all_sprites.add(player_ship)
for i in range(15):
    all_sprites.add(meteors[i])
    meteor_sprites.add(meteors[i])
# ФУНКЦИИ
def draw_hp_bar(screen, x, y, hp):
    if hp < 0:
        hp = 0
    fill = hp/100*HP_BAR_WIDTH
    circuit_rect = pygame.Rect(x,y, HP_BAR_WIDTH, HP_BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y, fill, HP_BAR_HEIGHT)
    pygame.draw.rect(screen, GREEN, fill_rect)
    pygame.draw.rect(screen, WHITE, circuit_rect, 2)

# основной игровой цикл
while run:
    #0 задержка для фиксированного FPS
    clock.tick(FPS)
    #1 обработка событий
    for event in pygame.event.get():
        # если тип события - закрытие окна программы
        if event.type == pygame.QUIT:
            # выйти из программы
            run = False
        # стрельба по пробелу
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player_ship.rect.centerx, player_ship.rect.top)
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)
                shoot_sound.play()

    #2 действия и взаимодействия
    all_sprites.update()
    # ПРОВЕРКА СТОЛКНОВЕНИЙ
    #проверка столкновений корабля и метеоров
    hits = pygame.sprite.spritecollide(player_ship, meteor_sprites, True)
    for meteor in hits:
        #спавн нового метеора взамен удаленного
        new_meteor = Meteor()
        all_sprites.add(new_meteor)
        meteor_sprites.add(new_meteor)
        #отнимаем hp
        player_ship.hp -= meteor.rect.width // 3
    #проверка столкновений игрока и бонусов
    bonus_hits = pygame.sprite.spritecollide(player_ship, bonus_sprites, True)
    for bonus in bonus_hits:
        if bonus.type == 'pill':
            player_ship.hp +=  PILL_ADD_HP
            if player_ship.hp > PLAYER_MAX_HP:
                player_ship.hp = PLAYER_MAX_HP
    #конец игры
    if player_ship.hp <= 0:
        run = False
    #проверка столкновений пуль и метеоров
    bullet_hits = pygame.sprite.groupcollide(meteor_sprites, bullet_sprites,
                                             True, True)
    for meteor in bullet_hits:
        #выпадает бонус с шансом 10%
        chance = randint(1,1000)
        if chance < 100:
            bonus = Bonus(meteor.rect.centerx, meteor.rect.centery, meteor.speedy)
            all_sprites.add(bonus)
            bonus_sprites.add(bonus)
        #спавним новый метеор взамен сбитого
        new_meteor = Meteor()
        all_sprites.add(new_meteor)
        meteor_sprites.add(new_meteor)
        score += 1
        
    #3 отрисовка
    screen.fill(GREY)
    all_sprites.draw(screen)
    text_score.draw(screen)
    draw_hp_bar(screen, SCREEN_WIDTH - 155, 5, player_ship.hp)
    pygame.display.update()

#здесь основной цикл игры закончился
# завершить pygame
pygame.quit()
# выйти
sys.exit()
