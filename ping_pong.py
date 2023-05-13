from pygame import *
window = display.set_mode((700, 500))
background = transform.scale(
    image.load('background.png'), (700, 500))
window.blit(background, (0, 0))



 
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
        if keys_pressed[K_s] and self.rect.y < 630: #если нажата клавиша "d" и координаты игрока меньше 630 
            self.rect.y += self.speed #то игрок передвигается в право
    def update_r(self): #метод апдейт для передвижения
        keys_pressed = key.get_pressed() #получаем все события клавиатуры
        if keys_pressed[K_UP] and self.rect.y > 0: #если нажата клавиша "a" и координаты больше нуля
            self.rect.y -= self.speed  #то плеер передвигается влево
        if keys_pressed[K_DOWN] and self.rect.y < 630: #если нажата клавиша "d" и координаты игрока меньше 630 
            self.rect.y += self.speed #то игрок передвигается в право
Lraketka = Player('raketka.png', 50, 100, 5, 50, 300)
Rraketka = Player('raketka.png', 600, 100, 5, 50, 300)
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0, 0))
    Lraketka.reset()
    Rraketka.reset()
    Lraketka.update_l()
    Rraketka.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
