def find_min_max(numbers):
    if not numbers:
        return None, None
    
    # 첫 번째 값으로 초기화
    minimum = numbers[0]
    maximum = numbers[0]
    
    # 나머지 값들과 비교
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return minimum, maximum

def main():
    try:
        # 사용자 입력 받기
        user_input = input(("비교할 숫자를 공백 기준으로 입력하세요. : ")).strip()
        
        # 공백으로 나누기
        input_parts = user_input.split()
        
        # 숫자로 변환
        numbers = []
        for part in input_parts:
            try:
                num = float(part)
                numbers.append(num)
            except ValueError:
                raise ValueError("Invalid input.")
                print("Invalid input.")
                return
        
        # 빈 입력 처리
        if not numbers:
            print("Invalid input.")
            return
        
        # 최소값, 최대값 찾기
        minimum, maximum = find_min_max(numbers)
        
        # 결과 출력
        print(f"Min: {minimum}, Max: {maximum}")
        
    except Exception as e:
        print("Invalid input.")

if __name__ == "__main__":
    main()

