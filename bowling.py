def score(game):
    result = 0
    frame = 1
    first_roll = True
    for i in range(len(game)):
        if game[i] == '/' and frame < 10:
            result += 10 - get_value(game[i-1]) + get_value(game[i+1])           
        elif game[i].upper() == "X" and frame < 10:
            result += get_value(game[i]) + get_value(game[i+1])
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])
            else:
                result += get_value(game[i+2])
        else:
            result += get_value(game[i]) 
        if first_roll is True:
            first_roll = False
        else:
            first_roll = True
            frame += 1
        if game[i].upper() == 'X':
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

print(score("x34----------------"))