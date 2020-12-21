data = []

# with open('test_small.txt', 'r') as f:
# with open('test.txt', 'r') as f:
with open('inputs/input20.txt', 'r') as f:
    data = f.read().splitlines()

import numpy as np

tiles = dict()
ident = ""
block = []
for line in data:
    if line == "":
        tiles[ident] = np.array(block)
        ident = ""
        block = []
        # append block
        continue
    if "Tile" in line:
        ident = int(line.split(" ")[1].split(":")[0])
        continue
    l = []
    for c in line:
        if c == ".":
            l.append(0)
        else:
            l.append(1)
    block.append(l)

tiles[ident] = np.array(block)

print("Parsing Done")

def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

tileSetCache = dict()

def genTileSet(tilename, tile):
    global tileSetCache
    if tilename in tileSetCache:
        return tileSetCache[tilename]
    tiles = [] 
    tiles.append(tile)
    tiles.append(np.rot90(tile, 1))
    tiles.append(np.rot90(tile, 2))
    tiles.append(np.rot90(tile, 3))
    tiles.append(np.flipud(tile))
    tiles.append(np.rot90(np.flipud(tile), 1))
    tiles.append(np.rot90(np.flipud(tile), 2))
    tiles.append(np.rot90(np.flipud(tile), 3))
    tileSetCache[tilename] = tiles
    return tiles

def solve(coordX, coordY, cubelen, solutiongrid, tiles):
    if len(tiles) == 0:
        print("Done!")
        return solutiongrid
    for tilename, tile in tiles.items():
#    tilename, tile = next(iter(tiles.items()))
        tileset = genTileSet(tilename, tile)
        solutiongrid[coordY][coordX]["id"] = tilename
        for t in tileset:
            # print("Checking Tile " + str(tilename) + " for " + str(coordY) + "," + str(coordX))
            fitX, fitY = True, True
            if coordX - 1 >= 0:
                # check, if left corner fits
                compareY = solutiongrid[coordY][coordX-1]["tile"][:, 9]
                if not np.array_equal(compareY, t[:, 0]):
                    fitX = False
            if coordY - 1 >= 0:
                # check, if top corner fits
                compareY = solutiongrid[coordY-1][coordX]["tile"][9]
                if not np.array_equal(compareY, t[0]):
                    fitX = False
            if fitX and fitY:
                solutiongrid[coordY][coordX]["tile"] = t
                nextX = (coordX + 1) % cubelen
                nextY = coordY + int((coordX+1)/cubelen)
                result = solve(nextX, nextY, cubelen, solutiongrid, without_keys(tiles, [tilename]))
                if result is not None:
                    return result

        # if "id" in solutiongrid[coordY][coordX]:
        #     solutiongrid[coordY][coordX].pop("id")
        # if "tile" in solutiongrid[coordY][coordX]:
        #     solutiongrid[coordY][coordX].pop("tile")
    # if we reach here, there is no solution:
    return None

import math
cubelen = int(math.sqrt(len(tiles)+1))
solutiongrid = [[dict() for y in range(cubelen)] for x in range(cubelen)]
solution = solve(0, 0, cubelen, solutiongrid, tiles)
if solution is None:
    print("No Solution found - stupid!")
    exit(1)

print("Got Solution!")
result = solutiongrid[0][0]["id"] * solutiongrid[cubelen-1][0]["id"] \
    * solutiongrid[0][cubelen-1]["id"] * solutiongrid[cubelen-1][cubelen-1]["id"]
print("Result is " + str(result))

# cut grid borders
for y in solutiongrid:
    for x in y:
        x["tile"] = x["tile"][1:9, 1:9]

# merge in one array
lines = []
for y in solutiongrid:
    line = None
    for x in y:
        if line is None:
            line = x["tile"]
        else:
            line = np.concatenate((line, x["tile"]), 1)
    lines.append(line)

picture = None
for line in lines:
    if picture is None:
        picture = line
    else:
        picture = np.concatenate((picture, line), 0)

pictures = genTileSet("picture", picture)

# Monster:
# 00000000000000000010
# 10000110000110000111
# 01001001001001001000

# 20*3 --> 15 Files are active
monster = np.array(\
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
    )


count = 0
wildSea = 0
for i in picture:
    for j in i:
        if j == 1:
            wildSea += 1
print("The wild sea is " + str(wildSea) + " and there are monsters in it")

monstercount = 0
for pic in pictures:
    count += 1
    for y in range(len(pic)-3):
        for x in range(len(pic)-20):
            if np.array_equal(np.multiply(monster, pic[y:y+3, x:x+20]), monster):
                monstercount += 1
                print("Found 1 in count " + str(count))

print("We have wild sea: " + str(wildSea - monstercount*15))

print("done")