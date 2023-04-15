strength = int(input())
stamina = int(input())
course = input()

hurdles_completed = 0
i = 0

while i < len(course):
    if course[i] == '|':
        if i < len(course) - 1 and course[i+1] == '|': # height of hurdle
            hurdle_height = 2
            i += 1
        elif i < len(course) - 2 and course[i+1] == '|' and course[i+2] == '|':
            hurdle_height = 3
            i += 2
        else:
            hurdle_height = 1
        
        if hurdle_height <= strength: # see if runner can jump over
            hurdles_completed += 1
            stamina -= 1
            if stamina == 0:
                break
        else:
            break
        
    i += 1

print(hurdles_completed)
