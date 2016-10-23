

def test_one():
    p = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
    x, y = 0, 0
    strength = 2
    result = [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]
    return p, x, y, strength, result

def test_two():
    p = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
    x, y = 2, 1
    strength = 5
    result = [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
    return p, x, y, strength, result

def test_three():
    p = [[5,4,3,6,5,10], [9,7,15,16,5,3], [2,1,0,11,19,18], [19,1,13,8,6,15], [11,7,17,4,12,9], [18,3,12,14,2,16]]
    x, y = 3,3
    strength = 20
    result = [[-1]*6]*6
    return p, x, y, strength, result

def test_four():
    p = [[999]*25]*25
    x,y = 0, 0
    strength = 999
    result = [[-1]*25]*25
    return p, x, y, strength, result

def test_five():
    p = []
    x,y = 0, 0
    strength = 999
    result = []
    return p, x, y, strength, result

def test_six():
    p = [[],[],[]]
    x,y = 0, 0
    strength = 999
    result = p
    return p, x, y, strength, result

def test_seven():
    p = [range(8)]*4
    x,y = 0, 0
    strength = 999
    result = [[-1]*8]*4
    return p, x, y, strength, result

def test_eight():
    p = [range(4)]*8
    x,y = 0, 0
    strength = 999
    result = [[-1]*4]*8
    return p, x, y, strength, result