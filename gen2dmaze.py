import math, random

class cell():
    #data holder, typ = type 0 = wall 1 = block 2 = node

    def __init__(self, position, typ, id=None):
        self.position = position
        self.typ = typ
        self.id = id


def generate(width, height):
    internalwidth = width * 2 + 1
    internalheight = height * 2 + 1

    walls = genwalls(internalwidth, internalheight)
    blocks = genblocks(internalwidth, internalheight)
    cells = gencells(internalwidth, internalheight)
    newwalls = []

    while len(blocks) > 0:
        currentblock = blocks[random.randint(0, len(blocks)-1)]    
        cell1, cell2 = getneighbors(currentblock, cells)

        if cell1.id == cell2.id:
            newwalls.append(cell(currentblock.position, 0))
            blocks.remove(currentblock)
            
        else:
            oldid = cell2.id
            newid = cell1.id

            for cel in cells:
                if cel.id == oldid:
                    cel.id = newid
            
            blocks.remove(currentblock)
    
    rawoutput = []

    for cel in walls:
        rawoutput.append(cel.position)

    for cel in newwalls:
        rawoutput.append(cel.position)

    output = []

    for y in range(internalheight):
        temp = []
        for x in range(internalwidth):
            temp.append(0)
        output.append(temp)
    for position in rawoutput:
        output[position[1]][position[0]] = 1

    return(output)
            



def genwalls(width, height):
    output = []
    
    for x in range(width):
        for y in range(height):
            
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                output.append(cell((x, y), 0))

            elif x % 2 == 0 and y % 2 == 0:
                output.append(cell((x, y), 0))

    return output


def genblocks(width, height):
    output = []
    
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass
            
            elif x % 2 == 1 and y % 2 == 0:
                output.append(cell((x, y), 1))
            
            elif x % 2 == 0 and y % 2 == 1:
                output.append(cell((x,y), 1))

    return output


def gencells(width, height):
    output = []
    currentnum = 0
    
    for x in range(width):
        for y in range(height):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                pass

            elif x % 2 == 1 and y % 2 == 1:
                output.append(cell((x, y), 2, currentnum))
                currentnum += 1

    return (output)


def searchcells(x, y, cells):
    position = (x, y)
    for cel in cells:

        if cel.position == position:
            return cel

    return None

def getneighbors(currentblock, cells):
    neighborcells = []

    neighborcells.append(searchcells(currentblock.position[0], currentblock.position[1] + 1, cells))
    neighborcells.append(searchcells(currentblock.position[0], currentblock.position[1] - 1, cells))
    neighborcells.append(searchcells(currentblock.position[0] + 1, currentblock.position[1], cells))
    neighborcells.append(searchcells(currentblock.position[0] - 1, currentblock.position[1], cells))
    neighborcells.remove(None)
    neighborcells.remove(None)
        
    return(neighborcells[0], neighborcells[1])

def draw(width, height, nodes):
    output = []
    for x in range(width):
        temp = []
        for y in range(height):
            temp.append(0)
        output.append(temp)

    for node in nodes:
        output[node[0]][node[1]] = 1

    print("drawing")
    for i in output:
        print(str(i)+"\n")

def drawid(width, height, nodes):
    output = []
    for x in range(height):
        temp = []
        for y in range(width):
            temp.append(0)
        output.append(temp)

    for node in nodes:
        output[node.position[0]][node.position[1]] = node.id

    print("drawing")
    for i in output:
        print(str(i)+"\n")

if __name__ == "__main__":
    print(generate(5, 6))