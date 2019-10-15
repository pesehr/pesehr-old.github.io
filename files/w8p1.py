

ROWS = 6
COLUMNS = 10

def draw_row(columns, space):
    for i in range(0,(columns - space)//2):
        print("*",end = '')
    for i in range(0,space):
        print(" ",end = '')
    for i in range(0,(columns- space)//2):
        print("*",end = '')
    print('')

for i in range(0,ROWS+1):
    if i == 0 or i == ROWS:
        draw_row(COLUMNS,0)
    else:
        draw_row(COLUMNS,8)

