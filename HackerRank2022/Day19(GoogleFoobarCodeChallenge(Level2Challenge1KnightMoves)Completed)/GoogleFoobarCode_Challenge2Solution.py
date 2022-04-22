from itertools import product


def knight_moves(position1, position2):
    x, y = position1, position2
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]
    return moves


def solution(src, dest):
    board_dict = {}
    spots = range(64)
    values = [(x, y) for x in range(8) for y in range(8)]
    for i in spots:
        board_dict[i] = values[i]
    src_cartesian = board_dict[src]
    dest_cartesian = board_dict[dest]
    if src_cartesian == dest_cartesian:
        return 0
    moves = knight_moves(src_cartesian[0], src_cartesian[1])
    if dest_cartesian in moves:
        return 1
    move_count = 0
    list_of_checked_new_moves = []
    while dest_cartesian not in moves:
        move_count += 1
        print(move_count)
        moves.extend(list_of_checked_new_moves)
        list_of_checked_new_moves = []
        for j in moves:
            new_moves = knight_moves(j[0], j[1])
            for k in new_moves:
                if k not in moves:
                    list_of_checked_new_moves.append(k)
            if dest_cartesian in list_of_checked_new_moves:
                break
    return move_count
