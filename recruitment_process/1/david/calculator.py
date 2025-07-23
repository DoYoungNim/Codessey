def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b


def parse_expression(expression):


    try:
        # 공백 제거
        expression = expression.strip().replace(' ', '')
        
        if not expression:
            return None
        
        # 연산자 찾기 (마지막으로 나타나는 연산자를 찾아야 음수 처리 가능)
        operators = ['+', '-', '*', '/']
        operator_pos = -1
        operator = None
        
        # 뒤에서부터 연산자 찾기 (음수 처리를 위해)
        for i in range(len(expression) - 1, 0, -1):  # 첫 번째 문자는 제외 (음수 가능성)
            if expression[i] in operators:
                operator_pos = i
                operator = expression[i]
                break
        
        # 연산자를 찾지 못한 경우
        if operator_pos == -1:
            return None
        
        # 숫자 부분 분리
        num1_str = expression[:operator_pos]
        num2_str = expression[operator_pos + 1:]
        
        # 빈 문자열 체크
        if not num1_str or not num2_str:
            return None
        
        # 숫자 변환
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        return num1, operator, num2
    
    except ValueError:
        return None



def calculate_expression(expression):

    parsed = parse_expression(expression)
    
    if parsed is None:
        return "Error: Invalid expression format."
    
    num1, operator, num2 = parsed
    
    # 연산자에 따라 적절한 함수 호출
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)


def interactive_calculator():

    print("=== Interactive Calculator Mode ===")
    
    # 사용자로부터 첫 번째 숫자 입력 받기
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number input.")
        return
    
    # 사용자로부터 연산자 입력 받기
    operator = input("Enter operator (+, -, *, /): ")
    
    # 사용자로부터 두 번째 숫자 입력 받기
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return
    
    # 연산자에 따라 적절한 함수 호출
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator.")
        return
    
    # 결과 출력
    if isinstance(result, str):  # 에러 메시지인 경우
        print(result)
    else:
        # 결과가 정수인 경우 정수로 출력, 아닌 경우 실수로 출력
        if result == int(result):
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")


def expression_calculator():

    print("=== Expression Calculator Mode ===")
    print("Example: 2 + 3")
    
    expression = input("Enter expression: ")
    result = calculate_expression(expression)
    
    if isinstance(result, str):  # 에러 메시지인 경우
        print(result)
    elif result == int(result):
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")


def main():
    """
    계산기 프로그램의 메인 함수
    """
    print("Python Calculator")
    print("Choose mode:")
    print("1. Interactive mode (step by step)")
    print("2. Expression mode (one line input)")
    
    try:
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            interactive_calculator()
        elif choice == '2':
            expression_calculator()
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    except KeyboardInterrupt:
        print("\nCalculator terminated.")


if __name__ == "__main__":
    main()