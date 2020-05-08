'''
    Created on March 31.2020
    @author: Yueyi Gao
'''
import re
import math

def _status(parms):
    result = {}
    
    # light
    if not ('light' in parms):
        light = 1
    elif (parms['light'] == ''):
        result['status'] = 'error: light is null'
        return result
    elif (is_number(parms['light']) == False):
        result['status'] = 'error: light is not integer'
        return result
    else:
        light = int(parms['light'])
        if (light >= 10):
            result['status'] = 'error: light is above bound'
            return result
        elif (light <= -1):
            result['status'] = 'error: light is below bound'
            return result
    
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
            return result
        elif (dark <= -1):
            result['status'] = 'error: dark is below bound'
            return result
        
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
            return result
        elif (blank <= -1):
            result['status'] = 'error: blank is below bound'
            return result
    

    if(light == dark):
        result['status'] = 'error: light is equal to dark'
        return result
    elif(light == blank):
        result['status'] = 'error: light is equal to blank'
        return result
    elif(dark == blank):
        result['status'] = 'error: dark is equal to blank'
        return result
    
    # board
    if not ('board' in parms):
        result['status'] = 'error: board is missing'
        return result
    elif (parms['board'] == ""):
        result['status'] = 'error: board is null'
        return result 
    board_string = parms['board']
    board_1d = [int(s) for s in re.findall(r'\b\d+\b', board_string)]
    if(int(math.sqrt(len(board_1d))) != math.sqrt(len(board_1d))):
        result['status'] = 'error: board is non square'
        return result  
    size = int(math.sqrt(len(board_1d)))
    if(size % 2 == 1):
        result['status'] = 'error: board is odd'
        return result
    for i in board_1d:
        if (board_1d[i] != blank and board_1d[i] != light and board_1d[i] != dark):
            result['status'] = 'error: board'
            return result
    
    
    blank_num = 0
    
    if (light < 10 and light > -1 and dark < 10 and dark > -1 and blank < 10 and blank > -1 and size < 17 and size > 5):
        board_2d = [([0] * size) for i in range(size)]
        n = 0
        for i in range(size):
            for j in range(size):
                board_2d[i][j] = board_1d[n]
                n+=1
        
        light_check = 0
        dark_check = 0
        for i in range(size):
            for j in range(size):
                #count blank
                if(board_2d[i][j] == blank):
                    blank_num+=1
                #check light
                if(board_2d[i][j] == dark):
                    #1
                    if(i-1>=0 and j-1 >=0 and board_2d[i-1][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size and temp_j+1 < size):
                            temp_i+=1
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #2
                    if(i-1>=0 and board_2d[i-1][j] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size):
                            temp_i+=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #3
                    if(i-1>=0 and j+1 <size and board_2d[i-1][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size and temp_j-1 >= 0):
                            temp_i+=1
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #4
                    if(j-1 >=0 and board_2d[i][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_j+1 < size):
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #5
                    if(j+1 <size and board_2d[i][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_j-1 >= 0):
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #6
                    if(i+1<size and j-1 >=0 and board_2d[i+1][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0 and temp_j+1 < size):
                            temp_i-=1
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #7
                    if(i+1<size and board_2d[i+1][j] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0):
                            temp_i-=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #8
                    if(i+1<size and j+1<size and board_2d[i+1][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0 and temp_j-1 >=0):
                            temp_i-=1
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==light):
                                light_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                #check dark
                elif(board_2d[i][j] == light):
                    if(i-1>=0 and j-1 >=0 and board_2d[i-1][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size and temp_j+1 < size):
                            temp_i+=1
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #2
                    if(i-1>=0 and board_2d[i-1][j] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size):
                            temp_i+=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #3
                    if(i-1>=0 and j+1 <size and board_2d[i-1][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i+1 <size and temp_j-1 >= 0):
                            temp_i+=1
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #4
                    if(j-1 >=0 and board_2d[i][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_j+1 < size):
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #5
                    if(j+1 <size and board_2d[i][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_j-1 >= 0):
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #6
                    if(i+1<size and j-1 >=0 and board_2d[i+1][j-1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0 and temp_j+1 < size):
                            temp_i-=1
                            temp_j+=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #7
                    if(i+1<size and board_2d[i+1][j] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0):
                            temp_i-=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
                    #8
                    if(i+1<size and j+1 <size and board_2d[i+1][j+1] == blank):
                        temp_i = i
                        temp_j = j
                        while (temp_i-1 >=0 and temp_j-1 >=0):
                            temp_i-=1
                            temp_j-=1
                            if (board_2d[temp_i][temp_j]==dark):
                                dark_check = 1
                                break
                            elif (board_2d[temp_i][temp_j]==0):
                                break
        
        placed = ''
        if(light_check==1 and dark_check ==1):
            result['status'] = 'ok'
            if(blank_num % 2 == 1):
                placed = str(light)
            elif(blank_num % 2 == 0):
                placed = str(dark)     
        elif(dark_check==1 and light_check==0):
            result['status'] = 'dark'
            placed = str(dark) 
        elif(dark_check==0 and light_check==1):
            result['status'] = 'light'
            placed = str(light)
        else:
            result['status'] = 'end'
        
        # integrity
        if not ('integrity' in parms):
            result['status'] = 'error: integrity'
            return result
        elif (parms['integrity'] == ""):
            result['status'] = 'error: integrity'
            return result 
        integrity = parms['integrity'] 
        integrity_check = ''
        board_string = eval('['+board_string.replace(' ','').replace('[','').replace(']','')+']')
        for i in range(len(board_string)):
            integrity_check = integrity_check + str(board_string[i])
        integrity_check = integrity_check + '/' + str(light) +'/'+ str(dark) +'/'+ str(blank) +'/'+ placed
        import hashlib
        integrity_check = hashlib.sha256(integrity_check.encode()).hexdigest()
        if (integrity_check != integrity):
            result['status'] = 'error: integrity'
            return result  
          
    return result


# Justify integer
def is_number(s):
    if(bool(re.search('[a-z]',s))==True):
        return False
    if(bool(re.search('[A-Z]',s))==True):
        return False
    try:
        float(s)
    except ValueError:
        return False
    else:
        return float(s).is_integer()
