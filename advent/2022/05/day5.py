import ctools
def main():
    data = ctools.wopen("day5.d")
    raw_boxes, raw_instructions = [i.split("\n") for i in data.split("\n\n")]
    # boxes = raw_boxes.split("\n")
    # instructions = raw_instructions.split("\n")
    box_position = []
    # watched a youtube video for inspiration, can't find it as of 8/20/23
    for x, i in enumerate(raw_boxes[-1]):
        try:
            if int(i):
                box_position.append((int(i), x))
        except:
            # print("err")
            continue
    # print(box_position)
    box_setup = {}
    for place, _ in box_position:
        box_setup[place] = []
    for box in raw_boxes[:-1]:
        ### This outputs the letters for the last position, 9. Weird.
        for place, position in box_position:
            if box[position]:
                box_setup[place] += [box[position]]
                # print(type(place))
            try:
                pass 
                # print("")
            except:
                box_setup[place] = []
    for i in box_setup:
        clean_stack = [x for x in box_setup[i] if x != ' '][::-1]
        box_setup[i] = clean_stack
    
    ### instructions
    
    moves = []
    for instruction in raw_instructions:
        parts_of_instruct = instruction.strip().split(" ")
        # print(instruction, parts_of_instruct)
        # moves = [i for i in instruction.split(" ") if type(i) == int]
        part_of_move = []
        for part in parts_of_instruct:
            # print(part)
            try:
                part_of_move.append(int(part))
            except:
                pass
        moves.append(part_of_move)

    for move in moves:
        if len(move) == 3:
            many = move[0]
            origin = move[1]
            to = move[2]
            origin_list = box_setup[origin]
            to_list = box_setup[to]
            for _ in range(many):
                to_list.append(origin_list.pop())

            box_setup[origin] = origin_list
            box_setup[to] = to_list
    part_1 = ''
    for i in box_setup:
        # print(box_setup[i][-1])
        part_1 += box_setup[i][-1]
    print(part_1)

    ### PART 2
    box_setup = {}
    for place, _ in box_position:
        box_setup[place] = []
    for box in raw_boxes[:-1]:
        ### This outputs the letters for the last position, 9. Weird.
        for place, position in box_position:
            if box[position]:
                box_setup[place] += [box[position]]
                # print(type(place))
            try:
                pass 
                # print("")
            except:
                box_setup[place] = []
    for i in box_setup:
        clean_stack = [x for x in box_setup[i] if x != ' '][::-1]
        box_setup[i] = clean_stack

    for move in moves:
        if len(move) == 3:
            many = move[0]
            origin = move[1]
            to = move[2]
            origin_list = box_setup[origin]
            to_list = box_setup[to]
            # CHATGPT help
            # grab everything but the last 'many'
            keep = origin_list[:-many]
            # grab only the last 'many'
            send = origin_list[-many:]

            new_to_list = to_list + send

            box_setup[origin] = keep
            box_setup[to] = new_to_list
    part_2 = ''
    for i in box_setup:
        # print(box_setup[i][-1])
        part_2 += box_setup[i][-1]
    print(part_2)

    # print(moves)
    
    # for i in range(1,9):
        # box_setup = [x for x in box_setup[str(i)] if x != ' ']

    # print(box_setup, type(box_setup))
    # print(raw_boxes)
    # print(box_setup)
    print("success")
if __name__ == "__main__":
    main()

