from collections import defaultdict
x = defaultdict(lambda: 'World')
x['0'] = '\nYoooo'
x['1'] = '\nBeb'
print(x['Hello'], x['0'],x['1'])
