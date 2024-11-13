import sympy


# define exp
def exp():
    var_x = sympy.symbols("var_x")
    return var_x * var_x, var_x


# calculate symbol diff
def cal_grad(exp, var_x):
    return sympy.diff(exp, var_x)


# naive grad descent
def grad_descent(exp, var_x, learning_rate, initial_location, max_times=100):
    current_location = initial_location
    current_grad = cal_grad(exp, var_x).subs(var_x, current_location)
    grad_count = 0
    while current_grad != 0 and grad_count != max_times:
        # print(current_grad)
        grads_dict[current_location] = current_grad
        current_location = current_location - learning_rate * current_grad
        current_grad = cal_grad(exp, var_x).subs(var_x, current_location)
        grad_count += 1
    if current_location < -999999 or current_location > 999999:
        print("the function doesn't converge.")
        return None
    return current_location


exp, var_x = exp()
# print(cal_grad(exp, var_x).subs(var_x, 1))
grads_dict = {}
min_value_pos = grad_descent(exp, var_x, 0.1, 10, 100)
if (min_value_pos != None):
    min_value = exp.subs(var_x, min_value_pos)
    print(f"minvalue is: {min_value}")