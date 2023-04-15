unit_a, unit_b = 0, 0
degree_a, degree_b = 0.0, 0.0
GPA_a, GPA_b = 0.0, 0.0
while True:
    print('작업을 선택하세요')
    print('1. 입력')
    print('2. 계산')
    ex = input()
    if ex == '1':
            print('학점을 입력하세요:')
            unit = input()
            print('평점을 입력하세요:')
            degree = input()
            def degree_score(degree):
                match degree:
                    case 'A+':
                        return float(4.5)
                    case 'A':
                        return float(4.0)
                    case 'B+':
                        return float(3.5)
                    case 'B':
                        return float(3.0)
                    case 'C+':
                        return float(2.5)
                    case 'C':
                        return float(2.0)
                    case 'D+':
                        return float(1.5)
                    case 'D':
                        return float(1.0)
                    case 'F':
                        return float(0.0)
            unit_a += int(unit)
            if degree == 'F':
                unit_b += 0
            else :
                unit_b += int(unit)

            degree_a += degree_score(degree)
            if degree == 'F':
                degree_b += 0
            else:
                degree_b += degree_score(degree)

            GPA_a += float(unit_a*degree_a)
            GPA_b += float(unit_b*degree_b)

            continue


    elif ex == '2':
            print('제출용: ' + str(unit_a) + '학점 (GPA: ' + str(GPA_a/unit_a)+')')
            print('제출용: ' + str(unit_b) + '학점 (GPA: ' + str(GPA_b/unit_b)+')')
            break