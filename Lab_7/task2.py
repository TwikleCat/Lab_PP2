import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = r"C:\Users\Artemida\Desktop\Аида\PP2\Lab_7"  

songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]
song_index = 0


pygame.font.init()
font = pygame.font.Font(None, 30)  

def play_song():
    if songs:  
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[song_index]))
        pygame.mixer.music.play()
    else:
        print("No MP3 files found in the folder.")


def draw_text(text, x, y):
    screen.fill((0, 0, 0))  
    text_surface = font.render(text, True, (255, 255, 255))  
    screen.blit(text_surface, (x, y))
    pygame.display.flip() 


if songs:
    play_song()
else:
    print("Error: No MP3 files found!")

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Music Player")
running = True

while running:
    draw_text(f"Now playing: {songs[song_index]}", 20, 130)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")

            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                print("Stopped")
                
            elif event.key == pygame.K_n:  
                if songs:
                    song_index = (song_index + 1) % len(songs)
                    play_song()
                
            elif event.key == pygame.K_b:  
                if songs:
                    song_index = (song_index - 1) % len(songs)
                    play_song()

pygame.quit()