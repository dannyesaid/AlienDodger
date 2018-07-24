
import pygame, random, time

pygame.init()

#enemy class
class enemy( pygame.sprite.Sprite ):
    def __init__( self, left, top ):
        pygame.sprite.Sprite.__init__( self )
        self.image =            enemy_image
        self.rect =             self.image.get_rect()
        self.rect.x =           left
        self.rect.y =           top

#Hero Class
class hero_class( pygame.sprite.Sprite ):
    def __init__( self, left, top ):
        pygame.sprite.Sprite.__init__( self )
        self.image = hero_image
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top
    #Hero controls
    def move_left( self ):
        self.rect.x              -= 35
    def move_right( self ):
        self.rect.x              += 35
    def jump( self ):
        self.rect.y              -= 35
    def fall ( self ):
        self.rect.y              += 35

#Hero weapon class
class hero_weapon( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image =            hero_weapon_image
        self.rect =             self.image.get_rect()
        self.rect.x =           hero.rect.x + ( hero_width // 2 )
        self.rect.y =           hero.rect.y + ( hero_height // 2 )

def update_hero_weapons():
    #animates the hero weapons
    for hero_throw in hero_weapon_group:
        hero_throw.rect.x              +=  20
    #check if any are outside the screen, if so remove it
        if not screen_rectangle.contains( hero_throw.rect ):
            hero_weapon_group.remove( hero_throw )

def move_enemies( speed ):
    #moves the enemies speed pixels to the right. Then check if the enemy is still in the screen, if not remove it
    for alien in enemy_group:
        alien.rect.x    -= speed
    #check any enemy is outside the screen, remove it
        if not screen_rectangle.contains( alien.rect ):
            enemy_group.remove( alien )

def correct_out_of_screen_hero():
    #keeps hero in the screen
    if hero.rect.right      >    screen_rectangle.right:
        hero.rect.right     =    screen_rectangle.right
    elif hero.rect.left     <    screen_rectangle.left:
        hero.rect.left      =    screen_rectangle.left
    elif hero.rect.top      <    screen_rectangle.top:
        hero.rect.top       =    screen_rectangle.top
    elif hero.rect.bottom   >    screen_rectangle.bottom:
        hero.rect.bottom    =    screen_rectangle.bottom

def update_time( waves ):
    #updates time/score record
    time_text =                  pygame.font.SysFont( 'Comic Sans MS' , 20 )
    text_surface =               time_text.render( str( waves ), False, white)
    screen.blit( text_surface, top_left_of_screen )

#updates the game
def update_game( speed_to_move_enemies, wave_numbers ):


    screen.blit( background, top_left_of_screen )          #draw the background
    enemy_group.draw( screen )                            #draw the enemies
    update_hero_weapons()                                 #move the hero weapons
    hero_weapon_group.draw( screen )                      #draw the hero weapons
    move_enemies( speed_to_move_enemies )                 #update the enemies
    pygame.sprite.groupcollide( enemy_group, hero_weapon_group, True, True )    #account for collisions between hero weapons and enemies
    correct_out_of_screen_hero()                          #make sure the hero is in the screen
    screen.blit( hero.image, hero.rect )                  #draw the hero
    update_time( wave_numbers )                           #update the time tracker
    pygame.display.update()                               #update the screen


#colors
white =                         ( 255, 255, 255 )
black =                         ( 0,    0,   0  )

#initialize the screen and syntactical sugar for screen
monitor_info =                  pygame.display.Info()
screen_width =                  monitor_info.current_w // 2
screen_height =                 monitor_info.current_h // 2
screen =                        pygame.display.set_mode( ( screen_width, screen_height ) )
screen_rectangle =              screen.get_rect()
top_left_of_screen =            ( 0, 0 )

#create background and ending image
background =                    pygame.image.load( 'Dependencies\\background two.jpg' )
background =                    pygame.transform.scale( background, ( screen_width, screen_height ) )
ending_image =                  pygame.image.load( 'Dependencies\\ending image.jpg' )
ending_image =                  pygame.transform.scale( ending_image, ( screen_width, screen_height ) )

#enemy
enemy_width =                   screen_width // 8
enemy_height =                  screen_height // 8
enemy_image_original =          pygame.image.load( 'Dependencies\\enemy.png' )
enemy_image =                   pygame.transform.scale( enemy_image_original, ( enemy_width, enemy_height  ) )
enemy_group =                   pygame.sprite.Group()

#hero
hero_image_original =           pygame.image.load( 'Dependencies\\hero.png' )
hero_width =                    screen_width // 8
hero_height =                   screen_height // 8
hero_image =                    pygame.transform.scale( hero_image_original, ( hero_width, hero_height ) )
hero =                          hero_class( 20, screen_height - 120 ) #actual hero

#hero weapon
hero_weapon_image_original =    pygame.image.load( 'Dependencies\\hero weapon.png' )
hero_weapon_image =             pygame.transform.scale( hero_weapon_image_original, ( screen_width // 15, screen_height // 15 ) )
hero_weapon_group =             pygame.sprite.Group()

#sound effects
fire_sound =                    pygame.mixer.Sound( 'Dependencies\\shot.ogg' )
fire_sound.set_volume( 1.0 )

#set pygame key repeat setting
pygame.key.set_repeat( 300, 30 )
