
def calculate_power(base, exponent):
    """
    반복문을 사용하여 제곱 계산을 수행하는 함수
    
    Args:
        base (float): 밑
        exponent (int): 지수
    
    Returns:
        float: 제곱 계산 결과
    """
    if exponent == 0:
        return 1
    elif exponent > 0:
        result = 1
        for i in range(exponent):
            result *= base
        return result
    else:  # 음수 지수 처리
        result = 1
        for i in range(abs(exponent)):
            result *= base
        return 1 / result


def get_number_input():
    while True:
        try:
            number = float(input("Enter number: "))
            return number
        except ValueError:
            print("Invalid number input.")


def get_exponent_input():
    while True:
        try:
            exponent = int(input("Enter exponent: "))
            return exponent
        except ValueError:
            print("Invalid exponent input.")


def main():
    # 사용자 입력 받기
    base = get_number_input()
    exponent = get_exponent_input()
    
    # 제곱 계산 수행
    result = calculate_power(base, exponent)
    
    # 결과 출력
    if result == int(result):
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()