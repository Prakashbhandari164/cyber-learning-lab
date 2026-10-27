<div align="center">

# 🟢 CYBER LEARNING LAB

### `Learn • Practice • Protect`

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:003b00,100:00ff41&height=180&section=header&text=CYBER%20LEARNING%20LAB&fontSize=34&fontColor=00ff41&animation=fadeIn&fontAlignY=38" width="100%" />

**A beginner-friendly cybersecurity learning toolkit built with Python.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-00ff41?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![Learning](https://img.shields.io/badge/Purpose-Education-003b00?style=for-the-badge)](#-responsible-use)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-111111?style=for-the-badge)](#-setup)

</div>

## ⚡ About

Cyber Learning Lab is a small collection of safe, beginner-level Python utilities for learning defensive cybersecurity concepts.

### 🧰 Tools

| Tool | Description |
|---|---|
| `password_checker.py` | Gives basic password-strength feedback locally |
| `hash_tool.py` | Calculates a SHA-256 hash for text |
| `file_integrity.py` | Calculates a file's SHA-256 fingerprint |
| `network_info.py` | Displays basic network configuration for your own device |

## 🚀 Setup

### Termux (Android)

```bash
pkg update
pkg install python git -y
git clone https://github.com/Prakashbhandari164/cyber-learning-lab.git
cd cyber-learning-lab
python password_checker.py
```

### Linux / Windows

Install Python 3.10 or newer, clone the repository, open the project folder, and run a script with `python filename.py`.

No third-party Python packages are required.

## 🧪 Run a tool

```bash
python password_checker.py
python hash_tool.py
python file_integrity.py
python network_info.py
```

## 🔐 Responsible use

- Use these tools only on your own device, files, accounts, and networks, or where you have explicit permission.
- This project does not include password theft, phishing, credential capture, stealth, or unauthorized scanning.
- Do not enter real passwords into online tools. The password checker runs locally and does not save or transmit input.
- Treat hashes as fingerprints, not encryption. Hashing does not make a password recoverable.

## 🗺️ Learning roadmap

1. Python fundamentals and command-line use
2. Password hygiene and multi-factor authentication
3. Hashing and file integrity
4. IP addresses and basic networking
5. Linux permissions, logs, and defensive monitoring
6. Secure coding and responsible disclosure

## 🤝 Contributing

Beginner-friendly improvements, documentation fixes, and safe defensive tools are welcome. Please explain what a tool does and how to test it safely.

## 📄 License

This project is released under the MIT License. See [`LICENSE`](LICENSE).

<div align="center">

**Built for learning. Used responsibly.** 🟢

</div>
