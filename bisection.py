

def f(x):
    return (1.0 - x)**2 + x
def g(x):
    return 1- 0.01*(x**2) + 0.01*x

def monotonicity(f, x1,delta):
    #lim([f(x1) - f(x1-delta)]/delta ) when delta->0, 
    #if the limit greater than 0 then the function is increse,
    y = (f(x1)-f(x1-delta) ) / delta
    if y > 0: return 1          #function increasing 
    elif y == 0: return 0       #because delta!=0, so it is unlikely; function will find extremum point, 
    else: return -1             #function decreasing

"""
To Find the optimal 
param: a is start point of the function
param: b is end point of the function
"""
def bisection_find_min(a,b,f,delta):
    start = a
    end = b
    while start < end:
        mid = (start+end)/2
        is_increasing = monotonicity(f,mid,delta)
        if is_increasing== 1: 
            end = mid+delta
        elif is_increasing == -1:
            start = mid-delta
        else:
            return mid
    return (start+end)/2

def bisection_find_max(a,b,f,delta):
    start = a
    end = b
    while start < end:
        mid = (start+end)/2
        is_increasing = monotonicity(f,mid,delta)
        if is_increasing== 1: 
            start = mid+delta
        elif is_increasing == -1:
            end = mid-delta
        else:
            return mid
    return (start+end)/2

def recur_bisection_min(a,b,f,delta):
    start = a
    end = b
    mid = (start+end)/2
    is_increasing = monotonicity(f,mid,delta)

    if is_increasing == 1: 
        end = mid+delta
        return recur_bisection_min(start,end,f,delta)
    elif is_increasing == -1:
        start = mid-delta
        return recur_bisection_min(start,end,f,delta)
    else:
        return mid

def recur_bisection_max(a,b,f,delta):
    start = a
    end = b
    mid = (start+end)/2
    is_increasing = monotonicity(f,mid,delta)

    if is_increasing == 1: 
        start = mid+delta
        return recur_bisection_max(start,end,f,delta)
    elif is_increasing == -1:
        end = mid-delta
        return recur_bisection_max(start,end,f,delta)
    else:
        return mid
        
            
x = bisection_find_max(0.0, 5.0, f,0.001); 
print("optimum is "+str(x)+", function value is " +str(f(x)))