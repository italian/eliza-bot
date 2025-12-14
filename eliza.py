import re
import random
import logging

# Словарь правил: ключ — регулярное выражение (raw string),
# значение — список шаблонов ответа.
rules = {
    # Более специфичное правило для "Я хочу ..." должно идти раньше общего "Я ..."
    r"^Я хочу (.*)": ["Зачем ты хочешь %s?"],

    # Правило для фраз, начинающихся с "Я ..."
    r"^Я (.*)": ["Почему ты %s?", "Как давно ты %s?"],

    # Дежурные фразы (если ничего не подошло):
    r"(.*)": ["Расскажи подробнее.", "Интересно...", "Продолжай."],
}


def match_and_respond(message: str):
    """Проверяет `message` по каждому правилу и возвращает первый подходящий ответ.

    - Итерируемся по `rules` в порядке вставки.
    - Используем `re.match` (начало строки) с флагом `IGNORECASE`.
    - Подставляем захваченные группы в шаблон ответа с помощью `%`.
    - Если никакое правило не сработало — возвращаем `None`.
    """
    for pattern, responses in rules.items():
        m = re.match(pattern, message, flags=re.IGNORECASE)
        if not m:
            continue
        template = random.choice(responses)
        groups = m.groups()
        if not groups:
            return template
        try:
            if len(groups) == 1:
                return template % groups[0]
            return template % groups
        except TypeError as e:
            logging.debug("Template formatting failed: %s", e)
            return template


if __name__ == "__main__":
    # Простой интерактивный запуск для ручного тестирования
    try:
        while True:
            text = input('> ')
            resp = match_and_respond(text)
            print(resp or '...')
    except (KeyboardInterrupt, EOFError):
        print('\nДо свидания')
