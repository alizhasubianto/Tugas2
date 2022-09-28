**Alizha - 2106652000 - PBP D**

# TUGAS 4 PBP: Pengimplementasian Form dan Autentikasi Menggunakan Django

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Kegunaan {% csrf_token %} pada elemen form adalah untuk menghindari serangan *Cross-Site Request Forgery* (CSRF)yang dapat membahayakan keamanan aplikasi web. {% csrf_token %} akan menghasilkan token rahasia dan unik yang di*generate* oleh aplikasi server dalam permintaan HTTP berikutnya yang dibuat oleh klien. Setelah permintaan dibuat, server akan membandingkan dua token yang ditemukan di *user session* dan *request*. Sehingga, jika tidak terdapat potongan kode {% csrf_token %} pada program, maka tidak akan ada token yang dihasilkan. Apabila tidak terdapat token, *request* akan ditolak, *user session* dihentikan, dan aktivitas dapat dinilai sebagai potensi serangan CSRF.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

## Implementasi Checklist
1. Menjalankan perintah `python manage.py startapp todolist` pada *virtual environment* untuk membuat aplikasi todolist
2. Mendaftarkan aplikasi todolist dengan menambahkan `'todolist'` pada variabel `INSTALLED_APPS` di *file* `settings.py` yang terdapat pada folder `project_django`
3. Membuat model Task dengan membuat sebuah class bernama task yang terdiri dari variabel user, date, title, description, dan is_finished pada file models.py yang berada di dalam folder mywatchlist.
4. Menjalankan perintah `python manage.py makemigrations`, lalu dilanjutkan dengan `python manage.py migrate`.
5. Membuat *file* forms.py pada folder todolist sebagai form yang digunakan pada saat ingin membuat task baru.
6. M 