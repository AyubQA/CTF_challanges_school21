Задание 37: Анализ памяти

Категория: Forensics (memory dump)
Сложность: Hard

Дан дамп памяти mem.dmp. Нужно найти процесс ssh и извлечь из него пароль (флаг) с помощью volatility.

Подсказка:
1. Установите volatility: pip install volatility3
2. Определите профиль: volatility -f mem.dmp windows.info
3. Найдите процессы: volatility -f mem.dmp windows.pslist
4. Найдите процесс ssh: volatility -f mem.dmp windows.cmdline
5. Дамп процесса: volatility -f mem.dmp windows.memmap -p <PID> -D output/
6. Ищите флаг в дампе: strings output/* | grep school21
7. Или используйте strings напрямую: strings mem.dmp | grep school21

Команды:
- volatility -f mem.dmp windows.pslist
- strings mem.dmp | grep -i "password\|flag\|school21"

