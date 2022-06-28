from settings import Settings
import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.right = True
        self.left = False

        self.standing = True
        self.walking = False
        self.jumping = False
        self.current_frame = 0

        self.coins = 0
        self.hearts = 3

        self.load_images()
        self.image = self.standing_frames_right[0]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.settings.screen_width/2, self.game.settings.screen_height/2)
        self.pos = vec(self.game.settings.screen_width/2, self.game.settings.screen_height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def load_images(self):
        self.standing_frames_right = [
            pygame.transform.scale(self.game.spritesheet.get_image(23, 24, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(87, 24, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(151, 24, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(215, 24, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(279, 24, 18, 24), (18*4, 24*4)),]

        self.standing_frames_left = [pygame.transform.flip(x, True, False) for x in self.standing_frames_right]

        self.walking_frames_right = [
            pygame.transform.scale(self.game.spritesheet.get_image(24, 87, 16, 25), (16*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(88, 87, 15, 25), (15*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(152, 87, 16, 25), (16*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(215, 87, 18, 25), (18*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(278, 87, 20, 25), (20*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(341, 87, 22, 25), (22*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(406, 87, 20, 25), (20*4, 25*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(471, 87, 18, 25), (18*4, 25*4)),]

        self.walking_frames_left = [pygame.transform.flip(x, True, False) for x in self.walking_frames_right]

        self.jumping_frames_right = [
            pygame.transform.scale(self.game.spritesheet.get_image(24, 152, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(87, 152, 18, 24), (18*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(150, 152, 18, 24), (18*4, 24*4)),

            pygame.transform.scale(self.game.spritesheet.get_image(20, 216, 24, 24), (24*4, 24*4)),
            pygame.transform.scale(self.game.spritesheet.get_image(84, 216, 23, 24), (23*4, 24*4)),
        ]

        self.jumping_frames_left = [pygame.transform.flip(x, True, False) for x in self.jumping_frames_right]

    def update(self):
        self.animate()
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            if self.rect.left > 0:
                self.acc.x -= 0.5
        if keys[pygame.K_d]:
            self.acc.x = 0.5

        self.acc.x += self.vel.x * (-0.12)
        self.vel += self.acc

        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def jump(self):
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        hits_enemy = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits or hits_enemy:
            if hits:
                self.game.jump_sound.play()
            elif hits_enemy:
                self.game.kick_sound.play()
            self.vel.y = -15
            self.jumping = True

    def animate(self):
        if self.standing:       
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.standing_frames_right):
                self.current_frame = 0

            if self.right:
                self.image = self.standing_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.standing_frames_left[int(self.current_frame)]
            
        if self.walking:
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.walking_frames_right):
                self.current_frame = 0
                
            if self.right:
                self.image = self.walking_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.walking_frames_left[int(self.current_frame)]
            
        if self.jumping:
            self.current_frame += 0.0001 

            if self.current_frame >= (len(self.jumping_frames_right) - 1):
                self.current_frame = (len(self.jumping_frames_right) - 1)
            
            if self.right:
                self.image = self.jumping_frames_right[int(self.current_frame)]
            
            if self.left:
                self.image = self.jumping_frames_left[int(self.current_frame)]
        
        self.image.set_colorkey((0, 0, 0))
        

class InvisibleWall(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize

class InvisibleWall2(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize

class Platform1(pygame.sprite.Sprite):
    def __init__(self, x, y, game, index):
        self.game = game
        self.index = index - 1
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.platforms1[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize
    
    def load_images(self):
        self.platforms1 = [
            pygame.transform.scale(self.game.spritesheet1.get_image(0, 0, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(16, 0, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(32, 0, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(0, 16, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(16, 16, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(32, 16, 16, 16), (64, 64)),

            pygame.transform.scale(self.game.spritesheet1.get_image(48, 0, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet1.get_image(64, 0, 16, 16), (64, 64)),]

class Platform2(pygame.sprite.Sprite):
    def __init__(self, x, y, game, index):
        self.game = game
        self.index = index - 1
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.platforms2[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize

    def load_images(self):
        self.platforms2 = [
            pygame.transform.scale(self.game.spritesheet2.get_image(192, 112, 16, 16), (64, 64)), 
            pygame.transform.scale(self.game.spritesheet2.get_image(208, 112, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(224, 112, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(192, 128, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(208, 128, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(224, 128, 16, 16), (64, 64)),
            # caveira
            pygame.transform.scale(self.game.spritesheet2.get_image(288, 128, 16, 16), (64, 64)),
            # border
            pygame.transform.scale(self.game.spritesheet2.get_image(256, 96, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(272, 96, 16, 16), (64, 64)),
            # bridge
            pygame.transform.scale(self.game.spritesheet2.get_image(128, 192, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(144, 192, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(192, 192, 16, 16), (64, 64)),

            ]

class Platform3(pygame.sprite.Sprite):
    def __init__(self, x, y, game, index):
        self.game = game
        self.index = index - 1
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.platforms3[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize
    
    def load_images(self):
        self.platforms3 = [
            pygame.transform.scale(self.game.spritesheet3.get_image(16, 32, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet3.get_image(32, 32, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet3.get_image(48, 32, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet3.get_image(16, 48, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet3.get_image(32, 48, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet3.get_image(48, 48, 16, 16), (64, 64)),]

class Water1(pygame.sprite.Sprite):
    def __init__(self, x, y, game, index):
        self.game = game
        self.index = index - 1
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.Water[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize

    def load_images(self):
        self.Water = [
            pygame.transform.scale(self.game.spritesheet2.get_image(320, 112, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(336, 112, 16, 16), (64, 64)),
            pygame.transform.scale(self.game.spritesheet2.get_image(320, 128, 16, 16), (64, 64)),
        ]

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y, game, index):
        self.game = game
        self.index = index
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.image = self.chests[self.index]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize + 18

    def load_images(self):
        self.chests = [
            pygame.transform.scale(self.game.spritesheet_chest.get_image(292, 68, 23, 23), (46, 46)),
            pygame.transform.scale(self.game.spritesheet_chest.get_image(36, 68, 23, 23), (46, 46)),
            pygame.transform.scale(self.game.spritesheet_chest.get_image(4, 68, 23, 23), (46, 46)),
        ]

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(self.game.spritesheet_coin.get_image(0, 0, 16, 16), (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize
        self.current_frame = 0
        self.load_images()
    def load_images(self):
        self.coins_frames = [
            pygame.transform.scale(self.game.spritesheet_coin.get_image(0, 0, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(16, 0, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(32, 0, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(0, 16, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(16, 16, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(32, 16, 16, 16), (32, 32)),
            pygame.transform.scale(self.game.spritesheet_coin.get_image(0, 32, 16, 16), (32, 32)),]
    
    def update(self):
        self.animate()

    def animate(self):     
        self.current_frame += 0.12
        if self.current_frame > len(self.coins_frames):
            self.current_frame = 0
        
        self.image = self.coins_frames[int(self.current_frame)]
        self.image.set_colorkey((0, 0, 0))

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.right = True
        self.left = False

        self.standing = False
        self.walking = True
        self.attacking = False

        self.image = pygame.transform.scale(self.game.spritesheet_enemy1.get_image(0, 16, 48, 48), (48*3, 48*3))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize
        self.current_frame = 0
        self.load_images()

        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(3, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames_right = [
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(0, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(64, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(128, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(192, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(256, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(320, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(384, 16, 48, 48), (48*3, 48*3)),]
        
        self.standing_frames_left = [pygame.transform.flip(x, True, False) for x in self.standing_frames_right]

        self.walking_frames_right = [
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(448, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(512, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(576, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(640, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(704, 16, 48, 48), (48*3, 48*3)),
            pygame.transform.scale(self.game.spritesheet_enemy1.get_image(768, 16, 48, 48), (48*3, 48*3)),
        ]

        self.walking_frames_left = [x.set_colorkey((255, 255, 255)) for x in self.walking_frames_right]

        self.walking_frames_left = [pygame.transform.flip(x, True, False) for x in self.walking_frames_right]

    def update(self):
        self.animate()
        self.acc = vec(0, 0.5)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def animate(self):
        if self.standing:       
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.standing_frames_right):
                self.current_frame = 0

            if self.right:
                self.image = self.standing_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.standing_frames_left[int(self.current_frame)]
            
        if self.walking:
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.walking_frames_right):
                self.current_frame = 0
                
            if self.right:
                self.image = self.walking_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.walking_frames_left[int(self.current_frame)]

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.right = True
        self.left = False

        self.standing = False
        self.walking = True
        self.attacking = False

        self.image = pygame.transform.scale(self.game.spritesheet_enemy2.get_image(48, 0, 47, 37), (47*3, 37*3))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize 
        self.current_frame = 0
        self.load_images()

        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(6, 0)
        self.acc = vec(0, 0.5)

    def load_images(self):
        self.walking_frames_right = [
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(0, 0, 47, 37), (47*3, 37*3)),
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(48, 0, 47, 37), (47*3, 37*3)),
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(96, 0, 47, 37), (47*3, 37*3)),
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(144, 0, 47, 37), (47*3, 37*3)),
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(192, 0, 47, 37), (47*3, 37*3)),
            pygame.transform.scale(self.game.spritesheet_enemy2.get_image(240, 0, 47, 37), (47*3, 37*3)),
        ]

        self.walking_frames_left = [x.set_colorkey((0, 0, 0)) for x in self.walking_frames_right]

        self.walking_frames_left = [pygame.transform.flip(x, True, False) for x in self.walking_frames_right]
    
    def update(self):
        self.animate()
        self.acc = vec(0, 0.5)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def animate(self):
        if self.standing:       
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.standing_frames_right):
                self.current_frame = 0

            if self.right:
                self.image = self.standing_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.standing_frames_left[int(self.current_frame)]
            
        if self.walking:
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.walking_frames_right):
                self.current_frame = 0
                
            if self.right:
                self.image = self.walking_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.walking_frames_left[int(self.current_frame)]

class Enemy3V(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.right = True
        self.left = False

        self.standing = False
        self.walking = True
        self.attacking = False

        self.image = pygame.transform.scale(self.game.spritesheet_enemy3.get_image(0, 0, 48, 32), (48*3, 32*3))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize
        self.current_frame = 0
        self.load_images()

        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(0, 3)

    def load_images(self):
        self.walking_frames_right = [
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(0, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(48, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(96, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(144, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(196, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(240, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(288, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(336, 0, 48, 32), (48*3, 32*3)),
        ]

        self.walking_frames_left = [x.set_colorkey((0, 0, 0)) for x in self.walking_frames_right]

        self.walking_frames_left = [pygame.transform.flip(x, True, False) for x in self.walking_frames_right]
    
    def update(self):
        self.animate()
        self.acc = vec(0, 0)
        hit_invisible_wall = pygame.sprite.spritecollide(self, self.game.invisible_wall, False)
        if hit_invisible_wall:
            self.vel.y *= -1
            if self.vel.y > 0:
                self.left = False
                self.right = True
            elif self.vel.y < 0:
                self.right = False
                self.left = True
        self.pos += self.vel

        self.rect.midbottom = self.pos

    def animate(self):
        if self.standing:       
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.standing_frames_right):
                self.current_frame = 0

            if self.right:
                self.image = self.standing_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.standing_frames_left[int(self.current_frame)]
            
        if self.walking:
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.walking_frames_right):
                self.current_frame = 0
                
            if self.right:
                self.image = self.walking_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.walking_frames_left[int(self.current_frame)]

class Enemy3H(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)

        self.right = False
        self.left = True

        self.standing = False
        self.walking = True
        self.attacking = False

        self.image = pygame.transform.scale(self.game.spritesheet_enemy3.get_image(0, 0, 48, 32), (48*3, 32*3))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.game.settings.tilesize
        self.rect.y = y * self.game.settings.tilesize + 100
        self.current_frame = 0
        self.load_images()

        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(-3, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.walking_frames_right = [
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(0, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(48, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(96, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(144, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(196, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(240, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(288, 0, 48, 32), (48*3, 32*3)),
            pygame.transform.scale(self.game.spritesheet_enemy3.get_image(336, 0, 48, 32), (48*3, 32*3)),
        ]

        self.walking_frames_left = [x.set_colorkey((0, 0, 0)) for x in self.walking_frames_right]

        self.walking_frames_left = [pygame.transform.flip(x, True, False) for x in self.walking_frames_right]
    
    def update(self):
        self.animate()
        self.acc = vec(0, 0)
        hit_invisible_wall = pygame.sprite.spritecollide(self, self.game.invisible_wall, False)
        if hit_invisible_wall:
            self.vel.x *= -1
            if self.vel.x > 0:
                self.rect.y = hit_invisible_wall[0].rect.top - 60
                self.left = False
                self.right = True
            if self.vel.x < 0:
                self.rect.y = hit_invisible_wall[0].rect.bottom + 60
                self.right = False
                self.left = True
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def animate(self):
        if self.standing:       
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.standing_frames_right):
                self.current_frame = 0

            if self.right:
                self.image = self.standing_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.standing_frames_left[int(self.current_frame)]
            
        if self.walking:
            self.current_frame += 0.12
            
            if self.current_frame >= len(self.walking_frames_right):
                self.current_frame = 0
                
            if self.right:
                self.image = self.walking_frames_right[int(self.current_frame)]
            
            if self.left:               
                self.image = self.walking_frames_left[int(self.current_frame)]

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image

    
