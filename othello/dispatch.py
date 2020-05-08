import othello.create as create
import othello.status as status
import othello.place as place
import othello.next as next

ERROR01 = 'error: no op is specified'
ERROR02 = 'error: parameter is not a dictionary'
ERROR03 = 'error: op is not legal'
STATUS = 'status'
OP = 'op'
OPS = {
    'create' : create._create,
    'status' : status._status,
    'place' : place._place,
    'next' : next._next,
    }

def _dispatch(parms = None):

    result = {}
    
    # Validate parm
    if(parms == None):
        result = {STATUS: ERROR01}
    elif(not(isinstance(parms, dict))):
        result = {STATUS: ERROR02}
    elif (not(OP in parms)):
        result = {STATUS: ERROR01}
    elif(not(parms[OP] in OPS)):
        result[STATUS] = ERROR03
    else:
        result = OPS[parms[OP]](parms)
    return result
