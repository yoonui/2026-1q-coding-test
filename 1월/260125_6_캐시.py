def solution(cacheSize, cities):
    cache = []
    answer = 0

    for i in cities:
        city = i.lower()
        if city in cache:
            c = cache.index(city)
            a = cache.pop(c)
            cache.append(city)
            answer += 1
        else:
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
            answer += 5

    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0, ["Jeju", "Jeju"]))