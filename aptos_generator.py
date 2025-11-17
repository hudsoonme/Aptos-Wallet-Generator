import os
from ed25519 import SigningKey

def generate_aptos_wallet():
    # 32 случайных байта — seed/private key
    private_key = os.urandom(32)
    signing_key = SigningKey(private_key)
    public_key = signing_key.verifying_key.to_bytes()

    # Aptos адрес = 0x + 32-байтный публичный ключ (без хэширования!)
    address = "0x" + public_key.hex()

    return {
        "address": address,
        "private_key_hex": private_key.hex(),
        "public_key_hex": public_key.hex()
    }

print("Aptos Wallet Generator\n")
print("-" * 70)

# Генерируем 10 кошельков (измените число при желании)
for i in range(10):
    wallet = generate_aptos_wallet()
    print(f"Кошелёк {i+1}")
    print(f"Адрес:         {wallet['address']}")
    print(f"Приватный ключ: {wallet['private_key_hex']}")
    print(f"Публичный ключ: {wallet['public_key_hex']}")
    print("-" * 70)

print("Готово! Никогда не передавайте приватные ключи третьим лицам.")
