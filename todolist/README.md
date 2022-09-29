**Alizha - 2106652000 - PBP D**

# TUGAS 4 PBP: Pengimplementasian Form dan Autentikasi Menggunakan Django

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
Kegunaan {% csrf_token %} pada elemen form adalah untuk menghindari serangan *Cross-Site Request Forgery* (CSRF)yang dapat membahayakan keamanan aplikasi web. {% csrf_token %} akan menghasilkan token rahasia dan unik yang di*generate* oleh server dalam permintaan HTTP berikutnya yang dibuat oleh klien. Setelah permintaan dibuat, server akan membandingkan dua token yang ditemukan di *user session* dan *request*. Sehingga, jika tidak terdapat potongan kode {% csrf_token %} pada program, maka tidak akan ada token yang dihasilkan. Apabila tidak terdapat token, *request* akan ditolak, *user session* dihentikan, dan aktivitas dapat dinilai sebagai potensi serangan CSRF.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, Bisa. Kita bisa membuat elemen <form> manual tanpa menggunakan generator dengan menggunakan method post yang diisi csrf token. Setelah itu, input fields dapat dibuat dengan menggunakan HTML. Kemudian, setelah form disubmit, kita dapat men-*trigger* input yang dimasukkan dengan method `request.POST.get`

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pada saat user melakukan submisi form atau menekan tombol login, logout, dan sebagainya, browser akan meng-*generate* HTTP Request, *method*, dan argumen ke URL tujuan berdasarkan HTML page form. Setelah itu, server akan menerima HTTP Request yang diberikan oleh user dan server akan memilih fungsi pada views.py dan memilih path mana yang akan dihandle. Kemudian, views.py akan melakukan sesuatu sesuai kode yang terdapat di dalamnya. Lalu, server akan meng-*generate* halaman HTML, sehingga HTML *layout* dapat ditampilkan kepada user.

## Implementasi Checklist
1. Menjalankan perintah `python manage.py startapp todolist` pada *virtual environment* untuk membuat aplikasi todolist. Lalu aplikasi todolist didaftarkan dengan menambahkan `'todolist'` pada variabel `INSTALLED_APPS` di *file* `settings.py` yang terdapat pada folder `project_django`.
2. Menambahkan potongan kode `path('todolist/', include('todolist.urls')),` pada variabel urlpatterns di *file* urls.py yang berada di folder project_django
3. Membuat model Task dengan membuat sebuah class bernama `Task` yang terdiri dari variabel user, date, title, description, dan is_finished pada file models.py yang berada di dalam folder todolist. Setelah itu, saya menjalankan perintah `python manage.py makemigrations`, lalu dilanjutkan dengan `python manage.py migrate`.
5. Membuat fungsi show_todolist, status, dan delete yang terhubung ke todolist.html, fungsi create_task yang terhubung ke create_task, fungsi login yang terhubung ke login.html, serta fungsi logout yang terhubung ke logout.html. Pada Fungsi show_todolist, status, delete, dan create_task, ditambahkan potongan kode, yaitu `login_required(login_url='/todolist/login')` untuk membuat restriksi, sehingga user harus login terlebih dahulu untuk mengaksesnya.
6. Membuat *folder* baru bernama `templates` berisikan *file-file* yang terdiri dari todolist.html yang dapat menampilkan tombol `create new task`, `logout`, serta tabel todolist. Selain itu, dibuat juga `file` createtask.html sebagai tampilan untuk *user* saat ingin menambahkan *task* baru, login.html, register.html, dan juga logout.html.
7. Lalu, dibuat *file* forms.py pada folder todolist yang digunakan untuk membuat halaman form saat *user* ingin membuat task baru (saat klik create new task). *file* forms.py terhubung dengan createtask.html dan fungsi create_task di todolist/views.py sehingga nantinya pada createtask.html form bisa dibuat dengan menggunakan generator `form.as_table`.
8. Membuat *file* bernama urls.py untuk melakukan *routing* fungsi-fungsi yang terdapat pada views.py dengan membuat variabel urlpatterns dan menambahkan kode berikut:
```
urlpatterns = [ 
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('create-task/', create_task, name='create_task'),
    path('status/<int:id>/', status, name='status'),
    path('delete/<int:id>/', delete, name='delete'),
]
```
9. Django di*deploy* ke heroku dan membuat dua user dengan masing-masing 3 dummy list to do.


## Link Django
Akses [di sini](https://tugas2-alizha.herokuapp.com/todolist/login/?next=/todolist/)