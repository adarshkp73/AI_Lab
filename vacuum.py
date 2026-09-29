import random

room = [] #two rooms

print("enter status of room a and room b; 0 is clean 1 is dirty")

room += [int(input())]
room += [int(input())]

vacuum_loc = random.randint(0, 1)
print("vacuum is currently in", chr(vacuum_loc+65))

score = 0

while(True):
    if(room[vacuum_loc]==1):
        print("Room", chr(vacuum_loc+65), "is dirty")
        #vacuum suck operation
        print("sucked room", chr(vacuum_loc+65))
        room[vacuum_loc] = 0
        #move to left or right
        vacuum_loc = -1*(vacuum_loc-1)
        print("moving to room", chr(vacuum_loc+65))
        score+=1
    elif(room[vacuum_loc]==0):
        print("Room", chr(vacuum_loc+65), "is already clean")
        vacuum_loc = -1*(vacuum_loc-1)
        print("Moving to room", chr(vacuum_loc+65))
    if(sum(room) == 0):
        break

print(room)
print("both rooms are clean")
print("Perfomance score is", score)
