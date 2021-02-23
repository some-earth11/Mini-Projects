import pafy 
  
url = input("Enter Video URL: ")
video = pafy.new(url) 
       
best = video.getbest()   #gets_the_best_resolution_possible_regardless_of_format
best.download() 