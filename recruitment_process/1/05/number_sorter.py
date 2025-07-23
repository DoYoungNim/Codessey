def bubble_sort(numbers):
    n = len(numbers)
    
    # 버블 정렬 구현
    for i in range(n):
        # 각 패스마다 가장 큰 값이 맨 뒤로 이동
        for j in range(0, n - i - 1):
            # 인접한 두 원소를 비교하여 순서가 잘못되었으면 교환
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    return numbers

def main():
    try:
        # 사용자 입력 받기
        user_input = input(("정렬할 숫자를 공백 기준으로 입력하세요. : ")).strip()
        
        # 빈 입력 처리
        if not user_input:
            print("Invalid input.")
            return
        
        # 공백으로 나누기
        input_parts = user_input.split()
        
        # 숫자로 변환
        numbers = []
        for part in input_parts:
            try:
                num = float(part)
                numbers.append(num)
            except ValueError:
                print("Invalid input.")
                return
        
        # 빈 리스트 처리
        if not numbers:
            print("Invalid input.")
            return
        
        # 정렬 수행
        sorted_numbers = bubble_sort(numbers)
        
        # 결과 출력 (float 형태로 출력)
        sorted_str = " ".join(str(num) for num in sorted_numbers)
        print(f"Sorted: {sorted_str}")
        
    except Exception:
        print("Invalid input.")

if __name__ == "__main__":
    main()