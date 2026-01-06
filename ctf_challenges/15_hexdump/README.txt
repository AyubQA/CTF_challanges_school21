Задание 15: Найдите флаг в hex дампе файла.

Подсказка: Используйте grep для поиска или xxd для работы с hex.
Команды: grep -r 'school21' .
         xxd -r dump.hex  # конвертация hex в бинарный
         strings dump.hex | grep school21
