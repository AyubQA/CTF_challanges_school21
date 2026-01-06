Задание 25: Лог-детектив

Категория: Forensics / Linux
Сложность: Medium

Дан журнал auth.log. Нужно найти IP-адрес, с которого произошла успешная аутентификация, и это будет флагом.

Подсказка:
1. Ищите строки с "Accepted": grep "Accepted" auth.log
2. Или "authentication success": grep "authentication success" auth.log
3. Извлеките IP адреса: grep "Accepted" auth.log | awk '{print $NF}'
4. Формат флага: school21{IP_ADDRESS} (где IP_ADDRESS заменен на найденный адрес)

Команды:
- grep -i "accepted\|success" auth.log
- awk '/Accepted/ {print $NF}' auth.log

