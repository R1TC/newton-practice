# Function:
def f_x(x):
    """
    Function definition

    Parameters
    ----------
    x : numerical value to compute in the function

    Returns
    -------
    f(x) : numerical value
        Numerical value of the function evaluated at the input parameter x
    """
    result = x**2 - 2 * x + 1
    return result


# Approximate first derivative
def D1_x(x, epsilon=0.001):
    """
    Approximation of the first derivative of the function defined in f_x,
    f'(x)=f(x+epsilon)-f(x)/epsilon

    Parameters
    ----------
    x : numerical value to compute in the function
    epsilon: numerical value
        increment used to compute the derivative

    Returns
    -------
    D1_x : numerical value
        Numerical value of the first derivative of the function evaluated at the input parameter x
    """
    result = (f_x(x + epsilon) - f_x(x)) / epsilon
    return result


# Approximate second derivative
def D2_x(x, epsilon=0.001):
    """
    Approximation of the second derivative of the function defined in f_x,
    f''(x)=f'(x+epsilon)-f'(x)/epsilon

    Parameters
    ----------
    x : numerical value to compute in the function
    epsilon: numerical value
        increment used to compute the derivative

    Returns
    -------
    D2_x : numerical value
        Numerical value of the second derivative of the function evaluated at the input parameter x
    """
    result = (D1_x(x + epsilon) - D1_x(x)) / epsilon
    return result


# Newton method : tol= Newton method tolerance, epsilon: derivative approximation epsilon
def N_M(x_0, tol, epsilon):
    """
    Newton's method to obtain the root of the function defined in f_x

    Parameters
    ----------
    x_0 : numerical value
        Initial guess of the root, used for newton's method
    tol: numerical value
        threshold value at which the iteration will stop
    epsilon: numerical value
        increment used to compute the derivative


    Returns
    -------
    x_t : numerical value
        Numerical value of the approximated root
    """
    difference = 1
    x_t_1 = x_0
    count = 0
    while difference > tol:
        x_t = x_t_1 - (D1_x(x_t_1, epsilon)) / (D2_x(x_t_1, epsilon))
        difference = abs(x_t - x_t_1)
        count += 1
        if count == 100:
            print("Loop finished after break.")
            break
    else:
        print("Loop finished normally.")
    return x_t


N_M(2, 0.1, 0.1)
