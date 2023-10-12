expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1 Buatlah Fungsi add_expense disini

def add_expense(date, description, amount):
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    expenses.append(new_expense)


# TODO 2 Buatlah Fungsi calculate_total_expense disini
def calculate_total_expenses(expenses): return sum(
    expense['jumlah'] for expense in expenses)

# TODO 3 Buatlah Fungsi get_expenses_by_date disini

def get_expenses_by_date(date):
    return [expense for expense in expenses if expense['tanggal'] == date]

# TODO 4 Buatlah fungsi generate_expenses_report disini

def generate_expenses_report():
    for expense in expenses:
        yield f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}"

# TODO 5 pastikan semua fungsi yang ada sudah berupa pure function


# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command): return input(command)


def add_expense_interactively():
    date = input("Masukan Tanggal Pengeluaran (YYYY-MM-DD): ")
    description = input("Masukan deskripsi pengeluaran: ")
    amount = int(input("Masukan jumlah pengeluaran: "))
    new_expenses = add_expense(date, description, amount)
    print("Pengeluaran berhasil di tambah.")
    return new_expenses


def view_expenses_by_date():
    date = input("Masukan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report():
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report()
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


def main():
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == '1':
            add_expense_interactively()
        elif choice == '2':
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == '3':
            view_expenses_by_date()
        elif choice == '4':
            print("\nLaporan Pengeluaran Harian:")
            view_expenses_report()
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
