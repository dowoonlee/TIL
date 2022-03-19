# 쇼핑몰에서 상품검색
# 검색어의 고유한 부분문자열(다른 문자 내에 존재하지 않는 부분문자열) 중 가장 짧은 애들
# 사전순으로 정렬 + 중복x
# 검색어가 존재하지않는 경우 None
# ["pencil","cilicon","contrabase","picturelist"]
# => ["en nc pe","ico ili lic","a b","u"]
# ["abcdeabcd","cdabe","abce","bcdeab"]
# => ["abcd eabc","be da","ce","None"]


# 문제 설명
# 당신은 쇼핑몰에서 상품을 검색할 수 있습니다. 검색어를 입력하면 검색어를 부분 문자열로 갖는 모든 상품들이 검색됩니다.
# 부분 문자열이란, 문자열의 연속된 일부를 의미합니다. 예를 들어 abcde의 부분 문자열로 abc나 bcde 등이 있고, ac나 ea는 부분 문자열이 아닙니다.
#
# 특정 단어로 검색해서 검색된 상품의 개수가 하나일 때, 해당 단어를 상품의 고유 검색어라고 합니다. 당신은 상품마다 고유 검색어 중 가장 짧은 고유 검색어 목록을 구하려 합니다.
#
# 검색어 목록은 사전 순서대로 빠른 순으로 정렬되고, 중복되지 않아야 합니다. 검색어 목록은 공백 하나로 검색어들을 구분하는 형태입니다. 만약 고유 검색어가 없다면 None을 목록에 담습니다.
#
# 예를 들어, 쇼핑몰에 pencil, cilicon, contrabase, picturelist 네 가지 상품이 있다면, 각 상품의 가장 짧은 고유 검색어 목록은 다음과 같습니다.
#
# pencil : en nc pe
# cilicon : ico ili lic
# contrabase : a b
# picturelist : u
# pencil의 고유 검색어를 예시로 들어보겠습니다.
#
# pencil의 고유 검색어 중 길이가 1인 검색어는 존재하지 않습니다.
# p를 검색어로 검색하면 pencil과 picturelist 두 가지 상품이 검색되므로 p는 pencil의 고유 검색어가 아닙니다.
# e,n,c,i,l도 마찬가지로, pencil과 다른 상품이 함께 검색되므로 pencil의 고유 검색어가 아닙니다.
# en,nc,pe중 하나를 검색했을 때 pencil 하나만 검색됩니다. 따라서 pencil의 가장 짧은 고유 검색어는 en,nc,pe 3가지입니다.
# enc, nci, pencil 등도 고유 검색어지만, 더 짧은 고유 검색어가 존재하므로 가장 짧은 고유 검색어에서 제외됩니다.
# 쇼핑몰에 등록된 상품의 이름을 담은 문자열 배열 goods가 매개변수로 주어졌을 때, 가장 짧은 고유 검색어 목록을 순서대로 문자열 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

def solution(goods):
    ans = []
    for good in goods:  # for all goods
        flag = True
        length = 1
        sub_ans = []
        while flag and length < len(good)+1:  # check the substring of length
            substrs = []
            for idx in range(0, len(good) - length + 1):  # substring of index [idx, idx+length]
                substrs.append(good[idx:idx + length])
            substrs = list(set(substrs))
            for substr in substrs:
                for comp_good in goods:
                    flag2 = True
                    if comp_good != good and substr in comp_good:
                        flag2 = False
                        break
                if flag2:
                    sub_ans.append(substr)
            if sub_ans:  # if there are unique substr
                flag = False  # finish while loop
            length += 1
        if sub_ans:
            sub_ans = list(set(sub_ans))
            sub_ans.sort()
            ans.append(" ".join(sub_ans))
        else:
            ans.append("None")

    answer = ans
    return answer

x = solution(["abcdeabcd","cdabe","abce","bcdeab"])
print(x)