import pafy 

url = input("Enter Video URL: ")
video = pafy.new(url) 

bestaudio = video.getbestaudio(preftype="m4a")   #gets_the_best_audio_possible_in_m4a_format
bestaudio.download() 
