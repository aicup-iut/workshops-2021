import random
import time
import sys
from enum import Enum


class Tile_State(Enum):
    deadzone = 0
    fire = 1
    box = 2
    wall = 3
    bomb = 4
    upgrade_range = 5
    upgrade_health = 6
    upgrade_trap = 7
    player = 8
    trap = 9
    box_broken = 10


def has_state(_state_mask, _state_to_check):
    return _state_mask & int(pow(2, _state_to_check.value))


def add_state(_state_mask, _state_to_add):
    return _state_mask | int(pow(2, _state_to_add.value))


def remove_state(_state_mask, _state_to_remove):
    return _state_mask & ~(int(pow(2, _state_to_remove.value)))


# Just a random log
print(f"Let's have fun!\n", file=sys.stderr)

# Initiation stage

# Getting initiation message from engine
init_msg = input()
# Telling the engine that we received the initiation message
print("init confirm")
# Logging the initiation message
print(f'Agent says: Initiation message received ({init_msg}).', file=sys.stderr)
# Extracting info from initiation message
height, width, x, y, health, bombRange, trapCount, vision, bombDelay, maxBombRange, dzStart, dzDelay, maxStep = map(int, init_msg.split()[
    1:])
# Logging extracted info
print(
    f'\t\t\tInitiation message contents ({height=}, {width=}, {x=}, {y=}, {health=}, {bombRange=}, {trapCount=}, {vision=}, {bombDelay=}, {maxBombRange=}, {dzStart=}, {dzDelay=}, {maxStep=}).', file=sys.stderr)

otherX = None
otherY = None
otherHealth = None
tiles = [[0 for _ in range(width)] for _ in range(height)]


# Main loop
while True:
    t = time.time()
    visibleBoxesCount = 0

    # Getting input from engine
    raw_inp = input()

    # Termination stage
    if 'term' in raw_inp:
        print(f'Agent says: Termination message received ({raw_inp}).', file=sys.stderr)
        break

    print(f'Agent says: Loop message received ({raw_inp})', file=sys.stderr)

    # Extracting info from loop message
    inp = list(map(int, raw_inp.split()[:-1]))
    stepCount, lastAction, x, y, health, healthUpgradeCount, bombRange, trapCount, isOtherPlayerInVision = inp[:9]

    tilesBaseIndex = 9
    if isOtherPlayerInVision:
        otherX = inp[9]
        otherY = inp[10]
        otherHealth = inp[11]
        tilesBaseIndex += 3

    for i in range(inp[tilesBaseIndex]):
        tileX = inp[tilesBaseIndex + (3*i) + 1]
        tileY = inp[tilesBaseIndex + (3*i) + 2]
        tileState = inp[tilesBaseIndex + (3*i) + 3]
        tiles[tileX][tileY] = tileState

        # Count the number visible boxes
        if has_state(tileState, Tile_State.box):
            visibleBoxesCount += 1

    # Logging extracted info
    print(
        f'\t\t\tLoop message contents ({(stepCount, lastAction, x, y, health, healthUpgradeCount, bombRange, trapCount, isOtherPlayerInVision, otherX, otherY, otherHealth)})', file=sys.stderr)
    print(
        f'\t\t\tTiles ({tiles})', file=sys.stderr)
    print(
        f'\t\t\t{visibleBoxesCount=}', file=sys.stderr)

    # Deciding our next move...
    # time.sleep(0.398) # Simulating a late response

    # Formulating a response
    random.seed(time.time())
    response = int(random.random()*10)

    # Logging the response
    print(f'\t\t\t\t===>{response=} (Responded in {time.time() - t} seconds)', file=sys.stderr)

    # Responding to engine
    print(f'{response}')
