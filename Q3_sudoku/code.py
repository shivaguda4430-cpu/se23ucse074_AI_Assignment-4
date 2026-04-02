def print_grid(g):
    for i in range(9):
        for j in range(9):
            print(g[i][j], end=" ")
        print()

def find_unassigned(g):
    mrv=None
    cell=None
    for i in range(9):
        for j in range(9):
            if g[i][j]==0:
                domain=get_domain(g,i,j)
                if mrv is None or len(domain)<len(mrv):
                    mrv=domain
                    cell=(i,j)
    return cell,mrv

def get_domain(g,r,c):
    used=set()
    for i in range(9):
        used.add(g[r][i])
        used.add(g[i][c])
    br=(r//3)*3
    bc=(c//3)*3
    for i in range(3):
        for j in range(3):
            used.add(g[br+i][bc+j])
    return [x for x in range(1,10) if x not in used]

def forward_check(g,r,c,val):
    g[r][c]=val
    for i in range(9):
        if g[r][i]==0 and not get_domain(g,r,i):
            g[r][c]=0
            return False
        if g[i][c]==0 and not get_domain(g,i,c):
            g[r][c]=0
            return False
    br=(r//3)*3
    bc=(c//3)*3
    for i in range(3):
        for j in range(3):
            if g[br+i][bc+j]==0 and not get_domain(g,br+i,bc+j):
                g[r][c]=0
                return False
    g[r][c]=0
    return True

def solve(g):
    cell,domain=find_unassigned(g)
    if not cell:
        return True
    r,c=cell
    for val in domain:
        if forward_check(g,r,c,val):
            g[r][c]=val
            if solve(g):
                return True
            g[r][c]=0
    return False

grid=[
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

print("Sudoku Solution:\n")
if solve(grid):
    print_grid(grid)
else:
    print("No solution exists")
