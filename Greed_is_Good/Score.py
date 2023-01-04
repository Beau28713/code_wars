from collections import Counter


def score(dice):
    print(dice)
    count = Counter(dice)
    score = 0

    trip = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    single = {1: 100, 5: 50}

    for key in count:
        if count[key] > 3 and key in trip:
            score += trip[key]
            if key in single:
                score += single[key]

        elif count[key] == 3 and key in trip:
            score += trip[key]

        elif count[key] == 2 and key in single:
            score += single[key] *2
        
        elif count[key] == 1 and key in single:
            score += single[key]

    print(score)
    return score
