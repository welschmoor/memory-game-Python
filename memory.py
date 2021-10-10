# #################################
#   Memory
#   Johannes Welsch
#   10 October 2021
#   install and import simplegui to get it working
#   Or use codeskulptor.org, paste the code there and voila it is working
#
#   Took me almost 2 hours to get it working. I failed with lists (arrays)
#   Then used a dict and it was easy breezy
#
#   The game features numbers (overturned cards), you click on them, they
#   turn over, if they match, they stay open... well that's Memory for you.
#
###################################
import simplegui
import random


cardlist = [
    {"id":"1a",  "number":1,  "show":False,  "matched":False },
    {"id":"1b",  "number":1,  "show":False,  "matched":False },
    {"id":"2a",  "number":2,  "show":False,  "matched":False },
    {"id":"2b",  "number":2,  "show":False,  "matched":False },
    {"id":"3a",  "number":3,  "show":False,  "matched":False },
    {"id":"3b",  "number":3,  "show":False,  "matched":False },
    {"id":"4a",  "number":4,  "show":False,  "matched":False },
    {"id":"4b",  "number":4,  "show":False,  "matched":False },
    {"id":"5a",  "number":5,  "show":False,  "matched":False },
    {"id":"5b",  "number":5,  "show":False,  "matched":False },
    {"id":"6a",  "number":6,  "show":False,  "matched":False },
    {"id":"6b",  "number":6,  "show":False,  "matched":False },
]

opened_cardlist = []

score = 0
moves = 1

# If the first card is open, we set first to True, the if second, we set it also to True
game_state = {"first":False, "second": False}



def new_game():
    global moves, score, opened_cardlist, game_state, cardlist
    random.shuffle(cardlist)
    increment = 0
    for each in cardlist:
        each["position"] = increment
        increment += 50
        each["show"] = False
    opened_cardlist = []
    score = 0
    moves = 1
    print('moves reset')
    game_state = {"first":False, "second": False}
    
     
def mouseclick(pos):   
    global opened_cardlist, score, game_state, moves
    print(moves)
    # if both cards are opened, set them to closed if they are not a match. Reset opened_cardlist
    if game_state["first"] and game_state["second"]:
        game_state["first"] = False
        game_state["second"] = False
        opened_cardlist = []
        for each in cardlist:
            if each["matched"] == False:
                 each["show"] = False
            else:
                each["show"] = True
           

    
       
    index = 0
    for each in cardlist:
        if pos[0] > each["position"] and pos[0] <= each["position"]+50:
            if each["show"] == True: return
            moves += 1
            each["show"] = True
            if game_state["first"]:
                game_state["second"] = True # if first opened, then second is opened too.
            game_state["first"] = True	# first card opened
            opened_cardlist.append(each)
    #print(opened_cardlist)
    
    # if we opened two and they match, we mutate list to have property matched
    if len(opened_cardlist) == 2 and opened_cardlist[0]["number"]==opened_cardlist[1]["number"]:
        print('match!')
        score += 1
        print(score)
        for each in cardlist:
            if each == opened_cardlist[0] or each == opened_cardlist[1]:
                each['matched'] = True
        opened_cardlist = []

        
    print(opened_cardlist)
    
          
  






                        
  
def draw(canvas):
    increment = 50
    
    for each in cardlist:
        
        canvas.draw_text(str(each['number']), (each["position"], 84), 100, 'grey')
       
        if each["matched"] == True:
            each["show"] == True
        if each["show"] == False:
            canvas.draw_polygon([(each["position"], 0), (each["position"]+50, 0),(each["position"]+50, 100), (each["position"], 100)], 3, 'grey', 'Green')
       
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(moves))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric