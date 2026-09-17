# SCT_CS_1
# Caesar Cipher Python Tool

A lightweight, interactive Command Line Interface (CLI) application built in Python to encrypt and decrypt text messages using the classic **Caesar Cipher** substitution algorithm.

---

## 📌 Features

- **Encryption & Decryption:** Seamlessly encrypt plain text or decrypt cipher text using any integer shift key.
- **Case Sensitivity:** Preserves original character casing (uppercase remains uppercase, lowercase remains lowercase).
- **Special Character Handling:** Non-alphabetic characters (spaces, numbers, punctuation, symbols) pass through unchanged.
- **Wrap-around Support:** Uses modulo arithmetic to handle arbitrary shift keys, including values larger than 25 or negative integers.
- **Interactive CLI:** Interactive user input with error handling for smooth terminal operations.

---

## 🛠️ Requirements

- **Python 3.6+** (No external dependencies required — standard Python library only).

---

## 🚀 Quick Start

### 1. Clone the Repository



git clone [https://github.com/YOUR-USERNAME/caesar-cipher.git](https://github.com/YOUR-USERNAME/caesar-cipher.git)

cd caesar-cipher

2. Run the Program



python main.py

💡 How It Works

The Caesar Cipher is a classic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

Encryption: E(x) = (x + n) mod 26

Decryption: D(x) = (x - n) mod 26

where x is the letter's index (0–25) and n is the shift key.

📖 Example Usage

Encrypting a Message


--- Caesar Cipher Program ---

Select an option:
1. Encrypt message
2. Decrypt message
3. Exit
Enter choice (1, 2, or 3): 1

Enter the message to encrypt: Hello, World! 123
Enter the shift value (e.g., 3): 3

Result (Encrypted): Khoor, Zruog! 123

Decrypting a Message


Select an option:
1. Encrypt message
2. Decrypt message
3. Exit

Enter choice (1, 2, or 3): 2

Enter the message to decrypt: Khoor, Zruog! 123
Enter the shift value (e.g., 3): 3

Result (Decrypted): Hello, World! 123

📁 Repository Structure

caesar-cipher/
│
├── main.py          # Main Python program containing cipher logic & CLI
├── README.md        # Project documentation
└── .gitignore       # Git ignore rules for Python environment

📜 License

This project is open-source and available under the MIT License.
