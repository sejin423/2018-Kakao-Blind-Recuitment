# 이진수 변환
def binary(x):
    result = ''
    arr = ['0','1']
    num = x
    while num > 0:
        result = arr[num % 2] + result
        num //= 2
    return result 
    
def solution(n, arr1, arr2):
    answer = []
    
    for ar1, ar2 in zip(arr1,arr2):
        full_str = ''
        bin_result1 = binary(ar1)
        bin_result2 = binary(ar2)
        
        while len(bin_result1) < n:
            bin_result1 = '0' + bin_result1
        while len(bin_result2) < n:
            bin_result2 = '0' + bin_result2
			
        for i in range(n):
            # 두 결과 값 중 한개라도 1인 경우에 '#' 추가, 그렇지 않으면 ' ' 추가
            if bin_result1[i] =='1' or bin_result2[i] =='1':
                full_str += '#'
            else:
                full_str += ' '
        answer.append(full_str)
        
    return answer
