
# coding: utf-8

# In[43]:

import math
list1 = [1550, 1700, 900, 850, 1000, 950]
Var = 0
Average = sum(list1)/len(list1)
for i in list1:
    Var_Calc = (i - Average) ** 2 / (len(list1) - 1)
    Var += Var_Calc
    Std_Dev = math.sqrt(Var)
print (Std_Dev)

