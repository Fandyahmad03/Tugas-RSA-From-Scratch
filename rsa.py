# ============================================
# IMPLEMENTASI RSA DARI NOL SES
# ============================================

# Fungsi untuk mencari GCD (FPB)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Extended Euclidean Algorithm
def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y


# Fungsi mencari modular inverse
def mod_inverse(e, phi):
    gcd_val, x, y = extended_euclidean(e, phi)
    if gcd_val != 1:
        return None
    return x % phi


# Modular Exponentiation (efisien)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod

        exp = exp // 2
        base = (base * base) % mod

    return result


# ============================================
# PROGRAM UTAMA
# ============================================

print("=== PROGRAM RSA DARI NOL ===")

# Input bilangan prima
p = int(input("Masukkan bilangan prima p: "))
q = int(input("Masukkan bilangan prima q: "))

# Hitung n dan phi
n = p * q
phi = (p - 1) * (q - 1)

print("n = p * q =", n)
print("phi(n) =", phi)

# Input nilai e
e = int(input("Masukkan nilai e (relatif prima dengan phi): "))

# Cek apakah e valid
if gcd(e, phi) != 1:
    print("Error: e tidak relatif prima dengan phi!")
    exit()

# Hitung d
d = mod_inverse(e, phi)

print("Public Key  =", (e, n))
print("Private Key =", (d, n))

# Enkripsi
message = int(input("Masukkan plaintext (angka kecil): "))
cipher = mod_exp(message, e, n)

print("Ciphertext =", cipher)

# Dekripsi
decrypted = mod_exp(cipher, d, n)
print("Hasil Dekripsi =", decrypted)