# Function:
def f_x(x):
    result = x**2-2*x+1
    return result

# Approximate first derivative
def D1_x(x,epsilon=0.001):
    result = (f_x(x+epsilon)-f_x(x))/epsilon
    return result

# Approximate second derivative
def D2_x(x,epsilon=0.001):
    result = (D1_x(x+epsilon)-D1_x(x))/epsilon
    return result

# Newton method : tol= Newton method tolerance, epsilon: derivative approximation epsilon
def N_M(x_0,tol,epsilon):
    difference = 1
    x_t_1 = x_0
    count=0
    while difference > tol:
        x_t = x_t_1 - (D1_x(x_t_1,epsilon))/(D2_x(x_t_1,epsilon))
        difference = abs(x_t-x_t_1)
        count += 1 
        if count == 100:
            print("Loop finished after break.")
            break
    else:
        print("Loop finished normally.")
    return x_t

N_M(2,0.1,0.1)