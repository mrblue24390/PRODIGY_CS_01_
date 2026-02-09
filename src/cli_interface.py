# Encrypt a message
python src/caesar_cipher.py --encrypt --message "Hello World" --shift 3

# Decrypt a message
python src/caesar_cipher.py --decrypt --message "Khoor Zruog" --shift 3

# Encrypt a file
python src/caesar_cipher.py --encrypt --file input.txt --shift 5 --output encrypted.txt
