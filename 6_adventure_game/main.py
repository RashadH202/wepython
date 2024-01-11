print("welcome to treasure island")

print("your mission is to find the mystical bear!")
bear = '''
       _ 
      (\\  _                      ___
     .-"`"(\\                _.""`   `"-.
    /      ` `-._        _.-"            `\__
   6   6)        `-.__.-'                    `",
  /                                         `;-`
 /     ,                                     |
()    /  /`                                  |
 `---`"~``\                                  |
           \                                 |
            \            \      /           /
            /`,   ,      |     |           /
           /   "-.|      |     |         /'
          /     / |     /,__   |       /`\
     jgs /    /'  |    /    `"'\      (   \
      __/   /'    |   |         `\     \   \
      \    /      |   |           `\    \   \
       `-,/      /    |            /     |-"`
                `"""^^^           `^^""""`
'''
choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right".').lower()

if choice1 == "left" : 
   choice2 = input('you\'ve came to a lake. there is an island in the middle of the lake. Type "wait" or "right"\n').lower()
   if choice2 == "wait":
    choice3 = input('there is an island in the middle of the lake. Type "wait", "run across the lake", or "run along the shore line"?\n').lower()
    if choice3 == "run across the lake":
       print("when you enter the water you hear the roar of the bear in the distance as you made your way to the island. you turn and see the bear in the distances.\n" + bear)
    elif choice3 == "run along the shore line":
       print("the bear creeps up, and bites your arm off")
    elif choice3 == "wait" :
       print("the bear lets off a roar and scares the life out of you and you die of a heart attack.")
   else:
        print("sorry the bear snuk up and knocked you out")
else:
  print("Sorry you got mauled")