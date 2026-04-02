letters=['S','E','N','D','M','O','R','Y']

def valid(assign):
    if len(set(assign.values()))<len(assign):
        return False
    if 'S' in assign and assign['S']==0:
        return False
    if 'M' in assign and assign['M']==0:
        return False
    if len(assign)==8:
        s=assign
        send=s['S']*1000+s['E']*100+s['N']*10+s['D']
        more=s['M']*1000+s['O']*100+s['R']*10+s['E']
        money=s['M']*10000+s['O']*1000+s['N']*100+s['E']*10+s['Y']
        return send+more==money
    return True

def backtrack(assign):
    if len(assign)==8:
        return assign
    for l in letters:
        if l not in assign:
            var=l
            break
    for d in range(10):
        assign[var]=d
        if valid(assign):
            res=backtrack(assign)
            if res:
                return res
        del assign[var]
    return None

res=backtrack({})
if res:
    print("\nSolution:\n")
    for k in sorted(res):
        print(f"{k} = {res[k]}")
