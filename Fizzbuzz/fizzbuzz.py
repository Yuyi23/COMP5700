def fizzbuzz(n = None):
    FIZZ_VALUE = "fizz"
    BUZZ_VALUE = "buzz"
    FIZZBUZZ_VALUE = "fizzbuzz"
    ERROR_VALUE = "Danger, Will Robinson"
    LOWER_BOUND = 1
    UPPER_BOUND = 50
    FIZZ_NUMERIC = 3
    BUZZ_NUMERIC = 5
    
    if(not(isinstance(n, int))):
        return ERROR_VALUE
    if(n < LOWER_BOUND):
        return ERROR_VALUE
    if(n > UPPER_BOUND):
        return ERROR_VALUE
    
    fizzRemainder = n % FIZZ_NUMERIC
    buzzRamainder = n % BUZZ_NUMERIC
    
    if((buzzRamainder == 0) & (fizzRemainder == 0)):
        return FIZZBUZZ_VALUE
    if(fizzRemainder == 0):
        return FIZZ_VALUE
    if(buzzRamainder == 0):
        return BUZZ_VALUE
    return str(n)
