
import interest
import display

def main():
    print("=== Program Kalkulator Bunga Tabungan ===")

    try:
        principal = float(input("Masukkan saldo awal (contoh: 80000): "))
        rate = float(input("Masukkan bunga tahunan (misal 5%): ")) / 100
        years = int(input("Masukkan lama menabung (tahun): "))

        ci = interest.compound_interest(principal, rate, years)
        si = interest.simple_interest(principal, rate, years)

        display.print_result(principal, rate, years, ci, si)

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    main()

# Masukkan pada terminal: python main.py