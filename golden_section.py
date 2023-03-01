import math 

R = (math.sqrt(5) - 1) * 0.5

def f(x):
    return (1.0 - x)**2 + x

def monotonicity(x1,y1,x2,y2):
    slop = (y2-y1)/(x2-x1)
    if slop >0: return 1
    elif slop <0: return -1
    else: return 0

def golden_section_min(a,b,f,delta):
    start = a
    end = b
    while start < end:
        d = start + R*(end-start)
        c = end - R*(end-start)
        is_increasing = monotonicity(c,f(c), d,f(d))
        if is_increasing == 1:
            end = d
        elif is_increasing == -1:
            start = c
        else:
            return d
    return start + R*(end-start)
    
def g(x):
    return (x-10)**2 + 10

            
x = golden_section_min(0.0, 24.0, g, 0.001); 
print("optimum is "+str(x)+", function value is " +str(g(x)))