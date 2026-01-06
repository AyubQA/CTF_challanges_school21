Задание 34: Сжатый след

Категория: Forensics / Linux
Сложность: Hard

Дан файл log.gz — сжатый журнал. Нужно найти в нём строку, содержащую флаг, используя zcat, grep и т.д.

Подсказка:
1. Используйте zcat: zcat log.gz | grep school21
2. Или zgrep: zgrep school21 log.gz
3. Или распакуйте: gunzip log.gz и затем grep log
4. Или less: less log.gz (автоматически распакует)
5. Или zless: zless log.gz

Команды:
- zcat log.gz | grep school21
- zgrep -r school21 log.gz
- gunzip log.gz && grep school21 log

