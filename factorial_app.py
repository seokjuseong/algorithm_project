print("factorial_app.py is now running")
import time
test_array =  [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
def run_with_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed

def factorial_iter(n): 
    result = 1
    for k in range (2, n + 1):
        result *= k
    return result

def factorial_rec(n):
    #재귀 호출 기반 n!
    if n == 1 or n == 0:
        return 1
    
    return n * factorial_rec(n - 1)
        

if __name__ == "__main__":
    while(True):
        print("""
            1. 반복법으로 n! 계산
            2. 재귀로 n! 계산    
            3. 두 방식 모두 계산 후 결과/시간 비교
            4. 준비된 테스트 데이터 일괄 실행
            5. 프로그램 종료""")
        while(True):
            choice = int(input("\t*팩토리얼 실행 방식을 선택하세요 (1 / 2 / 3/ 4 / 5) :"))
            if choice not in [1, 2, 3, 4, 5]:
                print("항목에 해당하는 번호를 입력하세요")
                continue
            break
            


        while(True):
            if choice == 5:
                print("프로그램을 종료합니다.")
                exit()
            elif choice == 4:
                print("테스트 데이터 실행")
                for i in test_array:
                    result_i, t_i = run_with_time(factorial_iter, i)
                    result_r, t_r = run_with_time(factorial_rec, i)
                    print(f"재귀함수fac: {i}! = {result_r} 소요시간: {t_r:.6f}")
                    print(f"반복함수fac: {i}! = {result_i} 소요시간: {t_i:.6f}")
                break
            

            try:
                num = int(input("\t숫자를 입력하세요 :"))
                if num < 0:
                    raise ValueError("0보다 큰 정수를 입력하세요")
                break
            except ValueError:
                print("0 보다 크거나 같은 정수를 입력하세요")
                continue
                
        if choice == 1:
            result, t = run_with_time(factorial_iter, num)
            print(f"반복문 팩토리얼 : {num}! = {result}")
            print(f"소요시간: {t:.6f}")
        elif choice == 2:
            result, t = run_with_time(factorial_rec, num)
            print(f"재귀함수 팩토리얼 : {num}! = {result}")
            print(f"소요시간: {t:.6f}")
        elif choice == 3:
            
            result, t = run_with_time(factorial_iter, num)
            print(f"반복문 팩토리얼 : {num}! = {result}")
            print(f"소요시간: {t:.6f}")

            result, t = run_with_time(factorial_rec, num)
            print(f"재귀함수 팩토리얼 : {num}! = {result}")
            print(f"소요시간: {t:.6f}")
        print("---------------------------------------")