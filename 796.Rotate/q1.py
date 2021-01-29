def rotateString(A: str, B: str):
    C = A + A
    n = len(A)
    if A==B:
        return True
    for i in range(n):
        print(C[i:n+i])
        if C[i:n+i]==B:
            return True
        
    return False
print(rotateString('',''))
