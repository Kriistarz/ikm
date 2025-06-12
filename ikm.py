class BallChain:
    def __init__(self, balls):
        """Инициализация цепочки шариков."""
        self.balls = balls  # Основная структура данных для хранения цепочки

    def process_chain(self):
        """Основной метод обработки цепочки шариков."""
        total_removed = 0
        while True:
            removed = self.remove_sequences()  # Удаляем последовательности
            if removed == 0:  # Если больше ничего не удалено
                break
            total_removed += removed  # Суммируем удаленные шарики
        return total_removed

    def remove_sequences(self):
        """Внутренний метод для поиска и удаления последовательностей из 3+ одинаковых шариков."""
        if not self.balls:  # Если цепочка пуста
            return 0

        start = 0  # Начальный индекс для поиска последовательности
        removed = 0  # Счетчик удаленных шариков

        while start < len(self.balls):
            current = start + 1
            # Находим конец текущей последовательности одинаковых шариков
            while current < len(self.balls) and self.balls[current] == self.balls[start]:
                current += 1

            sequence_length = current - start
            if sequence_length >= 3:  # Если нашли последовательность из 3+ шариков
                # Удаляем последовательность из цепочки
                del self.balls[start:current]
                removed += sequence_length
                # Рекурсивно продолжаем поиск новых последовательностей
                return removed + self.remove_sequences()

            start += 1  # Переходим к следующему шарику

        return removed  # Возвращаем количество удаленных шариков


def main():
    """Основная функция с пользовательским интерфейсом."""
    print("Программа подсчета удаляемых шариков")
    print("Введите количество шариков и их цвета через пробел")
    print("Пример: 5 1 3 3 3 2")

    while True:
        try:
            # Получаем и обрабатываем пользовательский ввод
            user_input = input("Введите данные: ").strip()
            if not user_input:
                print("Ошибка: ввод не может быть пустым. Попробуйте снова.")
                continue

            # Преобразуем ввод в список чисел
            parts = list(map(int, user_input.split()))
            if len(parts) < 2:
                print("Ошибка: нужно ввести как минимум количество шариков и один цвет. Попробуйте снова.")
                continue

            # Проверяем соответствие количества шариков
            n = parts[0]
            if n != len(parts) - 1:
                print(f"Ошибка: указано {n} шариков, но введено {len(parts) - 1} цветов. Попробуйте снова.")
                continue

            # Проверяем допустимый диапазон количества шариков
            if n < 1 or n > 10 ** 5:
                print("Ошибка: количество шариков должно быть от 1 до 100000. Попробуйте снова.")
                continue

            # Извлекаем и проверяем цвета шариков
            balls = parts[1:]
            if any(ball < 0 or ball > 9 for ball in balls):
                print("Ошибка: цвета шариков должны быть числами от 0 до 9. Попробуйте снова.")
                continue

            # Создаем цепочку и обрабатываем
            chain = BallChain(balls)
            removed = chain.process_chain()
            print(f"Результат: {removed}")

            # Запрос на повторение
            another = input("Хотите проверить другую цепочку? (да/нет): ").lower()
            if another != 'да':
                break

        except ValueError:
            print("Ошибка: все вводимые значения должны быть целыми числами. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте снова.")


if __name__ == "__main__":
    main()
