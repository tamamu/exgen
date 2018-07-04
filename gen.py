
# coding: utf-8

# In[122]:


from sympy import *
import random
from math import floor
init_printing()


# In[123]:


def s_rational():
    return Rational(random.randint(1, 10), random.randint(2, 10))


# In[124]:


def s_sum(x):
    from sympy.abc import i, n
    return Sum(x, (i, 1, n))


# In[125]:


def s_prod(x):
    from sympy.abc import i, n
    return Product(x, (i, 1, n))


# In[162]:


def s_num():
    return random.randint(2, 10)


# In[176]:


def s_fn():
    s = random.randint(0,1)
    if s == 0:
        return Function('f')
    if s == 1:
        return Function('g')


# In[404]:


def s_value(stop=3, lv=0):
    from sympy.abc import e, a, b
    lv = lv+1
    s = random.randint(0, 14)
    if s == 0: # number
        return s_num()
    elif s == 1: # epsilon
        return exp(s_num())
    elif s == 2: # lg (log_2)
        return log(2, s_value(lv=lv)) if lv<stop else log(2, s_num())
    elif s == 3: # ln (log_e)
        return log(s_value(lv=lv)) if lv<stop else log(s_num())
    elif s == 4: # rational
        return s_rational()
    elif s == 5: # tan
        return tan(s_value(lv=lv)) if lv<stop else tan(s_num())
    elif s == 6: # sin
        return sin(s_value(lv=lv)) if lv<stop else sin(s_num())
    elif s == 7: # cos
        return cos(s_value(lv=lv)) if lv<stop else cos(s_num())
    elif s == 8: # root
        return root(s_value(lv=lv), 2) if lv<stop else root(s_num(), 2)
    elif s == 9: # f(a, b)
        return Function('h')(a, b)
    elif s == 10: # f(a)
        return s_fn()(a)
    elif s == 11: # f(b)
        return s_fn()(b)
    elif s == 12: # a
        return a**random.randint(1, 4)
    elif s == 13: # b
        return b**random.randint(1, 4)
    elif s == 14: # pi
        return pi


# In[405]:


def s_expr():
    while True:
        expr = s_value()
        if 'a' in str(expr) or 'b' in str(expr):
            break
    n = random.randint(0, 3)
    for i in range(n):
        s = random.randint(0,1)
        if s == 0:
            expr = expr * s_value()
        elif s == 1:
            expr = expr + s_value()
    return expr


# In[434]:



from IPython.display import display, Math
count = 0
expr_list = []
while count <= 10:
    expr = s_expr()
    try:
        d = diff(expr)
        expr_list.append(expr)
        count += 1
    except Exception:
        continue

print("""\subsection*{Differentiate following formulas:}
\\begin{enumerate}
""")
for i, expr in enumerate(expr_list, start=1):
    #display(Math("({})\ \ ".format(i)+latex(expr)))
    print("\item $"+latex(expr)+"$")
print("\end{enumerate}")

print("""\subsection*{Answers:}
\\begin{enumerate}""")
for i, expr in enumerate(expr_list, start=1):
    #display(Math("({})\ \ ".format(i)+latex(diff(expr))))
    print("\item $"+latex(diff(expr))+"$")
print("\end{enumerate}")
