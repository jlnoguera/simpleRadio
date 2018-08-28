import vlc
import time

#player = vlc.MediaPlayer("sample.mp3")
player = vlc.MediaPlayer("http://live.radiovoz.es/mp3/stream_coruna.mp3")


player.play()


time.sleep(50)



