'''
    Created on March 14.2020
    @author: Yueyi Gao
'''
def _create(parms):
    result = {}
    
    # size
    if not ('size' in parms):
        size = 8
    elif (parms['size'] == ""):
        result['status'] = 'error: size is null'
        return result
    elif (parms['size'].isdigit() == False):
        result['status'] = 'error: size is not integer'
        return result
    else:
        size = int(parms['size'])
        if (size > 16):
            result['status'] = 'error: size is above bound'
            return result
        elif (size <= 5):
            result['status'] = 'error: size is below bound'
            return result
        elif(size % 2 == 1):
            result['status'] = 'error: size is odd'
            return result
        
    # light
    if not ('light' in parms):
        light = 1
    elif (parms['light'] == ""):
        result['status'] = 'error: light is null'
        return result
    elif (is_number(parms['light']) == False):
        result['status'] = 'error: light is not integer'
        return result
    else:
        light = int(parms['light'])
        if (light >= 10):
            result['status'] = 'error: light is above bound'
        elif (light <= -1):
            result['status'] = 'error: light is below bound'
            
    # dark  
    if not ('dark' in parms):
        dark = 2
    elif (parms['dark'] == ""):
        result['status'] = 'error: dark is null'
        return result
    elif (is_number(parms['dark']) == False):
        result['status'] = 'error: dark is not integer'
        return result
    else:
        dark = int(parms['dark'])
        if (dark >= 10):
            result['status'] = 'error: dark is above bound'
        elif (dark <= -1):
            result['status'] = 'error: dark is below bound'
            
    # blank 
    if not ('blank' in parms):
        blank = 0
    elif (parms['blank'] == ""):
        result['status'] = 'error: blank is null'
        return result
    elif (is_number(parms['blank']) == False):
        result['status'] = 'error: blank is not integer'
        return result
    else:
        blank = int(parms['blank'])
        if (blank >= 10):
            result['status'] = 'error: blank is above bound'
        elif (blank <= -1):
            result['status'] = 'error: blank is below bound'
            
    # light = dark
    # light = blank 
    # dark = blank
    if(light == dark):
        result['status'] = 'error: light is equal to dark'
        return result
    elif(light == blank):
        result['status'] = 'error: light is equal to blank'
        return result
    elif(dark == blank):
        result['status'] = 'error: dark is equal to blank'
        return result
    
    # Normal situation
    if (light < 10 and light > -1 and dark < 10 and dark > -1 and blank < 10 and blank > -1 and size < 17 and size > 5):    
        board = [([blank] * size) for i in range(size)]
        board[size//2 - 1][size//2 - 1] = light
        board[size//2][size//2] = light
        board[size//2 - 1][size//2] = dark
        board[size//2][size//2 - 1] = dark
        board = eval('['+str(board).replace(' ','').replace('[','').replace(']','')+']')
        
        tokens = {'light':light, 'dark':dark, 'blank':blank}
        
        integrity = ''
        for i in range(len(board)):
            integrity = integrity + str(board[i])
        integrity = integrity + '/' + str(light) +'/'+ str(dark) +'/'+ str(blank) +'/'+ str(dark)
        import hashlib
        integrity = hashlib.sha256(integrity.encode()).hexdigest()
        
        result['board'] = board
        result['tokens'] = tokens
        result['status'] = 'ok'
        result['integrity'] = integrity
    return result

# Justify integer
def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return float(s).is_integer()

