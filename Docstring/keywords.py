from keyword import kwlist

for a,b,c,d in zip(*[iter(kwlist)] *4):
    print('|**'+a+'**|**'+b+'**|**'+c+'**|**'+d+'**|')
    if a == 'False':
        print('|--|--|--|--|')
