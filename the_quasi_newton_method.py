import numpy as np
import math

#plot 
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
ON_PLOT = True
if ON_PLOT:
    steps = []

gr = (math.sqrt(5)-1)/2
def f(x):
    return pow(x[0],2) + pow(x[1],2) +x[0] +2*x[1]

def gradient(f,X,h):
    #df has the same length(size) as vector X
    df = np.zeros(X.size)
    func = f
    #i mean dimention, axis
    for i in range(X.size):
        #difference at point x_i
        #a1, a2 is a vector like X,
        #only differentiate at one axis i, and keep other axis orinal point
        a1 = X.copy()
        a2 = X.copy()
        a1[i] = X[i] - h
        a2[i] = X[i] + h
        df[i] = ( func(a2) - func(a1) )/(2*h)
    return df

#min f(x_k + t*p_k),
def golden_section_line_search(a,b,f,L):
    x = a
    y = b
    while y-x>2*L:
        d = x + gr*(y-x)
        c = y - gr*(y-x)
        if f(d)>f(c):
            y = d
        else:
            x = c
    return (x+y)/2
def t_min(x,p):
    t_func = lambda t: f(x + t * p)
    t = golden_section_line_search(0.0, 24, t_func, 0.001)
    return t

#DFP main function, 
#sk = x_{k+1} - x_k
#yk = g_{k+1} - g_k
#use np.dot 
def delta_dk(yk, sk, dk):
    d = ( np.dot(sk,sk.T)/np.dot(sk.T,yk) )- \
        np.dot(np.dot(np.dot(dk, yk), yk.T),dk)/np.dot(np.dot(yk.T, dk) ,yk)
    return d
    
#x_k is current point
def DFP(f,xk):
    epsilon, h, maxiter = 10**-5, 10**-5, 10**3
    #D will eventualy approach to Hessian Matrix of function f(x)
    dk = np.eye(np.size(xk))
    for _ in range(maxiter):
        # df = partial derivative of function at vector X
        df = gradient(f,xk,h)
        #gk = np.matrix([df]).T
        #if the norm of current grandient smaller than epsilon
        if np.linalg.norm(df) < epsilon:
            return xk        
        #pk is vector = -gk when dk is identity but, dk will change
        pk = -np.dot(dk,df)
        t = t_min(xk,pk)
        #t = linesearch(f, xk, pk)
        xk1 = xk + pk*t
        #optimize the xk1 
        df1 = gradient(f, xk1,h)
        #gk1 = np.matrix([df1]).T  
        if np.linalg.norm(df1) < epsilon:
            return xk1
        #yk = g_{k+1} - g_k
        yk = df1 - df
        sk = xk1 - xk
        dk1 = dk + delta_dk(yk,sk,dk)
        #iterate next 
        dk = dk1
        xk = xk1
        if ON_PLOT:
            steps.append(list(xk))   
    return xk   
x0 = np.array([0.0,0.0])
print(DFP(f,x0) )

def plot_2d_steps(steps,start):
    myvec = np.array([start]+steps).transpose()
    #print(myvec)
    plt.plot(myvec[0,],myvec[1,],'ro')
    for label,x,y in zip([str(i) for i in range(len(steps)+1)],myvec[0,],myvec[1,]):
        plt.annotate(label,xy = (x, y))
    return plt

if ON_PLOT:
    print(np.size(steps))
    plot_2d_steps(steps,x0).show()
    