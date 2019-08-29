def cell_check(section):
    '''
    Run the game of life rules at a 3x3 section to compute
    the middle cell
    '''
    # neighbor counter
    neighbors = 0
    # reference to the center of the section
    center = section[1][1]

    # sums all elements of the section
    for row in section:
        for cell in row:
            neighbors += cell

    # remove the center cell value to get only the
    # neighbor count
    neighbors -= center

    # applying the game of life rules
    # see that rule number two isn't effectively
    # applied since it doesn't change the state of the center cell
    if neighbors <= 1:
        # less than two neighbors, the cell dies of underpopulation
        center = 0
    elif neighbors == 3:
        # exactly three neighbors, the cell is born by reproduction
        center = 1
    elif neighbors >= 4:
        # more than three neighbors, the cell dies of overpopulation
        center = 0

    # returns the center cell value
    return center


def get_section(matrix, row, col):
    '''
    Extracts a 3x3 section from the plane given
    the center cell coordinate
    '''
    # builds an empty 3x3 section to make the plane section copy
    section = [[0 for _ in range(3)] for _ in range(3)]

    # runs through the plane section copying its values
    for sec_r, r in enumerate(range(row-1, row+2)):
        for sec_c, c in enumerate(range(col-1, col+2)):
            if r >= 0 and c >= 0 and r < 50 and c < 50:
                section[sec_r][sec_c] = matrix[r][c]

    # returns the copied 3x3 section
    return section


def game_of_life(seed):
    '''
    Receives the 50x50 plane seed, runs the game of life rules
    and returns the next generation
    '''
    # creates an empty plane to store the new generation
    # we don't mutate the seed to prevent side effects
    next_gen = [[0 for _ in range(50)] for _ in range(50)]

    # walks through the plane computing the next generation
    # of each cell
    for r, row in enumerate(seed):
        for c, col in enumerate(row):
            next_gen[r][c] = cell_check(get_section(seed, r, c))

    # returns the next generation
    return next_gen
