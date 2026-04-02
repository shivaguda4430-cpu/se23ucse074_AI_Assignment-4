from collections import deque

districts=[
"Adilabad","Bhadradri_Kothagudem","Hyderabad","Jagtial","Jangaon","Jayashankar_Bhupalpally",
"Jogulamba_Gadwal","Kamareddy","Karimnagar","Khammam","Komaram_Bheem","Mahabubabad",
"Mahabubnagar","Mancherial","Medak","Medchal_Malkajgiri","Mulugu","Nagarkurnool",
"Nalgonda","Narayanpet","Nirmal","Nizamabad","Peddapalli","Rajanna_Sircilla",
"Rangareddy","Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy",
"Warangal_Rural","Warangal_Urban","Yadadri_Bhuvanagiri"
]

adj={
"Adilabad":["Komaram_Bheem","Nirmal"],
"Komaram_Bheem":["Adilabad","Mancherial"],
"Mancherial":["Komaram_Bheem","Peddapalli","Nirmal"],
"Nirmal":["Adilabad","Mancherial","Jagtiyal"],
"Jagtiyal":["Nirmal","Peddapalli","Rajanna_Sircilla","Karimnagar"],
"Peddapalli":["Mancherial","Jagtiyal","Karimnagar"],
"Karimnagar":["Jagtiyal","Peddapalli","Rajanna_Sircilla","Warangal_Urban"],
"Rajanna_Sircilla":["Jagtiyal","Karimnagar","Siddipet"],
"Siddipet":["Rajanna_Sircilla","Medak","Jangaon","Warangal_Rural"],
"Medak":["Sangareddy","Siddipet","Kamareddy"],
"Sangareddy":["Medak","Medchal_Malkajgiri","Vikarabad"],
"Medchal_Malkajgiri":["Hyderabad","Rangareddy","Sangareddy"],
"Hyderabad":["Medchal_Malkajgiri","Rangareddy"],
"Rangareddy":["Hyderabad","Medchal_Malkajgiri","Vikarabad","Mahabubnagar"],
"Vikarabad":["Rangareddy","Sangareddy","Narayanpet"],
"Narayanpet":["Vikarabad","Mahabubnagar"],
"Mahabubnagar":["Narayanpet","Rangareddy","Wanaparthy","Nagarkurnool"],
"Wanaparthy":["Mahabubnagar","Jogulamba_Gadwal"],
"Jogulamba_Gadwal":["Wanaparthy","Nagarkurnool"],
"Nagarkurnool":["Jogulamba_Gadwal","Mahabubnagar","Nalgonda"],
"Nalgonda":["Nagarkurnool","Suryapet","Yadadri_Bhuvanagiri"],
"Suryapet":["Nalgonda","Khammam"],
"Khammam":["Suryapet","Bhadradri_Kothagudem"],
"Bhadradri_Kothagudem":["Khammam","Mulugu"],
"Mulugu":["Bhadradri_Kothagudem","Jayashankar_Bhupalpally"],
"Jayashankar_Bhupalpally":["Mulugu","Warangal_Rural"],
"Warangal_Rural":["Jayashankar_Bhupalpally","Warangal_Urban","Siddipet"],
"Warangal_Urban":["Warangal_Rural","Karimnagar","Jangaon"],
"Jangaon":["Warangal_Urban","Siddipet","Yadadri_Bhuvanagiri"],
"Yadadri_Bhuvanagiri":["Jangaon","Nalgonda","Medchal_Malkajgiri"],
"Kamareddy":["Medak","Nizamabad"],
"Nizamabad":["Kamareddy"],
"Mahabubabad":["Warangal_Rural"],
"Medchal_Malkajgiri_extra":[]
}

for d in districts:
    if d not in adj:
        adj[d]=[]

colors=["Red","Green","Blue","Yellow"]

def make_domains():
    return {v:list(colors) for v in districts}

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
    left=[v for v in districts if v not in assigned]
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
    if len(assigned)==len(districts):
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

def solve():
    doms=make_domains()
    if not ac3(doms):
        return None
    return backtrack({},doms)

def display(res):
    if not res:
        print("No solution found")
        return
    print("\nTelangana District Map Coloring:\n")
    for d in districts:
        print(f"{d:<30} {res[d]}")

result=solve()
display(result)
