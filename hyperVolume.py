#encoding=utf-8
import numpy as np
class HyperVolume:
    '''
    计算超体积值

    目标值需进行归一化处理
    '''
    def __init__(self,object_number):
        '''
        :param object_number int 目标数
        '''
        self.__object_number = object_number
    def get_hyperVolume(self,solutions,refer_point = [1.2,1.2]):
        '''
        计算超体积值

        :param solutions list 非支配解集，是解的目标函数值列表，形式如：[[object1,object2],[object1,object2],...]

        :param refer_point list 参考点，要被solutions内所有点支配，默认为[1.2,1.2]
        '''
        refer_point = np.array(refer_point)
        solutions = np.array(solutions)
        solutions = solutions[solutions[:,0].argsort(kind="mergesort")[::-1]] # 按第一个目标降序排序
        volume = 0
        for i in solutions:
            volume += abs(i[0] - refer_point[0])*abs(i[1] - refer_point[1])
            refer_point[0] -= refer_point[0] -  i[0]
        return volume