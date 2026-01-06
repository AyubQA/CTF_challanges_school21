Задание 33: Метаданные документа

Категория: Forensics (метаданные)
Сложность: Medium

В PDF-файле report.pdf в свойствах документа скрыт флаг. Нужно использовать pdfinfo или exiftool.

Подсказка:
1. Используйте exiftool: exiftool report.pdf
2. Или pdfinfo: pdfinfo report.pdf
3. Или strings: strings report.pdf | grep school21
4. Проверьте все метаданные: автор, заголовок, ключевые слова, комментарии
5. Или используйте Python: pip install PyPDF2 и извлеките метаданные

Команды:
- exiftool report.pdf
- pdfinfo report.pdf
- strings report.pdf | grep -i "flag\|school21"

