def check_bal(input: str) -> bool:
    
    # lh = left hand, rh = right hand
    # w = wing, p = parenthesis, s = square

    lhw, lhs, lhp = '{', '[', '('
    rhw, rhs, rhp = '}', ']', ')'

    balanced = True
    wcount, scount, pcount = 0, 0, 0

    for char in input:
        if char == lhw:
            wcount = wcount + 1
        elif char == lhs:
            scount = scount + 1
        elif char == lhp:
            pcount = pcount + 1
        elif char == rhw:
            wcount = wcount - 1
            if wcount < 0:
                balanced = False
                break
        elif char == rhs:
            scount = scount - 1
            if scount < 0:
                balanced = False
                break
        elif char == rhp:
            pcount = pcount - 1
            if pcount < 0:
               balanced = False
               break

    if wcount != 0 or scount != 0 or pcount != 0:
        balanced = False 
    
    return balanced

if __name__ == '__main__':
       result = check_bal('[{}{}()]')
       print(result)