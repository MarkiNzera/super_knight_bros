import pygame
from settings import Settings
from sprites import *

class Game:
    def __init__(self, settings):
        self.settings = settings
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Super Knight Bros')
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(self.settings.font_name)
        self.load_data()
        self.load_maps()
        self.player = Player(self)

        self.win_level1 = False
        self.win_level2 = False
        self.win_level3 = False

        self.image1_lvl1 = pygame.image.load('images/cenario/level1/BG1.png').convert_alpha()
        self.image2_lvl1 = pygame.image.load('images/cenario/level1/BG2.png').convert_alpha()
        self.image3_lvl1 = pygame.image.load('images/cenario/level1/BG3.png').convert_alpha()
        self.image1_lvl1 = pygame.transform.scale(self.image1_lvl1, (self.settings.screen_width, self.settings.screen_height))           
        self.image2_lvl1 = pygame.transform.scale(self.image2_lvl1, (self.settings.screen_width, self.settings.screen_height))       
        self.image3_lvl1 = pygame.transform.scale(self.image3_lvl1, (self.settings.screen_width, self.settings.screen_height))

        self.image1_lvl2 = pygame.image.load('images/cenario/level2/BG1.png').convert_alpha()
        self.image2_lvl2 = pygame.image.load('images/cenario/level2/BG2.png').convert_alpha()
        self.image3_lvl2 = pygame.image.load('images/cenario/level2/BG3.png').convert_alpha()
        self.image1_lvl2 = pygame.transform.scale(self.image1_lvl2, (self.settings.screen_width, self.settings.screen_height))           
        self.image2_lvl2 = pygame.transform.scale(self.image2_lvl2, (self.settings.screen_width, self.settings.screen_height))       
        self.image3_lvl2 = pygame.transform.scale(self.image3_lvl2, (self.settings.screen_width, self.settings.screen_height))

        self.image1_lvl3 = pygame.image.load('images/cenario/level3/BG1.png').convert_alpha()
        self.image2_lvl3 = pygame.image.load('images/cenario/level3/BG2.png').convert_alpha()
        self.image1_lvl3 = pygame.transform.scale(self.image1_lvl3, (self.settings.screen_width, self.settings.screen_height))           
        self.image2_lvl3 = pygame.transform.scale(self.image2_lvl3, (self.settings.screen_width, self.settings.screen_height))

    def level1(self):

        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.load('sounds/music_level_1.wav')
        pygame.mixer.music.play(-1)

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.solo_enemies = pygame.sprite.Group()
        self.flying_enemies = pygame.sprite.Group()
        self.invisible_wall = pygame.sprite.Group()
        self.invisible_wall2 = pygame.sprite.Group()
        self.player.pos = (self.settings.screen_width/2, self.settings.screen_height/2)
        self.all_sprites.add(self.player)
        for row, tiles in enumerate(self.tilemap1):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    p = Platform1(col, row, self, 1)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '2':
                    p = Platform1(col, row, self, 2)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '3':
                    p = Platform1(col, row, self, 3)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '4':
                    p = Platform1(col, row, self, 4)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '5':
                    p = Platform1(col, row, self, 5)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '6':
                    p = Platform1(col, row, self, 6)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '#':
                    p = InvisibleWall(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == ';':
                    p = InvisibleWall2(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall2.add(p)

                elif tile == 'C':
                    p = Chest(col, row, self, 0)
                    self.all_sprites.add(p)
                    self.chests.add(p)
                elif tile == 'c':
                    p = Coin(col, row, self)
                    self.all_sprites.add(p)
                    self.coins.add(p)

                elif tile == 'P':
                    p = Enemy1(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'G':
                    p = Enemy2(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'V':
                    p = Enemy3V(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'H':
                    p = Enemy3H(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                
        self.run()

    def level2(self):
        
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.load('sounds/music_level_2.wav')
        pygame.mixer.music.play(-1)

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.solo_enemies = pygame.sprite.Group()
        self.flying_enemies = pygame.sprite.Group()
        self.invisible_wall = pygame.sprite.Group()
        self.invisible_wall2 = pygame.sprite.Group()
        self.player.pos = (self.settings.screen_width/2, self.settings.screen_height/2)
        self.all_sprites.add(self.player)
        for row, tiles in enumerate(self.tilemap2):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    p = Platform2(col, row, self, 1)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '2':
                    p = Platform2(col, row, self, 2)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '3':
                    p = Platform2(col, row, self, 3)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '4':
                    p = Platform2(col, row, self, 4)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '5':
                    p = Platform2(col, row, self, 5)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '6':
                    p = Platform2(col, row, self, 6)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '7':
                    p = Platform2(col, row, self, 7)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '8':
                    p = Platform2(col, row, self, 8)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '9':
                    p = Platform2(col, row, self, 9)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '/':
                    p = Platform2(col, row, self, 10)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '-':
                    p = Platform2(col, row, self, 11)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '\\':
                    p = Platform2(col, row, self, 12)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '#':
                    p = InvisibleWall(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == ';':
                    p = InvisibleWall2(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall2.add(p)
                elif tile == 'w':
                    p = Water1(col, row, self, 3)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == 'o':
                    p = Water1(col, row, self, 1)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == 's':
                    p = Water1(col, row, self, 2)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == 'C':
                    p = Chest(col, row, self, 1)
                    self.all_sprites.add(p)
                    self.chests.add(p)
                elif tile == 'c':
                    p = Coin(col, row, self)
                    self.all_sprites.add(p)
                    self.coins.add(p)

                elif tile == 'P':
                    p = Enemy1(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'G':
                    p = Enemy2(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'V':
                    p = Enemy3V(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'H':
                    p = Enemy3H(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                
        self.run()

    def level3(self):

        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.load('sounds/music_level_3.wav')
        pygame.mixer.music.play(-1)

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.solo_enemies = pygame.sprite.Group()
        self.flying_enemies = pygame.sprite.Group()
        self.invisible_wall = pygame.sprite.Group()
        self.invisible_wall2 = pygame.sprite.Group()
        self.player.pos = (self.settings.screen_width/2, self.settings.screen_height/2)
        self.all_sprites.add(self.player)
        for row, tiles in enumerate(self.tilemap3):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    p = Platform3(col, row, self, 1)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '2':
                    p = Platform3(col, row, self, 2)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '3':
                    p = Platform3(col, row, self, 3)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '4':
                    p = Platform3(col, row, self, 4)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '5':
                    p = Platform3(col, row, self, 5)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '6':
                    p = Platform3(col, row, self, 6)
                    self.all_sprites.add(p)
                    self.platforms.add(p)
                elif tile == '#':
                    p = InvisibleWall(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall.add(p)
                elif tile == ';':
                    p = InvisibleWall2(col, row, self)
                    self.all_sprites.add(p)
                    self.invisible_wall2.add(p)
                 
                elif tile == 'C':
                    p = Chest(col, row, self, 2)
                    self.all_sprites.add(p)
                    self.chests.add(p)
                elif tile == 'c':
                    p = Coin(col, row, self)
                    self.all_sprites.add(p)
                    self.coins.add(p)
                
                elif tile == 'P':
                    p = Enemy1(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'G':
                    p = Enemy2(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'V':
                    p = Enemy3V(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                elif tile == 'H':
                    p = Enemy3H(col, row, self)
                    self.all_sprites.add(p)
                    self.enemies.add(p)
                
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.settings.fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        hits_chest = pygame.sprite.spritecollide(self.player, self.chests, False)
        if self.player.vel.y > 0:
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                self.player.jumping = False
        
        if self.player.rect.right > self.settings.screen_width - 340:
            self.player.pos.x -= abs(self.player.vel.x) + 0.5
            for plat in self.platforms:
                plat.rect.right -= abs(self.player.vel.x ) 
            
            for chest in self.chests:
                chest.rect.right -= abs(self.player.vel.x)


            for coin in self.coins:
                coin.rect.right -= abs(self.player.vel.x)

            for wall in self.invisible_wall:
                wall.rect.right -= abs(self.player.vel.x)
            
            for wall in self.invisible_wall2:
                wall.rect.right -= abs(self.player.vel.x)

            for enemy in self.enemies:
                enemy.pos.x -= abs(self.player.vel.x) + 1   

        hits_player_inv_wall = pygame.sprite.spritecollide(self.player, self.invisible_wall2, False)
        if hits_player_inv_wall:
            self.player.pos.x = hits_player_inv_wall[0].rect.top
            self.player.vel.x = 0

        for enemy in self.enemies:
            enemies_hits = pygame.sprite.spritecollide(enemy, self.platforms, False) # inimigo-plataforma
            hits_enemy = enemy.rect.colliderect(self.player.rect) # heroi-inimigo
            hit_invisible_wall = pygame.sprite.spritecollide(enemy, self.invisible_wall, False)
            if enemies_hits:
                enemy.pos.y = enemies_hits[0].rect.top + 1
                enemy.vel.y = 0

            if hit_invisible_wall:
                enemy.vel.x *= -1
                if enemy.vel.x > 0:
                    enemy.pos.x += 20
                    enemy.left = False
                    enemy.right = True
                if enemy.vel.x < 0:
                    enemy.pos.x -= 20
                    enemy.right = False
                    enemy.left = True

            if hits_enemy:
                if self.player.vel.y > 0:
                    self.player.jump()
                    enemy.kill()
                    self.player.coins += 5

                if self.player.vel.y == 0:
                    self.damage_sound.play()
                    if self.player.hearts > 0:
                        self.player.hearts -= 1
                        if self.player.vel.x > 0:
                            enemy.pos.x += 60
                            self.player.pos.x -= 60
                        elif self.player.vel.x < 0:
                            enemy.pos.x -= 60
                            self.player.pos.x += 60
                    else:
                        pygame.mixer.music.stop()
                        self.game_over_sound.play()
                        self.player.coins = 0
                        self.playing = False
                        self.player.hearts = 3
                        self.win_level1 = False
                        self.win_level2 = False
                        self.win_level3 = False

        for coin in self.coins:
            hit_coin = self.player.rect.colliderect(coin.rect)
            if hit_coin:
                coin.kill()
                self.coin_sound.play()
                self.player.coins += 1    
        
        if self.player.rect.left < 0:
            self.player.acc.x = 0
            self.player.vel.x = 0
        
        if self.player.rect.top > self.settings.screen_height:
            self.playing = False
            self.player.coins = 0
            self.player.hearts -= 1
            pygame.mixer.music.stop()
            if self.player.hearts <= 0:
                self.game_over_sound.play()
                self.player.coins = 0
                self.playing = False
                self.player.hearts = 3
                self.win_level1 = False
                self.win_level2 = False
                self.win_level3 = False
        
        if hits_chest:
            self.playing = False
            self.chest_sound.play()
            pygame.mixer.music.stop()
            self.course_clear_sound.play()
            if not self.win_level1:
                self.win_level1 = True
            elif self.win_level1 and not self.win_level2:
                self.win_level2 = True
            elif self.win_level2 and not self.win_level3:
                self.win_level3 = True
        
        if self.player.coins > 50:
            self.one_up_sound.play()
            self.player.hearts += 1
            self.player.coins -= 50

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                self.player.current_frame = 0
                if event.key == pygame.K_SPACE:
                    self.walking = False
                    self.player.jump()

                if event.key == pygame.K_a:
                    self.player.left = True
                    self.player.right = False
                    self.player.standing = False
                    self.player.walking = True
                    
                if event.key == pygame.K_d:
                    self.player.left = False
                    self.player.right = True
                    self.player.standing = False
                    self.player.walking = True
                
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event. key == pygame.K_d:
                    self.player.walking = False
                    self.player.standing = True
                

    def draw(self):   
        if not self.win_level1:

            self.screen.blit(self.image1_lvl1, (0, 0))
            self.screen.blit(self.image2_lvl1, (0, 0))
            self.screen.blit(self.image3_lvl1, (0, 0))
        
        elif self.win_level1 and not self.win_level2:
            self.image1_lvl2 = pygame.transform.scale(self.image1_lvl2, (self.settings.screen_width, self.settings.screen_height))           
            self.image2_lvl2 = pygame.transform.scale(self.image2_lvl2, (self.settings.screen_width, self.settings.screen_height))       
            self.image3_lvl2 = pygame.transform.scale(self.image3_lvl2, (self.settings.screen_width, self.settings.screen_height))

            self.screen.blit(self.image1_lvl2, (0, 0))
            self.screen.blit(self.image2_lvl2, (0, 0))
            self.screen.blit(self.image3_lvl2, (0, 0))
    
        elif self.win_level2 and not self.win_level3:
            self.image1_lvl3 = pygame.transform.scale(self.image1_lvl3, (self.settings.screen_width, self.settings.screen_height))           
            self.image2_lvl3 = pygame.transform.scale(self.image2_lvl3, (self.settings.screen_width, self.settings.screen_height))       

            self.screen.blit(self.image1_lvl3, (0, 0))
            self.screen.blit(self.image2_lvl3, (0, 0))

        self.all_sprites.draw(self.screen)
        self.show_score()
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.blit(self.image1_lvl1, (0, 0))
        self.screen.blit(self.image2_lvl1, (0, 0))
        self.screen.blit(self.image3_lvl1, (0, 0))
        self.draw_text('Super Knight Bros', 48, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height / 4)
        self.draw_text('Press space key to play', 22, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def show_end_level_screen(self):
        if not self.running:
            return
        self.screen.blit(self.image1_lvl1, (0, 0))
        self.screen.blit(self.image2_lvl1, (0, 0))
        self.screen.blit(self.image3_lvl1, (0, 0))
        self.draw_text("Congratulations", 48, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height / 4)
        self.draw_text("Press space key to play", 22, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.blit(self.image1_lvl1, (0, 0))
        self.screen.blit(self.image2_lvl1, (0, 0))
        self.screen.blit(self.image3_lvl1, (0, 0))
        self.draw_text("GAME OVER", 48, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height / 4)
        self.draw_text("Press space key to play", 22, (0, 0, 0), self.settings.screen_width / 2, self.settings.screen_height * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def show_score(self):
        self.draw_image_score()
        self.draw_text(f'X {self.player.coins}', 28, (0, 0, 0), 800, 20)
        if not self.win_level1:
            self.draw_text('Level 1', 28, (0, 0, 0), 416, 20)
        elif self.win_level1 and not self.win_level2:
            self.draw_text('Level 2', 28, (0, 0, 0), 416, 20)
        elif self.win_level2 and not self.win_level3:
            self.draw_text('Level 3', 28, (0, 0, 0), 416, 20)
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def draw_image_score(self):
        self.icon_coin = pygame.transform.scale(self.spritesheet_coin.get_image(0, 0, 16, 16), (32, 32))
        self.icon_coin.set_colorkey((0, 0, 0))
        self.screen.blit(self.icon_coin, (740, 20))

        self.heart_icon = pygame.transform.scale(self.spritesheet_heart.get_image(0, 0, 64, 64), (32, 32))
        self.heart_icon.set_colorkey((0, 0, 0))
        for i in range(self.player.hearts):
            self.screen.blit(self.heart_icon, (20 + 32 * i, 20))

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running == False
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                        pygame.mixer.pause()

    def load_maps(self):
        self.tilemap1 = []
        self.tilemap2 = []
        self.tilemap3 = []
        with open('level1.txt', 'rt') as f:
            for line in f:
                self.tilemap1.append(line)
            
        with open('level2.txt', 'rt') as f:
            for line in f:
                self.tilemap2.append(line)
        
        with open('level3.txt', 'rt') as f:
            for line in f:
                self.tilemap3.append(line)
        
    def load_data(self):
        self.spritesheet = Spritesheet('images/sprites/hero_spritesheet.png')
        
        self.spritesheet1 = Spritesheet('images/cenario/level1/Tileset.png')
        self.spritesheet2 = Spritesheet('images/cenario/level2/Tileset.png')
        self.spritesheet3 = Spritesheet('images/cenario/level3/Tileset.png')

        self.spritesheet_chest = Spritesheet('images/sprites/chest.png')
        self.spritesheet_coin = Spritesheet('images/sprites/coin.png')
        self.spritesheet_heart = Spritesheet('images/sprites/heart.png')

        self.spritesheet_enemy1 = Spritesheet('images/sprites/Enemy01/enemy01_sheet.png')
        self.spritesheet_enemy2 = Spritesheet('images/sprites/Enemy02/Run.png')
        self.spritesheet_enemy3 = Spritesheet('images/sprites/Enemy03/enemy03_sheet.png')

        self.coin_sound = pygame.mixer.Sound('sounds/coin_sound.wav')
        self.chest_sound = pygame.mixer.Sound('sounds/chest_sound.wav')
        self.jump_sound = pygame.mixer.Sound('sounds/jump_sound.wav')
        self.kick_sound = pygame.mixer.Sound('sounds/kick_sound.wav')
        self.one_up_sound = pygame.mixer.Sound('sounds/1_up_sound.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over_sound.wav')
        self.damage_sound = pygame.mixer.Sound('sounds/damage_sound.wav')
        self.course_clear_sound = pygame.mixer.Sound('sounds/course_clear_sound.wav')

def run():
    settings = Settings()
    game = Game(settings)
    game.show_start_screen()
    while game.running:
        if not game.win_level1:
            game.level1()
            if game.win_level1:
                game.show_end_level_screen()        
            else:
                game.show_go_screen()
        elif game.win_level1 and not game.win_level2 and game.running:       
            game.level2()
            if game.win_level2:
                game.show_end_level_screen()        
            else:
                game.show_go_screen()
        elif game.win_level2 and not game.win_level3 and game.running:   
            game.level3()
            if game.win_level3:
                game.win_level1 = False
                game.win_level2 = False
                game.win_level3 = False
                game.show_end_level_screen()   
                game.show_start_screen()     
            else:
                game.show_go_screen()


    pygame.quit()

if __name__ == "__main__":
    run()