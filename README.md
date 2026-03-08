# Caesar Cipher - Cyber Security Tool

**Prodigy Infotech Cyber Security Internship - Task 1**

A professional GUI-based Caesar Cipher application built with Python and Tkinter. This tool demonstrates core cryptography concepts including encryption, decryption, brute-force attacks, and frequency analysis.

---

## 📋 Features

### Core Functionality
- **Encryption**: Encrypt text messages using Caesar Cipher with customizable shift values (1-25)
- **Decryption**: Decrypt Caesar-encrypted messages with known shift values
- **Brute Force Attack**: Automatically test all 25 possible shifts to find the original message
- **Frequency Analysis**: Analyze letter frequency distribution in text (useful for cryptanalysis)

### File Operations
- **Encrypt Files**: Encrypt entire text files and save them with `_encrypted.txt` suffix
- **Decrypt Files**: Decrypt encrypted files and save them with `_decrypted.txt` suffix

### User Interface
- **Modern GUI**: Clean, intuitive interface built with Tkinter
- **Real-time Processing**: Instant encryption/decryption results
- **Multi-window Support**: Separate input and output areas for easy workflow
- **Error Handling**: Comprehensive input validation and error messages

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PRODIGY_CS_01.git
   cd PRODIGY_CS_01
   ```

2. **No external dependencies required**
   - Tkinter comes pre-installed with Python on most systems
   - For Windows: Included by default
   - For Linux: `sudo apt-get install python3-tk`
   - For macOS: `brew install python-tk`

### Running the Application

```bash
python caesar_cipher.py
```

---

## 📖 Usage Guide

### Basic Encryption/Decryption
1. Enter your message in the **Input Message** field
2. Set the **Shift Value** (1-25)
3. Click **Encrypt** or **Decrypt**
4. View results in the **Output** panel

### Brute Force Attack
1. Enter an encrypted message in the **Input Message** field
2. Click **Brute Force**
3. The tool will display all 25 possible decryptions
4. Look for readable text to identify the correct shift value

### Frequency Analysis
1. Enter your message or encrypted text in the **Input Message** field
2. Click **Frequency Analysis**
3. View the letter frequency distribution with percentages
4. Use this data to break substitution ciphers

### File Encryption
1. Click **Encrypt File**
2. Select a text file to encrypt
3. Confirm the shift value
4. Encrypted file will be saved in the same directory

---

## 🔐 Caesar Cipher Explained

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It works by:

- **Shifting** each letter in the plaintext by a fixed number of positions in the alphabet
- **Preserving** uppercase/lowercase and non-alphabetic characters
- **Wrapping around** the alphabet (Z→A)

### Example
```
Original:  Hello World
Shift by 3: Khoor Zruog
```

### Security Note
⚠️ The Caesar Cipher is **NOT secure** for real-world use. It:
- Has only 25 possible keys
- Is vulnerable to frequency analysis
- Can be broken in seconds
- Is used here for **educational purposes only**

For modern cryptography, use AES, RSA, or other industry-standard algorithms.

---

## 🛠️ Technical Details

### Architecture
- **Object-Oriented Design**: `CaesarCipherGUI` class encapsulates all functionality
- **Event-Driven GUI**: Button clicks trigger appropriate encryption/decryption operations
- **Text Processing**: Handles multi-line input with scrollable text widgets
- **File I/O**: Secure file handling with encoding support

### Key Methods
- `encrypt_text(message, shift)`: Core encryption algorithm
- `decrypt_text(message, shift)`: Core decryption algorithm
- `brute_force()`: Tests all shift values
- `frequency_analysis()`: Calculates letter frequencies
- `encrypt_file()`: File encryption wrapper
- `decrypt_file()`: File decryption wrapper

---

## 📊 Learning Outcomes

By working through this project, you'll understand:
1. **Cryptography Basics**: How substitution ciphers work
2. **Python GUI Development**: Building professional applications with Tkinter
3. **Cryptanalysis**: Techniques like frequency analysis and brute-force attacks
4. **File Handling**: Reading and writing encrypted files
5. **User Experience**: Designing intuitive interfaces

---

## 📁 Project Structure

```
PRODIGY_CS_01/
├── caesar_cipher.py      # Main application file
├── README.md             # This file
├── requirements.txt      # Python dependencies (minimal)
└── .gitignore           # Git ignore rules
```

---

## 🔄 Version History

### v1.0 (Initial Release)
- ✅ GUI-based encryption/decryption
- ✅ Brute force attack feature
- ✅ Frequency analysis tool
- ✅ File encryption/decryption
- ✅ Input validation and error handling

---

## 🤝 Contributing

This is a learning project for Prodigy Infotech internship. Feel free to:
- Add more cipher types (Vigenère, Rail Fence, etc.)
- Improve the UI with additional features
- Add unit tests for validation
- Optimize algorithms

---

## 📝 License

This project is created for educational purposes as part of the Prodigy Infotech Cyber Security Internship.

---

## 📧 Contact & Support

For questions or suggestions, feel free to reach out through:
- **Email**: your.email@domain.com
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [@yourusername](https://github.com/yourusername)

---

## 🎓 Learning Resources

- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Python Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Cryptography Basics](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis)

---

**Happy Learning! 🚀**

*Made with ❤️ for the Prodigy Infotech Cyber Security Internship*
