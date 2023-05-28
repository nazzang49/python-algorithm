# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    lru = [""] * cacheSize
    for city in cities:
        city = city.lower()
        # (!) cache hit
        if city in lru:
            answer += 1
            lru.remove(city)
            lru.insert(0, city)
        # (!) cache miss = new cache
        else:
            answer += 5
            lru.pop()
            lru.insert(0, city)
    return answer