def fib_dp_tab(n):
    # 1차원 테이블 준비
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    # Bottom-up 방식으로 테이블 채우기
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table

if __name__ == "__main__":
    n = int(input("계단의 개수를 입력하시오: "))
    array = fib_dp_tab(n + 1)
    print(f"{n}개의 계단을 오르는 방법의 수는 {array[-1]}가지입니다.")