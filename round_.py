# This python round() function takes two numeric arguments, a float-digit to be rounded off and the desired decimals_number 
# and returns the number rounded to the desired decimal number.
def round_(values,cut):
    from numpy import round
    if cut >0:
        Round_Final =round(values,cut)
    else:
        Round3=round(values,3)
        Round2 =round(Round3,2)
        Round1 =round(Round2,1)
        if int(str(Round1).split('.')[-1]) >= 5:
            Round_Final = int(str(Round1).split('.')[0]) +1
        else:
            Round_Final = int(str(Round1).split('.')[0]) 
    return Round_Final

values = 86.49134793661929
print(round_(values,1))
# 86.5

print(round_(values,0))
# 87
    
