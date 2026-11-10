import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        a = int(data[idx+1])
        b = int(data[idx+2])
        c = int(data[idx+3])
        idx += 4
        
        cycle_sum = a + b + c
        full_cycles = n // cycle_sum
        days = full_cycles * 3
        rem = n % cycle_sum
        
        if rem > 0:
            if rem <= a:
                days += 1
            elif rem <= a + b:
                days += 2
            else:
                days += 3
                
        results.append(str(days))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
