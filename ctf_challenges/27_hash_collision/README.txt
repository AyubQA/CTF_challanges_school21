Задание 27: Хэш-коллизия

Категория: Crypto (хэши)
Сложность: Hard

Даны два разных файла file1.bin и file2.bin, которые имеют одинаковый MD5-хэш. Нужно найти флаг, скрытый в одном из них.

Подсказка:
1. Проверьте хэши: md5sum file1.bin file2.bin
2. Убедитесь, что хэши одинаковые
3. Ищите флаг в содержимом файлов:
   - strings file1.bin | grep school21
   - strings file2.bin | grep school21
   - xxd file1.bin | grep school21
4. Или используйте hexdump: hexdump -C file1.bin | grep school21

Это демонстрирует уязвимость MD5 - два разных файла могут иметь одинаковый хэш.

