def solution(A):
    if max_A > 0:
        for i in range(max_A + 1):
            if i + 1 in A:
                pass
            else:
                return i + 1
    else:
        return 1

if __name__ == '__main__':
        A1 = [1, 2, 3]
        A2 = [-1, -2]
        A3 = range(1, 100000)
        A4 = range(-1000000, 1000000)
        sol = solution(A4)
        from time import time
        start = time()
        print(sol)
        print(f'{time()-start:.6f} seconds')
