import copy


class max_loading:
    weight = []
    cnt_box = 0
    temp_ret = []
    current_weight = 0
    rest_weight = 0
    max_weight = 0
    ret = []
    limited_weight = 0

    def __init__(self, weight, limited_weight):
        self.weight = weight
        self.limited_weight = limited_weight
        self.cnt_box = len(weight)
        for i in self.weight:
            self.rest_weight += i
        self.temp_ret = [0] * (self.cnt_box)
        self.ret = [0] * (self.cnt_box)

    def max_loading(self):
        self.load(1)

    def load(self, deepth):
        if deepth > self.cnt_box-1:
            if self.current_weight > self.max_weight:
                self.ret = copy.copy(self.temp_ret)
                self.max_weight = self.current_weight
            return
        self.rest_weight -= self.weight[deepth]
        if self.current_weight + self.weight[deepth] <= self.limited_weight:
            self.temp_ret[deepth] = 1
            self.current_weight += self.weight[deepth]
            self.load(deepth + 1)
            self.current_weight -= self.weight[deepth]
        if self.current_weight + self.rest_weight > self.max_weight:
            self.temp_ret[deepth] = 0
            self.load(deepth + 1)
        self.rest_weight += self.weight[deepth]


ml = max_loading([2, 2, 6, 5, 4], 16)
ml.max_loading()
print(ml.ret)
