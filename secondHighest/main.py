# Leetcode: 1796

def secondHighest(input: str) -> int:

    s = set()

    for item in input:
        if item.isdigit():
            s.add(item)
    
    num_list = sorted(s)

    if len(num_list) < 2:
        return -1

    return num_list[1]


if __name__ == '__main__':
    result = secondHighest("abc1111")
    print(result)