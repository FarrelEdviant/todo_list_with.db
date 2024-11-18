import sqlite3

# Database setup
def setup_database():
    """Membuat database dan tabel tasks jika belum ada."""
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Database operations
def get_tasks():
    """Mengambil semua tugas dari database."""
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task_to_db(task):
    """Menambahkan tugas baru ke database."""
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def remove_task_from_db(task_id):
    """Menghapus tugas dari database berdasarkan ID."""
    conn = sqlite3.connect("todo_list.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Menu fungsi
def display_menu():
    """Menampilkan menu pilihan."""
    print("\nMenu To-Do List:")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def view_tasks():
    """Menampilkan semua tugas dalam daftar."""
    tasks = get_tasks()
    if not tasks:
        print("\nDaftar tugas Anda kosong!")
    else:
        print("\nDaftar Tugas Anda:")
        for task_id, task in tasks:
            print(f"{task_id}. {task}")

def add_task():
    """Meminta pengguna untuk menambahkan tugas baru."""
    task = input("\nMasukkan tugas baru: ").strip()
    if task:
        add_task_to_db(task)
        print(f'"{task}" telah ditambahkan ke daftar tugas Anda.')
    else:
        print("Tugas tidak boleh kosong.")

def remove_task():
    """Meminta pengguna untuk menghapus tugas berdasarkan ID."""
    view_tasks()
    tasks = get_tasks()
    if tasks:
        try:
            task_id = int(input("\nMasukkan ID tugas yang ingin dihapus: "))
            if any(task_id == task[0] for task in tasks):
                remove_task_from_db(task_id)
                print(f"Tugas dengan ID {task_id} telah dihapus dari daftar tugas Anda.")
            else:
                print("ID tugas tidak valid.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

# Main program
def main():
    setup_database()
    while True:
        display_menu()
        choice = input("\nPilih opsi (1-4): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nKeluar dari To-Do List. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Harap pilih opsi yang benar.")

if __name__ == "__main__":
    main()
