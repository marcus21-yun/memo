# 입력값
# a = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']

a = ['감', '감']

# 채워야하는 함수
def count_list(a_list):
    result = {}
    for element in a_list:
        # print(result)
        # print(element)
        if element in result:
            result[element] += 1
            # print(result)
            # print(element)
            # print(result[element])
        else:
            result[element] = 1
            # print(result)
            # print(element)
            # print(result[element])

    return result


# 결과값
print(count_list(a))
