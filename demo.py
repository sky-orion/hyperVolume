#encoding=utf-8
'''
测试示例
'''
from hyperVolume import HyperVolume

object_number = 2 # 目标数
nondominated_solutions_size = 10 # 非支配解数
def get_solutions(n):
    '''
    生成非支配解
    '''
    solutions = [
        [i/n,(n-i)/n]
        for i in range(n)
    ]
    return solutions
nondominated_solutions = get_solutions(nondominated_solutions_size) # 得到非支配解集
print(nondominated_solutions)
hv = HyperVolume(object_number)
print(hv.get_hyperVolume(nondominated_solutions)) # 计算超体积值