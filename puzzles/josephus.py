"""
November 17, 2021

Holy shit I actually got this after a couple hours, stay confident in your thinking! Even if it takes extra time, trust yourself! :) Very proud of myself!

Problem: https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
You can run this code in https://app.coderpad.io/sandbox


1 2 3 4 5
  X
  
1 3 4 5
    X

1 3 5
X

3 5
  X
  
3 - Survives

which data structure?
list? [1,2,3,4,5]

dictionary?
{
1: "",
2: "",
3: "",
4: "",
5: "",
}


YES USE THIS - circular linked list?

if value is "Dead" - skip but dont count against k
iterate by k and update value for key to "Dead"

"""

# Node class to create Linked List
class Node:
    
    def __init__(self, id=None):
        self.id = id
        self.nextval = None

    def getNextNode(self):
        return self.nextval
    
# End of Linked List Class

    
# Function to create linked list
def makeDeathList(totalPeople):
    
    deathlist = []
    
    # create first player by default
    initialPlayer = Node(0)
    deathlist.append(initialPlayer)
    
    # populate deathlist and link Nodes
    for n in range(totalPeople):
        
        if n == (totalPeople-1):
            deathlist[n].nextval = initialPlayer
            break

        player = Node(n+1)
        deathlist.append(player)
        deathlist[n].nextval = player
        

    # testing to check the list
    '''
    for player in deathlist:
        print(str(player.id) + " " + str(player.getNextNode().id))
    '''
    
    return deathlist


# the actual logic
def russia(totalPeople: int, k: int):

    deathlist = makeDeathList(totalPeople)
    
    complete = False
    currentPlayer = deathlist[0]

    while not complete:
        
        # move k-1 positions forward
        for skipPlayer in range(k-1):
            currentPlayer = currentPlayer.getNextNode()
        
        # kill
        kill =  currentPlayer.getNextNode()
        print("Dead: " + str(kill.id))
        currentPlayer.nextval = kill.getNextNode()
        deathlist.remove(kill)
        
        if len(deathlist) == 1:
            complete = True
    
    return "The survivor is ..." + str(currentPlayer.id)

#print(russia(5, 2))
#print(russia(7, 3))
#print(russia(14, 2))
print(russia(47, 5))