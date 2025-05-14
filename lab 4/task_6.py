
board_size = int(input())

k_x, k_y = map(int, input().split())


move_directions = [
    (-1, -1), (-1, 0), (-1, 1),   
    (0, -1),           (0, 1),    
    (1, -1),  (1, 0),  (1, 1)    
]

possible_moves = []


for x, y in move_directions:
    new_x = k_x + x
    new_y = k_y + y
    

    if 1 <= new_x <= board_size and 1 <= new_y <= board_size:
        possible_moves.append((new_x, new_y))


possible_moves.sort()

print(len(possible_moves))  

for x, y in possible_moves:
    print(f"{x} {y}")