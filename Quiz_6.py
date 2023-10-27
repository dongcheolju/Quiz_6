def validate_korean_resident_id(resident_id):
    resident_id = resident_id.replace("-", "").replace(" ", "")      # 공백과 하이픈(-) 제거

    if len(resident_id) != 13:                                       # 입력 받은 수가 13자리가 아닌 경우 잘못된 것으로 판단
        return False

    id_digits = [int(digit) for digit in resident_id]                # 주민등록번호를 id_digits에 리스트로 저장
    multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]               # 가중치 리스트 생성

    total = sum(digit * multiplier for digit, multiplier in zip(id_digits[:12], multipliers))
         # zip 함수를 사용하여 id_digits[:12]와 multipliers 리스트에서 같은 인덱스의 요소끼리 묶어, 각각의 숫자를 곱한 결과를 리스트로 생성
         # 주민등록번호 12자리와 숫자에 각각의 가중치를 곱하고 그 결과를 모두 합한 값을 total 변수에 저장

    remainder = total % 11                                           # 합을 11로 나눈 나머지
    result = 11 - remainder                                          # 11에서 나머지를 빼서 result 변수에 저장
    #유효성 검사 실행
    if result == 10:                                                 # result가 10인 경우, 마지막 자리(검증 코드)가 0
        return int(resident_id[-1]) == 0
    elif result == 11:                                               # result가 11인 경우, 마지막 자리(검증 코드)가 1
        return int(resident_id[-1]) == 1
    else:                                                            # result가 10과 11이 아닌 경우, 검증 코드가 곧 result
        return int(resident_id[-1]) == result

# 주민등록번호 유효성 검사 실행 (하이픈 포함)
resident_id = input("주민등록번호 입력 (하이픈 포함)\n:")                   # 사용자에게 주민번호 입력 받기
if validate_korean_resident_id(resident_id):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

