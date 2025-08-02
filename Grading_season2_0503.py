def get_five_answers(prompt, problem_numbers):
    """5개 단위로 답을 입력받는 함수"""
    while True:
        answers = input(f"{prompt} (문제 {problem_numbers[0]}-{problem_numbers[-1]}번, 예: 32451): ")
        
        # 입력 검증
        if len(answers) == 5 and all(c in '12345' for c in answers):
            return [int(c) for c in answers]
        else:
            print("올바르지 않은 입력입니다. 1~5 사이의 숫자 5개를 입력해주세요.")

def get_all_answers(prompt_prefix):
    """20개 답안을 5개씩 4번에 걸쳐 입력받는 함수"""
    all_answers = []
    
    for i in range(0, 20, 5):
        problem_numbers = list(range(i+1, i+6))
        five_answers = get_five_answers(prompt_prefix, problem_numbers)
        all_answers.extend(five_answers)
    
    return all_answers

def get_points():
    """각 문제별 배점을 입력받는 함수"""
    print("각 문제의 배점을 입력하세요 (2 또는 3)")
    points = []
    
    for i in range(0, 20, 5):
        problem_numbers = list(range(i+1, i+6))
        while True:
            points_input = input(f"문제 {problem_numbers[0]}-{problem_numbers[-1]}번 배점 (예: 22333): ")
            
            # 입력 검증
            if len(points_input) == 5 and all(c in '23' for c in points_input):
                points.extend([int(c) for c in points_input])
                break
            else:
                print("올바르지 않은 입력입니다. 2 또는 3만 입력해주세요.")
    
    return points

def get_student_answers_with_backtick():
    """학생 답안을 백틱으로 구분하여 입력받는 함수"""
    print("학생 답안을 입력하세요 (20문제를 백틱으로 구분)")
    print("예: 12345`12345`12345`12345")
    print("또는 'q'를 입력하여 종료")
    
    while True:
        answers_input = input("학생 답안: ")
        
        if answers_input.lower() == 'q':
            return 'q'
        
        # 백틱으로 분리
        parts = answers_input.split('`')
        
        # 입력 검증
        if len(parts) == 4:
            student_answers = []
            valid = True
            
            for part in parts:
                if len(part) == 5 and all(c in '12345' for c in part):
                    student_answers.extend([int(c) for c in part])
                else:
                    valid = False
                    break
            
            if valid:
                return student_answers
        
        print("올바르지 않은 입력입니다. 4개 그룹을 백틱(`)으로 구분하고, 각 그룹은 5개의 숫자(1-5)여야 합니다.")

def main():
    print("=== 시험 채점 프로그램 ===")
    print("5지 선다 20문제 채점 시스템")
    print()
    
    # 정답 입력받기
    print("정답을 입력하세요.")
    correct_answers = get_all_answers("정답을 입력하세요")
    
    # 배점 입력받기 (각 문제마다)
    print()
    problem_points = get_points()
    
    # 총 배점 계산
    total_possible_points = sum(problem_points)
    
    print()
    print("=== 시험 정보가 입력되었습니다 ===")
    print(f"총 20문항, 만점: {total_possible_points}점")
    
    # 배점 확인
    for i in range(20):
        print(f"문제 {i+1}번: {problem_points[i]}점")
    print()
    
    # 학생 답안 입력 및 채점
    while True:
        print("-" * 50)
        student_answers = get_student_answers_with_backtick()
        
        if student_answers == 'q':
            print("프로그램을 종료합니다.")
            return
        
        # 채점
        wrong_problems = []
        correct_count = 0
        total_score = 0
        
        for i in range(20):
            if student_answers[i] == correct_answers[i]:
                correct_count += 1
                total_score += problem_points[i]
            else:
                wrong_problems.append(i + 1)
        
        wrong_count = 20 - correct_count
        
        # 결과 출력
        print()
        print("=== 채점 결과 ===")
        
        if wrong_problems:
            
            print("=== 틀린 문제 상세 ===")
            for prob_num in wrong_problems:
                student_ans = student_answers[prob_num - 1]
                correct_ans = correct_answers[prob_num - 1]
                lost_points = problem_points[prob_num - 1]
                print(f"문제 {prob_num}번 ({lost_points}점): 학생답안 [{student_ans}] / 정답 [{correct_ans}]")
        else:
            print("모든 문제를 맞혔습니다!")
        
        print(f"맞힌 문제: {correct_count}개")
        print(f"틀린 문제: {wrong_count}개")
        print(f"틀린 문제 번호: {', '.join(map(str, wrong_problems))}")
        print()
        print(f"총점: {total_score}점 (만점 {total_possible_points}점)")

        print()

if __name__ == "__main__":
    main()