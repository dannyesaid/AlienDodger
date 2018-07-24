from initialize_game import *

#game variables
number_of_enemies =                             3
enemy_speed =                                   5
number_of_waves =                               1

#create constants for action time intervals
new_wave_interval =                             3000
throw_time_interval =                           650
difficulty_time_interval =                      5000

#create time variable for changing game variables
frames_per_second_clock =                       pygame.time.Clock()         #frames per second
hero_weapon_time =                              pygame.time.get_ticks()     #controls how often a the hero may throw a weapon
create_enemies_time =                           pygame.time.get_ticks()     #controls frequence of enemy waves
increase_difficulty_time =                      pygame.time.get_ticks()     #controls interval until difficulty is increased

#collisions ratio callable
collide_ratio =                                 pygame.sprite.collide_rect_ratio( 0.5 )

#makes  wave of enemies
def create_some_enemies( enemies_to_make ):
    #creates enemy_numbers enemies
    for alien in range( enemies_to_make ):
        #create a new enemy at a random position
        new_enemy_x =                           random.randint( screen_width // 2, screen_width - enemy_width )
        new_enemy_y =                           random.randint( 0, screen_height - 60 )
        new_enemy =                             enemy( new_enemy_x, new_enemy_y )
        #if the new enemy is in the screen or there are 32+ enemies, add the new enemy to the enemy group
        if  screen_rectangle.contains( new_enemy ) or enemies_to_make >= 32:
            enemy_group.add( new_enemy )

#start background music
pygame.mixer.music.load( 'Dependencies\\background music new.mp3' )
pygame.mixer.music.play()

#main game loop
while True:

    #for every event in the event queue
    for event in pygame.event.get():
        #if user exited
        if event.type ==                        pygame.QUIT:
            pygame.quit()
        #moves hero according to key pressed
        if event.type ==                        pygame.KEYDOWN: #if any key is pressed
            if event.key == pygame.K_RIGHT:                     #if the right arrow is pressed move the hero right
                hero.move_right()
            elif event.key ==                   pygame.K_LEFT:  #if the left arrow is pressed move the hero left
                hero.move_left()
            elif event.key ==                   pygame.K_UP:    #if the up arrow is pressed move the hero up
                hero.jump()
            elif event.key ==                   pygame.K_DOWN:  #if the down arrow is pressed move the hero down
                hero.fall()
            #if the space bar is pressed and a sufficient amout of time has passed create a new hero weapon and update the time interval
            elif event.key == pygame.K_SPACE and pygame.time.get_ticks() >= hero_weapon_time + throw_time_interval:
                fire_sound.play()
                hero_weapon_group.add( hero_weapon() )
                hero_weapon_time =              pygame.time.get_ticks()

    #if a sufficient amout of time has passed create a new wave of aliens and update the time interval
    if pygame.time.get_ticks() >= create_enemies_time + new_wave_interval:
        number_of_waves             +=          1
        create_some_enemies( number_of_enemies )
        create_enemies_time  =                  pygame.time.get_ticks()

    #if a sufficient amount of time has passed increase the difficuly of the game
    if  pygame.time.get_ticks() >=              increase_difficulty_time + difficulty_time_interval :
        number_of_enemies       +=              1   #increase the number of enemies per wave by one
        enemy_speed             +=              1   #increase the speed of the enemies by one pixel
        increase_difficulty_time =              pygame.time.get_ticks() #update the time

    #if the hero has hit any aliens fill the screen black, output the score and restart the game
    if pygame.sprite.spritecollideany( hero, enemy_group, collided = collide_ratio ):
        screen.blit( ending_image, top_left_of_screen )
        ending_text =                           pygame.font.SysFont( 'Comic Sans MS' , 70 ) #next 3 lines display surface
        ending_surface =                        ending_text.render( 'You Got To Level ' + str( number_of_waves ) + '  :D', False, white)
        screen.blit( ending_surface, top_left_of_screen )
        pygame.display.update()
        time.sleep( 6 )                         #let the gamer take it in

        #reset the game
        enemy_group.empty()
        hero_weapon_group.empty()
        hero.rect.x =                           20
        hero.rect.y =                           screen_height - 120
        number_of_enemies =                     3
        enemy_speed =                           5
        number_of_waves =                       1

    update_game( enemy_speed, number_of_waves )             #update the game

    frames_per_second_clock.tick( 30 )                      #control frames per second
