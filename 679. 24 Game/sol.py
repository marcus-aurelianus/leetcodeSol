from operator import truediv, mul, add, sub
def judgePoint24(A) -> bool:
    if not A: return False
    if len(A) == 1: return abs(A[0] - 24) < 1e-6
    print(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                B = [A[k] for k in range(len(A)) if i != k != j]
                for op in (truediv, mul, add, sub):
                    print(B)
                    if (op is add or op is mul) and j > i: continue
                    if op is not truediv or A[j]:
                        B.append(op(A[i], A[j]))
                        print(B,A[i],A[j])
                        if judgePoint24(B): return True
                        B.pop()
    return False


print(judgePoint24([1,2,3,4]))
