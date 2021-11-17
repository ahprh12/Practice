grid = [
    [7,5,3,1,5],
    [9,1,4,1,4],
    [3,40,30,10,60]
    ]

startx, starty = 2,0
finishx, finishy = 0,4

def travel(startx,starty,finishx,finishy,grid):
    
    curx = startx
    cury = starty
    done = False
    
    while not done:
        
        print("(" + str(curx) + "," + str(cury) + ") - " + str(grid[curx][cury]))
        
        if (curx == finishx) and (cury == finishy):
            print("Done!")
            break

        upx = curx - 1
        upy = cury

        rightx = curx
        righty = cury + 1
        
        
        uprocks = grid[upx][upy] if upx >= 0 else -1
        rightrocks = grid[rightx][righty] if righty < len(grid[rightx]) else -1
        
        if (uprocks > -1) and (rightrocks > -1):
            
            # default go up if values are equal
            curx = upx if uprocks >= rightrocks else rightx
            cury = upy if uprocks >= rightrocks else righty
            
        elif uprocks < 0:
            
            if rightrocks > -1:
                print("here?")
                curx, cury = rightx, righty
        else: 
            print("or here?")
            curx, cury = upx, upy

travel(startx,starty,finishx,finishy,grid)

'''
Note: You can only travel either north (up) or east (right)

- start and end x y
- get grid dimensions

4 functions for moving:

    - checkUp (is the value above higher?)
        - then moveUp (update current position to above coord)
    - checkRight (is the value to the right higher?)
        -  then moveRight (update current position to coord to the right)
    
x coord can only be x-1
y coord can only be y+1

flow up/right:
1) Check if I am at finish coords
2)
    - else check if element exists
    - if not, check if other direction exists and update coords
3) if both exist, do a compare of each coords values
    - update coords of greater value
4) Repeat 

'''