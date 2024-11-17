import math

def main():
    n, m, k = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(k)]
    x_min, y_min = 0, 0

    for x, y in points:
        if x == y:
            if abs(x - x_min) < abs(y - y_min):
                x_min = max(x_min, x)  # Оновлюємо x_min, якщо він ближчий
            else:
                y_min = max(y_min, y)  # Оновлюємо y_min, якщо він ближчий
        else:
            if x < y:
                if x > x_min:
                    x_min = x
            else:
                if y > y_min:
                    y_min = y

    distance = math.sqrt(x_min ** 2 + y_min ** 2)
    print(distance)

main()
