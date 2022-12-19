max_A = max(A)
    if max_A > 0:
        for i in range(max_A + 1):
            if i + 1 in A:
                pass
            else:
                return i + 1
    else:
        return 1
        
