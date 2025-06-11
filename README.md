class BallChain:
    def __init__(self, balls):
        self.balls = balls

    def remove_balls(self):
        if not self.balls:
            return 0

        count = 0
        i = 0
        while i < len(self.balls):
            # Считаем количество одинаковых шариков подряд
            j = i
            while j < len(self.balls) and self.balls[j] == self.balls[i]:
                j += 1

            # Если количество одинаковых шариков 3 или более, то удаляем их
            if j - i >= 3:
                count += j - i
                self.balls = self.balls[:i] + self.balls[j:]  # Удаляем шарики из цепочки
                i = max(0, i - 1)  # Возвращаемся на один шаг назад, чтобы проверить новые цепочки
            else:
                i = j  # Переходим к следующему цвету

        return count


def main():
    try:
        # Ввод данных
        input_data = input("Введите количество шариков и их цвета (разделенные пробелами): ")
        data = list(map(int, input_data.split()))

        if len(data) < 2:
            raise ValueError("Должно быть как минимум одно значение для количества шариков и их цветов.")

        n = data[0]  # Количество шариков
        if n != len(data) - 1:
            raise ValueError("Количество шариков не соответствует количеству указанных цветов.")

        balls = data[1:]  # Цвета шариков

        # Проверка на допустимые цвета (от 0 до 9)
        if any(color < 0 or color > 9 for color in balls):
            raise ValueError("Цвета шариков должны быть в диапазоне от 0 до 9.")

        # Создаем объект цепочки шариков
        ball_chain = BallChain(balls)

        # Удаляем шарики и выводим результат
        destroyed_count = ball_chain.remove_balls()
        print(destroyed_count)

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
