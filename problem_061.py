def tria_fun(n): return (n*(n+1))//2
def squa_fun(n): return n**2
def pent_fun(n): return (n*(3*n-1))//2
def hexa_fun(n): return n*(2*n-1)
def hept_fun(n): return (n*(5*n-3))//2
def octa_fun(n): return n*(3*n-2)

def init_data(set_in):

    functions = [tria_fun, squa_fun, pent_fun, hexa_fun, hept_fun, octa_fun]

    for i in range(len(functions)) :

        n = 0
        while True:
            n+=1
            r = functions[i](n)
            if r < 1000  : continue
            if r > 10000 : break
            set_in[i].add(str(r))

# create a list of sets with all the numbers in string format
keys  = [set() for _ in range(6)]

init_data(keys)

# solve this recursively by building up the chain in memory
# when a full length chain is found the result is printed
chain = ["" for _ in range(6)] # initialize with empty chain

def solve(depth = 0, done=(99,), key=""): # (99,) mimics empty tuple

    # end of search when we have a matching chain: indicated by depth
    if depth == 6 and chain[0][:2] == chain[5][-2:]:
        # print result, explanation why below at recursion
        print(chain, done, sum([int(v) for v in chain]))
        return True

    # failed but reached max depth, small speed optimization
    if depth == 6 : return False

    # build chain by trying all numbers from all sets
    for set_i in range(6):

        if set_i in done : continue  # unless this set already in chain

        for k in keys[set_i]:   # try all keys

            # every number is potentially valid at depth 0
            # the others need to math the pattern
            if depth == 0 or (k[:2] == key[-2:]):

                chain[depth] = k # update chain

                # recursion
                res = solve(depth+1, done+(set_i,), k)

                # Skip at the first possible result or not?
                #
                # when not ending the recursion at the first possibility
                # there might not have a valid chain in memory when the
                # function exists
                #
                # solution: print at end of search but continue the search
                #
                # if res : return res # exit search if a solution is found

    # ending up here: no solution in current chain
    return False

res = solve()

# chain in memory probably invalid!
print(sum([int(v) for v in chain]))
