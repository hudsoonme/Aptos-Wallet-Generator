# Aptos Wallet Generator (Python)

100% рабочий генератор Aptos-кошельков (Ed25519 + правильный hex-адрес 0x…).  
Адреса полностью совместимы с Petra, Martian, Pontem, Fewcha и всеми Aptos-экосистемными кошельками.

## Установка и запуск: 

```bash
# 1. Клонируем репозиторий
git clone https://github.com/hudsoonme/aptos-wallet-generator.git
cd aptos-wallet-generator

# 2. Создаём виртуальное окружение (рекомендуется)
python -m venv venv
source venv/bin/activate      # Linux / macOS
# или
venv\Scripts\activate         # Windows

# 3. Устанавливаем минимальные зависимости
pip install ed25519

# 4. Запускаем генератор (по умолчанию создаст 10 кошельков)
python aptos_generator.py

## Пример вывода

----------------------------------------------------------------------
Кошелёк 1
Адрес:         0x3f4a9b8c2d1e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a
Приватный ключ: 3f4a9b8c2d1e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a
Публичный ключ: 8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b
----------------------------------------------------------------------
