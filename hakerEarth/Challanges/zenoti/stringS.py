
"""
 int best = 0;

        for(int i = 0;i<N;i++) {
            if(Math.abs(Arr[i]) > Math.abs(best)) {
                best = Arr[i];
            }else if(Math.abs(best) == Math.abs(Arr[i]) && best > Arr[i]) {
                best = Arr[i];
            }
        }
        return best;
"""

def Far_Sol(N, A):
    result=0
    for i in range(N):
        if abs(A[i]) > abs(result):
            result = A[i]
        elif result > A[i] and abs(result)==abs(A[i]):
            result = A[i]
    return result

A=[1, 2, 3, 4, 5]
N=len(A)
print(Far_Sol(N,A))


