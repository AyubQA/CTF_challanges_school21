Задание 26: Шифрование с открытым ключом

Категория: Crypto (RSA)
Сложность: Medium

Даны public.pem и зашифрованный файл flag.enc. Нужно расшифровать флаг, подобрав слабый параметр RSA (например, малый модуль).

Подсказка:
1. Просмотрите публичный ключ: openssl rsa -pubin -in public.pem -text -noout
2. Проверьте размер модуля (n) - если он маленький, можно факторизовать
3. Используйте factordb.com или yafu для факторизации
4. Или используйте RsaCtfTool: python RsaCtfTool.py --publickey public.pem --uncipherfile flag.enc
5. После получения приватного ключа: openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag.txt

Примечание: В упрощенной версии ключ может быть очень маленьким для быстрой факторизации.

