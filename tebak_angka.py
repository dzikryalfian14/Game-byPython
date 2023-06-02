import random

def main():
    print("=== Tebak Angka ===")
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Tebak angka (1-20): "))
        attempts += 1

        if guess < secret_number:
            print("Terlalu rendah!")
        elif guess > secret_number:
            print("Terlalu tinggi!")
        else:
            print(f"Selamat, Anda berhasil menebak angka {secret_number}!")
            print(f"Anda melakukan {attempts} percobaan.")
            break

if __name__ == "__main__":
    main()
