# 概念理解
# def move(plan,n,A,B):
#     if n == 1:
#          move(1,A,B)
#         plan.append((A,B))
#     if n > 1:
#         move(plan,n-1,A,C)
#         move(plan,1,A,B)
#         move(plan,n-1,C,B)

# plan记录移动策略，plan中的每个元素（x,y）表示把塔x最上面的圆盘移动到塔y的最上面
def move(plan,towers,n,x,y):
    set_xy = set((x,y)) #x,y组成集合
    z = towers - set_xy #第三个塔
    z = list(z)[0] #先把集合转换为列表，才能取出其中元素
    if n == 1:
        plan.append((x,y))
    if n > 1:
        move(plan,towers,n-1,x,z)
        move(plan,towers,1,x,y)
        move(plan,towers,n-1,z,y)


plan = []
n = 5
towers = set(('A','B','C')) #A, B, C三个塔
move(plan,towers,n,'A','B')
print(plan)

# n = 5 时的移动策略
# [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B'), ('A', 'C'),
#  ('B', 'C'), ('B', 'A'), ('C', 'A'), ('B', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), 
#  ('C', 'A'), ('C', 'B'), ('A', 'B'), ('C', 'A'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B'), 
#  ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]