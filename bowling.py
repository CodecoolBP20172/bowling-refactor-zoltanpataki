def score(game):
    result = 0
    frame = 1
    first_roll = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if not first_roll:
            frame += 1
        if first_roll is True:
            first_roll = False
        else:
            first_roll = True
        if game[i] == 'X' or game[i] == 'x':
            first_roll = True
            frame += 1
    return result


def get_value(char):
    if char.upper() == 'X':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    elif int(char) < 10 and int(char) > 0:
        return int(char)
    else:
        raise ValueError()

print(score(["x", "6", "/", "8", "1"]))