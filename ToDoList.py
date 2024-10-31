to_do_list = []
archived_tasks = []

# Kullanıcıdan alınan girdileri listeye ekleme fonksiyonu
def add_task(to_do_list):
    task = input("Yapılacak görevi gir: ")
    to_do_list.append(task)
    print("Görev Eklendi!")

# Listede bulunan görevleri gösteren fonksiyon
def show_tasks(to_do_list):
    if not to_do_list:  # Boş kontrolü
        print("Yapılacak görev yok.")
    else:
        print("Yapılacak Görevler:")
        for task in to_do_list:
            print("- " + task)

# Listedeki görevleri silen ve arşivleyen fonksiyon
def delete_task(to_do_list, archived_tasks):
    if not to_do_list:  # Boş kontrolü
        print("Liste boş\n")
        return  # Fonksiyondan çık

    task_to_delete = input("Silmek istediğiniz görevi girin: ")

    if task_to_delete in to_do_list:
        to_do_list.remove(task_to_delete)  # Görevi sil
        archived_tasks.append(task_to_delete)  # Silinen görevi arşivle
        print(f"{task_to_delete} görevi silindi ve arşivlendi.")
    else:
        print("Görev listesinde böyle bir görev bulunamadı.")

# Arşivdeki görevleri gösteren fonksiyon
def show_archived_tasks(archived_tasks):
    if not archived_tasks:
        print("Arşivde görev yok.")
    else:
        print("Arşivlenmiş Görevler:")
        for task in archived_tasks:
            print(f"- {task}")

# Ana döngü
while True:
    print("\nTo Do List Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görev Sil")
    print("4. Arşivdeki Görevleri Göster")
    print("5. Çıkış")

    choice = input("Seçiminiz (1/2/3/4/5): ")
    if choice == '1':
        add_task(to_do_list)
    elif choice == '2':
        show_tasks(to_do_list)
    elif choice == '3':
        delete_task(to_do_list, archived_tasks)
    elif choice == '4':
        show_archived_tasks(archived_tasks)
    elif choice == '5':
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
