class Node:
    """Класс для представления узла в цепочке шариков."""

    def __init__(self, color):
        self.color = color
        self.next = None


class BallChain:
    def __init__(self, balls):
        """Инициализация цепочки шариков."""
        self.head = None
        self.build_chain(balls)  # Создание цепочки из входных данных

    def build_chain(self, balls):
        """Создает цепочку шариков из списка цветов."""
        for color in balls:
            new_node = Node(color)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

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
        if not self.head:  # Если цепочка пуста
            return 0

        current = self.head
        previous = None
        removed = 0

        while current:
            count = 1  # Счетчик текущей последовательности
            while current.next and current.color == current.next.color:
                count += 1
                current = current.next

            if count >= 3:  # Если нашли последовательность из 3+ шариков
                # Удаляем последовательность
                if previous is None:  # Удаляем с начала цепочки
                    self.head = current.next
                else:
                    previous.next = current.next

                removed += count

                # Возвращаемся к предыдущему узлу, чтобы продолжить поиск
                current = previous.next if previous else self.head
                continue

            previous = current  # Переходим к следующему шарику
            current = current.next

        return removed  # Возвращаем количество удаленных шариков


def main():
    """Основная функция с пользовательским интерфейсом."""
    print("Программа подсчета удаляемых шариков")
    print("Введите количество шариков и их цвета через пробел")
    print("Пример: 5 1 3 3 3 2")

    while True:
        try:
            user_input = input("Введите данные: ").strip()
            if not user_input:
                print("Ошибка: ввод не может быть пустым. Попробуйте снова.")
                continue

            parts = list(map(int, user_input.split()))
            if len(parts) < 2:
                print("Ошибка: нужно ввести как минимум количество шариков и один цвет. Попробуйте снова.")
                continue

            n = parts[0]
            if n != len(parts) - 1:
                print(f"Ошибка: указано {n} шариков, но введено {len(parts) - 1} цветов. Попробуйте снова.")
                continue

            if n < 1 or n > 10 ** 5:
                print("Ошибка: количество шариков должно быть от 1 до 100000. Попробуйте снова.")
                continue

            balls = parts[1:]
            if any(ball < 0 or ball > 9 for ball in balls):
                print("Ошибка: цвета шариков должны быть числами от 0 до 9. Попробуйте снова.")
                continue

            chain = BallChain(balls)
            removed = chain.process_chain()
            print(f"Результат: {removed}")
            another = input("Хотите проверить другую цепочку? (да/нет): ").lower()
            if another != 'да':
                break

        except ValueError:
            print("Ошибка: все вводимые значения должны быть целыми числами. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}. Попробуйте снова.")


if __name__ == "__main__":
    main()
