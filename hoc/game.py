

#around 4 code
put()
turn_left()
turn_left()
move()
while True:
    if front_is_clear():
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
        move()
    else:
        turn_left()
        turn_left()
    if object_here():
        done()