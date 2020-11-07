import json

oper = ['+','-','*','%','^','|','&']

dictionary = {}

combines = [
['114514'],
['11451', '4'],
['1', '14514'],
['11', '4514'],
['114', '514'],
['1145', '14'],
['1145', '1', '4'],
['1', '1451', '4'],
['1', '1', '4514'],
['11', '4', '514'],
['114', '5', '14'],
['1', '14', '514'],
['11', '45', '14'],
['114', '51', '4'],
['1', '145', '14'],
['11', '451', '4'],
['114', '5', '1', '4'],
['1', '145', '1', '4'],
['1', '1', '451', '4'],
['1', '1', '4', '514'],
['11', '45', '1', '4'],
['11', '4', '51', '4'],
['11', '4', '5', '14'],
['1', '14', '5', '14'],
['1', '1', '45', '14'],
['1', '14', '51', '4'],
['11', '4', '5', '1', '4'],
['1', '14', '5', '1', '4'],
['1', '1', '45', '1', '4'],
['1', '1', '4', '51', '4'],
['1', '1', '4', '5', '14'],
['1', '1', '4', '5', '1', '4'],
]

def get_combines():
    origin = []
    #part 1
    for i in range(1,6):
        origin = [1 for _ in range(i)]
        for j in range(i):
            origin[j] = 7 - i
            yield origin
            origin[j] = 1
    origin = [1,1,1,1,1,1]
    yield origin
    #part 2
    for i in range(2,5): yield [i,6-i]
    for i in range(2,4): yield [i,1,5-i]
    for i in range(1,4): yield [i,2,4-i]
    for i in range(1,3): yield [i,3,3-i]
    #part 3
    origin = [2,2,1,1]
    yield origin
    for i in range(1,3):
        origin[i],origin[i+1] = origin[i+1],origin[i]
        yield origin
    for i in range(2):
        origin[i],origin[i+1] = origin[i+1],origin[i]
        yield origin
    yield [1,2,2,1]

def combine(bits):
    ori_nums = ['1','1','4','5','1','4']
    new_nums = []
    order = 0
    for i in bits:
        num = ''
        for _ in range(i):
            num += ori_nums[order]
            order += 1
        new_nums.append(num)
    return new_nums


def dfs(str,nums,f):
    if len(nums) == 0:
        try:
            value = eval(str)
            if abs(value) in dictionary or abs(value) > 114514:
                return
            if value < 0:
                str = '-(' + str + ')'
                dictionary[-value] = str
                f.write(f'    "{-value}": "{str}",\n')
            else:
                dictionary[value] = str
                f.write(f'    "{value}": "{str}",\n')
            if len(dictionary) % 500 == 0:
                print('found {} expr.'.format(len(dictionary)))
            return
        except:
            return
    for op in oper:
        dfs(str + op + nums[0],nums[1:],f)
        for i in range(1,20):
            if int(nums[0]) > i:
                dfs(str + op + '(' + '~-'*i + nums[0] + ')',nums[1:],f)
            dfs(str + op + '(' + '-~'*i + nums[0] + ')',nums[1:],f)


if __name__ == '__main__':
    with open('out.json','w') as f:
        f.write("{\n")
        for nums in combines:
            print(nums,end=' Begin.\n')
            dfs(nums[0],nums[1:],f)
            print('===> Done.')
        f.write("}\n");

#for i in get_combines():
#    print(combine(i))

