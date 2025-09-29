print("factorial_app.py is now running")
import time

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
    if n == 1:
        return 1
    
    return n * factorial_rec(n - 1)
        

if __name__ == "__main__":
    while(True):
        print("""
            1. 반복문 기반 팩토리얼
            2. 재귀함수 기반 팩토리얼    
            3. 반복문, 재귀함수 둘다 사용
            4. 프로그램 종료
            """)
        while(True):
            choice = int(input("\t*팩토리얼 실행 방식을 선택하세요 (1 / 2 / 3/ 4) :"))
            if choice not in [1, 2, 3, 4]:
                print("항목에 해당하는 번호를 입력하세요")
                continue
            break
            


        while(True):
            if choice == 4: 
                print("프로그램을 종료합니다.")
                exit()
            try:
                num = int(input("\t숫자를 입력하세요 :"))
                if num < 0:
                    raise ValueError("0보다 큰 정수를 입력하세요")
                break
            except ValueError:
                print("0 보다 큰 정수를 입력하세요")
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