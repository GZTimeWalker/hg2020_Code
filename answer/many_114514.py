import json
order = -1

data = {}
with open('out.json','r') as f:
    data = json.load(f)

data_r = {}
for i in data.keys():
    data_r[int(i)] = data[i]

keys = sorted(data_r.keys())
for i in keys:
    for r in range(1,31):
        if (i + r) not in data_r:
            data_r[i + r] = '-~'*r + '(' + data_r[i] + ')'
        if (i - r) > 0 and (i - r) not in data_r:
            data_r[i - r] = '~-'*r + '(' + data_r[i] + ')'

res = {}
for i in sorted([int(i) for i in data_r.keys()]):
    res[i] = data_r[i]

with open('final_out.json','w') as f:
    json.dump(res,f)
