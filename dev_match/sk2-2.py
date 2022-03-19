
# arr = ["1","2","4","3","3","4","1","5"]
# process = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
# result = ["24","3415","4922","12492215","13"]


##여러 프로세스가 다음 규칙에 따라 배열(arr) 하나에 접근하여 읽기(Read) 또는 쓰기(Write) 작업을 수행하려 합니다.
#
# 한 번에 여러 프로세스가 배열에서 동시에 읽기 작업을 수행할 수 있습니다.
# 배열에 읽기 작업을 수행 중인 경우, 새로운 읽기 요청 프로세스는 즉시 작업을 수행할 수 있습니다.
# 한 번에 하나의 프로세스만 배열에서 쓰기 작업을 수행할 수 있습니다.
# 배열에 쓰기 작업을 수행 중인 경우, 새로운 읽기, 쓰기 요청 프로세스는 모두 대기해야 합니다.
# 배열에 읽기 작업을 수행 중인 경우, 새로운 쓰기 요청 프로세스는 모두 대기해야 합니다.
# 하나 이상의 쓰기 작업이 대기 중인 경우, 새로운 읽기 요청 또한 대기해야 합니다.
# 대기 중인 읽기, 쓰기 작업 중에서 다음으로 작업할 프로세스를 선택할 때
# 읽기 작업보다 쓰기 작업을 먼저 수행합니다.
# 쓰기 작업이 여러 개라면, 먼저 요청된 쓰기 작업을 먼저 수행합니다.
# 대기 중인 작업을 배열에서 수행하려 함과 동시에 새로운 작업 요청이 들어온다면, 새 작업 요청을 포함하여 다음으로 작업할 프로세스를 선택합니다.
# 예를 들어, 10초에 쓰기 작업이 끝났고, 읽기 작업만 대기 중인 경우, 10초에 새로운 쓰기 작업 요청이 들어왔다면, 쓰기 작업을 먼저 처리합니다.
# 위 규칙에 따라 읽기, 쓰기 작업을 처리한 후, 읽기 작업에서 읽은 내용과 전체 프로세스가 배열을 사용한 시간은 얼마나 되는지 알아보려 합니다.
#
# 초기 배열의 상태가 담긴 문자열 배열 arr과 읽기, 쓰기 작업 요청이 담긴 문자열 배열 processes가 매개변수로 주어집니다. 읽기 작업에서 읽은 내용을 processes에서 주어진 순서대로 정답 배열에 담은 뒤, 배열이 전체 프로세스에 의해 사용된 시간을 정답 배열의 마지막에 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 5 ≤ arr의 길이 ≤ 1,000
# 1 ≤ arr의 원소 ≤ 9
# arr의 원소는 1부터 9까지의 숫자가 문자열 형태로 담겨있습니다.
# 1 ≤ processes의 길이 ≤ 1,000
# processes의 원소는 "read t1 t2 A B", 또는 "write t1 t2 A B C" 형태입니다.
# t1은 요청 시각, t2는 해당 요청을 처리하는데 걸리는 시간입니다.
# 1 ≤ t1 ≤ 1,000
# 1 ≤ t2 ≤ 100
# A, B는 데이터를 읽거나 쓸 구간으로, 배열의 인덱스를 나타냅니다.
# 0 ≤ A ≤ B < arr의 길이
# C는 배열 구간에 쓸 한 자리 숫자입니다. arr[A] ~ arr[B]에 해당하는 구간의 값을 전부 C로 바꾸면 됩니다.
# 1 ≤ C ≤ 9
# t1, t2, A, B, C는 모두 정수입니다.
# 같은 시각에 요청된 작업은 없습니다(즉, 모든 문자열에 대해서 t1의 값은 서로 다릅니다).
# processes에는 "read t1 t2 A B"가 적어도 하나 이상 들어있습니다.
# processes는 t1기준으로 정렬되어 있습니다.
# 배열이 전체 프로세스에 의해 사용된 시간은 정답 배열의 마지막에 문자열 형태로 담아 return 하면 됩니다.



arrinput = ["1","2","4","3","3","4","1","5"]
proinput = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]


#arrinput = ["1", "1", "1", "1", "1", "1", "1"]
#proinput = ["write 1 12 1 5 8", "read 2 3 0 2", "read 5 5 1 2", "read 7 5 2 5", "write 13 4 0 1 3", "write 19 3 3 5 5", "read 30 4 0 6", "read 32 3 1 5"]

def solution(arr, processes):

    write_process = []
    read_process = []


    for process in processes:
        ipt = list(map(str, process.split(" ")))
        t1, t2, a, b = int(ipt[1]), int(ipt[2]), int(ipt[3]), int(ipt[4])
        if ipt[0]=="read":
            read_process.append([t1, t2, a, b])
        else:
            write_process.append([t1, t2, a, b, ipt[5]])

    ans = [""]*len(read_process)

    cur_time = 1
    cur_process = []
    spent_time = 0

    def minst(arr):
        minv = 1001
        idx = -1
        for i, a in enumerate(arr):
            if minv>a[0]:
                idx = i
                minv = a[0]
        return [idx, minv]

    while (write_process or read_process or cur_process) and cur_time<30:


        cur_time += 1



    answer = ans
    answer.append(str(spent_time))
    #answer = []
    return answer



x = solution(arrinput, proinput)
print(x)