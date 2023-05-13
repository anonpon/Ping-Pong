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
    def update(self): #метод апдейт для передвижения
        keys_pressed = key.get_pressed() #получаем все события клавиатуры
        if keys_pressed[K_a] and self.rect.x > 0: #если нажата клавиша "a" и координаты больше нуля
            self.rect.x -= self.speed  #то плеер передвигается влево
        if keys_pressed[K_d] and self.rect.x < 630: #если нажата клавиша "d" и координаты игрока меньше 630 
            self.rect.x += self.speed #то игрок передвигается в право
   
