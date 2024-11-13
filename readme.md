# 食用指南
> 仅作参考，推荐自己实现
## 模块化
代码做了高度解耦，你只需要修改`exp`和一些`hyperparameters`就可以看到直观的效果

例如你可以修改下面代码的返回值来得到你想要的函数表达式
```python
# define exp
def exp():
    var_x = sympy.symbols("var_x")
    return var_x * var_x - 1, var_x
```
当然你也可以修改初始位置和学习率以及梯度下降次数来查看程序运行结果的不同
```python
def grad_descent(exp, var_x, learning_rate, initial_location, max_times=100):
```
## 健壮性
代码的健壮性不够完美但是足够用
```python
if current_location < -999999 or current_location > 999999:
    print("the function doesn't converge.")
    return None
```

## 代码优化方向
当前函数的定义域 $R$，对于某些函数（比如 $y=x^3$ ）我们无法找到最值。

可以为函数设定一个区间，这样就可以求取最值了。

good luck!