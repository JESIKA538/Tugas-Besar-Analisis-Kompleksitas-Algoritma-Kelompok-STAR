# =========================================
# Analisis Waktu Eksekusi Algoritma
# Brute Force Perpangkatan (Iteratif & Rekursif)
# =========================================

import time
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Fungsi pangkat iteratif
def pangkat_iteratif(a, n):
    hasil = 1
    for _ in range(n):
        hasil *= a
    return hasil

# Fungsi pangkat rekursif
def pangkat_rekursif(a, n):
    if n == 0:
        return 1
    return a * pangkat_rekursif(a, n - 1)

def main():
    a = 2
    n_list = [5, 10, 15, 30, 50, 100, 500, 1000]
    ULANG = 10000
    data = []

    print("Menghitung waktu eksekusi...\n")

    # Fungsi agar rekursi besar tidak error
    sys.setrecursionlimit(max(sys.getrecursionlimit(), max(n_list) + 100))

    for n in n_list:
        # Brute Force Iteratif
        start = time.perf_counter()
        for _ in range(ULANG):
            pangkat_iteratif(a, n)
        end = time.perf_counter()
        waktu_iter = (end - start) * 1e6 / ULANG

        # Brute ForceRekursif
        start = time.perf_counter()
        for _ in range(ULANG):
            pangkat_rekursif(a, n)
        end = time.perf_counter()
        waktu_rek = (end - start) * 1e6 / ULANG

        data.append([n, waktu_iter, waktu_rek])
        print(f"n={n:4d} | Iteratif={waktu_iter:.4f} µs | Rekursif={waktu_rek:.4f} µs")

    # Untuk menyimpan hasil ke CSV
    df = pd.DataFrame(data, columns=["n", "iteratif", "rekursif"])
    df.to_csv("data_waktu_python.csv", index=False)

    # Fungsi menampilkan grafik
    plt.plot(df["n"], df["iteratif"], marker='o', label="Iteratif")
    plt.plot(df["n"], df["rekursif"], marker='s', label="Rekursif")
    plt.xlabel("Nilai n")
    plt.ylabel("Waktu Eksekusi (µs)")
    plt.title("Perbandingan Waktu Eksekusi Brute Force")
    plt.legend()
    plt.grid(True)
    plt.savefig("grafik_waktu_python.png")
    plt.show()

    print("\nData disimpan di: data_waktu_python.csv")
    print("Grafik disimpan di: grafik_waktu_python.png")

if __name__ == "__main__":
    main()
