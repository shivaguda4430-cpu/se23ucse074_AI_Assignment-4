from collections import deque

states=["WA","NT","SA","Q","NSW","V","T"]

full_names={
"WA":"Western Australia",
"NT":"Northern Territory",
"SA":"South Australia",
"Q":"Queensland",
"NSW":"New South Wales",
"V":"Victoria",
"T":"Tasmania"
}

adj={
"WA":["NT","SA"],
"NT":["WA","SA","Q"],
"SA":["WA","NT","Q","NSW","V"],
"Q":["NT","SA","NSW"],
"NSW":["Q","SA","V"],
"V":["SA","NSW"],
"T":[]
}

defaults=["Red","Green","Blue"]

def make_domains(cols):
    return {v:list(cols) for v in states}

def revise(doms,xi,xj):
    changed=False
    for val in doms[xi][:]:
        if not any(val!=other for other in doms[xj]):
            doms[xi].remove(val)
            changed=True
    return changed

def ac3(doms):
    q=deque((xi,xj) for xi in adj for xj in adj[xi])
    while q:
        xi,xj=q.popleft()
        if revise(doms,xi,xj):
            if not doms[xi]:
                return False
            for xk in adj[xi]:
                if xk!=xj:
                    q.append((xk,xi))
    return True

def consistent(var,val,assigned):
    return all(assigned.get(nb)!=val for nb in adj[var])

def pick_var(assigned,doms):
    left=[v for v in states if v not in assigned]
    return min(left,key=lambda v:len(doms[v]))

def fwd_check(var,val,assigned,doms):
    pruned={}
    for nb in adj[var]:
        if nb not in assigned:
            nd=[v for v in doms[nb] if v!=val]
            if not nd:
                return None,pruned
            pruned[nb]=doms[nb][:]
            doms[nb]=nd
    return True,pruned

def backtrack(assigned,doms):
    if len(assigned)==len(states):
        return assigned
    var=pick_var(assigned,doms)
    for val in doms[var]:
        if consistent(var,val,assigned):
            assigned[var]=val
            ok,pruned=fwd_check(var,val,assigned,doms)
            if ok:
                res=backtrack(assigned,doms)
                if res:
                    return res
            assigned.pop(var)
            for nb,saved in pruned.items():
                doms[nb]=saved
    return None

def solve(cols):
    doms=make_domains(cols)
    if not ac3(doms):
        print("No solution possible with current colour set")
        return None
    return backtrack({},doms)

def display(res):
    if not res:
        print("No valid Colouring found\n")
        return
    print("\nSolution:\n")
    print(f"  {'State':<25} Colour")
    print(f"  {'-------------------':<25} -----")
    for v in states:
        print(f"  {full_names[v]:<25} {res[v]}")
    print()

print("\n*** Map Colouring Problem (CSP - Australia) ***\n")

cols=list(defaults)

while True:
    print("1. Solve with Current Colours")
    print("2. Set Custom Colours")
    print("3. Display Colours")
    print("4. Exit\n")

    try:
        ch=int(input("Enter Choice: "))
    except:
        print("Enter valid number\n")
        continue

    if ch==1:
        print(f"\nColours used: {', '.join(cols)}")
        res=solve(cols)
        display(res)

    elif ch==2:
        raw=input("Enter colours (comma separated): ").split(",")
        new=[c.strip() for c in raw if c.strip()]
        if len(new)<3:
            print("Minimum 3 colours required\n")
        else:
            cols=new
            print("Colours updated\n")

    elif ch==3:
        print(f"\nCurrent Colours: {', '.join(cols)}\n")

    elif ch==4:
        break

    else:
        print("Invalid choice\n")
