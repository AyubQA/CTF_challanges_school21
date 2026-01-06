Задание 36: Спрятанный в бинарнике

Категория: Forensics / Stegano
Сложность: Medium

В исполняемом файле program в секции .data записан флаг в hex-виде. Нужно извлечь его с помощью strings или xxd.

Подсказка:
1. Используйте strings: strings program | grep school21
2. Или xxd: xxd program | grep school21
3. Или objdump: objdump -s -j .data program
4. Или readelf: readelf -x .data program
5. Или hexdump: hexdump -C program | grep school21

Команды:
- strings program
- xxd program | less
- objdump -s program
- readelf -a program

