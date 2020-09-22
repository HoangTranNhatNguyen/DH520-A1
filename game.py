Psuedo Code
# import libraries
# this function allows us to exit python (error handling)
from sys import exit
#this allows us to randomly select something
from random import randint
#Dedent allows text to wrap naturally, not the way spec. in python
from textwrap import dedent

#define scenes and self 
class Scene (object):
  def enter(self):
      exit(1)
      
#set up the engine, I set this one up to use while, not for. 
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            #print out the last scene
        current_scene.enter()



# This class sets up the start of the game  
class The_Setup(Scene):
    def enter(self):
        print(dedent("""
            You are grocery shopping in a pandemic. Things don't go the way you expect. You need a mask, the store is out of lots of things, and there are killer bees. 
            """)
              Print("Let's start with some information about you")
Print("What's your name: \n")
name = input
Print("What's your favourite food?: \n")
food = input
Print(f "Ok {name}, you like {food}. Let's go grocery shoppping." )

 #this class checks for a mask, if yes, can proceed into store              
  class The_Entrance(Scene): 
     def enter(self): 
         print("Do you have a mask?") 
     #if yes, go to the store scene, if not, go to killer_Hornets scene 
              
 
  #this class checks to see if you are trying to buy groceries the store is out of 
    class The_Store(Scene): 
        def enter(self):
              print("Are you trying to buy flour, yeast, toilet paper or lysol?" 
       if yes, then go to random_koans scene, if no, go to line up scene 
                    
                    
  #this class is the line up
    class The_Lineup(Scene): 
        def enter(self): 
            print("How long can you wait in line? Your answer must be between 1 and 60 minutes") 
            Generate a random int between 1 and 60, if their answer is longer than this int, go to success scene  
                    if their answer is not longer than the random int, go to failure scene 
                    
  #this class is the failure condition 
     class Failure(Scene):
         def enter(self):
            print("Looks like 2020 ruined your grocery plans. Skip the Dishes again?") 
                    
                    
 #this class is the success condition 
       class Success(Scene): 
           def enter(self): 
              print("Hey, you got groceries. You can eat this week!") 
 
                    
 #this class is the killer-hornets scene 
       class Killer_Hornets(Scene): 
          def enter(self): 
              print(dedent("""
              Uh oh. Are those killer hornets? 
              Those are killer hornets. 
              BZZZZzzzzz. 
              ARGGGGHHHHHHH 
              Sorry . . . 
              """)
# this class is the koan-scene.
       class Koan_Scene(Scene):
           def enter(self): 
               koans = [
        "Out of yeast the mind comes forth."
        "Question: What is joy? Answer: Three pounds of all purpose flour."
        "Maybe you are searching among the toiletpaper for what only appears //in the roots"
        "When you meet the lysol, kill the germs."
    ]
    def enter(self):
        print(Ennui.koans[radint(0, len(self.koans)-1)])
        exit(1)
