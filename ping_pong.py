from pygame import *
window = display.set_mode((700, 500))
background = transform.scale(
    image.load('background.jpg'), (700, 500))
window.blit(background, (0, 0))
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("PLAYER 1 LOSE", True, (255, 0, 0)) 
lose2 = font1.render("PLAYER 2 LOSE", True, (255, 0, 0))

 
class GameSprite(sprite.Sprite): #создание класса геймпспрайт наследника спрайт
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height): #конструктор инит
        super().__init__() #функции суперкласса
        self.image = transform.scale(image.load(player_image), (player_width, player_height))#изображение
        self.speed = player_speed #скорость
        self.rect = self.image.get_rect() #квадрат хитбокс
        self.rect.x = player_x #координата x
        self.rect.y = player_y #координата y
        self.width = player_width #ширина
        self.height = player_height #высота
    def reset(self): #метод ресет который отрисовывает
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite): #создание класса плеер наследника геймпспрайт
    def update_l(self): #метод апдейт для передвижения
        keys_pressed = key.get_pressed() #получаем все события клавиатуры
        if keys_pressed[K_w] and self.rect.y > 0: #если нажата клавиша "a" и координаты больше нуля
            self.rect.y -= self.speed  #то плеер передвигается влево
        if keys_pressed[K_s] and self.rect.y < 700: #если нажата клавиша "d" и координаты игрока меньше 630 
            self.rect.y += self.speed #то игрок передвигается в право
    def update_r(self): #метод апдейт для передвижения
        keys_pressed = key.get_pressed() #получаем все события клавиатуры
        if keys_pressed[K_UP] and self.rect.y > 0: #если нажата клавиша "a" и координаты больше нуля
            self.rect.y -= self.speed  #то плеер передвигается влево
        if keys_pressed[K_DOWN] and self.rect.y < 500: #если нажата клавиша "d" и координаты игрока меньше 630 
            self.rect.y += self.speed #то игрок передвигается в право
ball = GameSprite("ball.png", 50, 50, 2, 50, 50 )    
Lraketka = Player('raketka.png', 10, 100, 5, 20, 400)
Rraketka = Player('raketka.png', 680, 100, 5, 20, 400)
clock = time.Clock()
finish = False
speed_x = 3
speed_y = 3
FPS = 60
game = True
while game:
    
    if finish != True:
        window.blit(background, (0, 0))
        Lraketka.reset()
        Rraketka.reset()
        ball.reset()
        Lraketka.update_l()
        Rraketka.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 500 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(Lraketka, ball) or sprite.collide_rect(Rraketka, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True
        if ball.rect.x > 700:
            window.blit(lose2, (200, 200))
            finish = True
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
    
