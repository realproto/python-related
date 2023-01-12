# Jan 11, 2023
# Exercise pass a list to func argument - magicians 
# show_magicians( magicians[:] <-- copy of org list, picked_m)

from time import sleep
magicians = ['doug henney', 'firestone', 'zig n roy', 'david copperfield',
             'mag6', 'mag8', 'mag4', 'houdini', 'amazing randy', 'mag1', 'mag2', 'mag3' ]
picked_m = []
sleep(6) 

def show_magicians( mylist ):
    """ Display magicians. """
    for magician in mylist:
        picked = mylist.pop() #is the problem here?
        picked_m.append(magician)
    #WHY THIS ONLY PRINTS SIX? WHY STOP AT SIX?
        print(f'mylist size: {len(mylist)}, picked size: {len(picked_m)} item pick:{picked}' )
        print(picked_m)
        print(f'Picked size: {len(mylist)}')

show_magicians(magicians)
##showit = show_magicians(magicians, picked_m)
###show_magicians(magicians[:], picked_m) #is prob here? Copy of list??   
### print(magicians)
###print(picked_m)
##print(showit)

    
