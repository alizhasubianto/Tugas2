**Alizha - 2106652000 - PBP D**

## TUGAS 3 PBP: Pengimplementasian Data Delivery Menggunakan Django

# Perbedaan JSON, XML, dan HTML
__JSON (JavaScript Object Notation)__
* suatu format yang digunakan untuk menyimpan, membaca, dan menukar informasi dari web server yang ditulis menggunakan JavaScript sehingga informasi tersebut dapat dibaca oleh *user*.
* lebih mudah untuk dibaca.
* Merepresentasikan objek.
* Dapat menyimpan data dalam bentuk array, sehingga lebih mudah dan cepat dalam melakukan transfer data.
* tidak mendukung *namespaces*.
* keamanannya kurang bagus.

__XML(Extensible Markup Languange)__
* Merupakan *mark up language*.
* Lebih sulit untuk dibaca dan diintrepretasikan.
* Menggunakan *tag structure* untuk merepresentasikan item data.
* tidak dapat menyimpan data dalam bentuk array.
* mendukung *namespaces*.
* lebih aman dibandingkan JSON

__HTML(Hypertext Markup Language)__
* Merupakan *mark up language*
* lebih mudah untuk dilihat, dipelajari, dan digunakan.
* keamanannya kurang bagus

# Mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah *platform*?
karena *data delivery* memiliki peran penting sebagai sarana untuk mengirimkan data dari suatu stack ke stack lainnya pada sebuah *platform*, sehingga kita memerlukan *data delivery* dalam mengimplementasikan sebuah *platform*.

# Implementasi Checklist
1. Membuat *virtual environment* dengan menjalankan perintah `python -m venv env` pada cmd
2. Menyalakan *virtual environtment* dengan menjalankan perintah `env\Scripts\activate.bat` pada cmd
3. Membuat suatu aplikasi baru bernama mywatchlist dengan menjalankan perintah `python manage.py startapp mywatchlist`
4. Menambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS pada file settings.py yang ada di dalam folder project_django.
5. Menambahkan models yang terdiri dari watched, title, rating, release_date, dan review pada file models.py yang berada di dalam folder mywatchlist
6. Menjalankan perintah `python manage.py makemigrations`, lalu dilanjutkan dengan `python manage.py migrate`
7. Membuat folder fixtures di dalam folder mywatchlist, lalu pada folder fixtures saya membuat *file* bernama `initial_watchlist.json`. *file* tersebut berisi data-data yang nantinya akan ditampilkan.
8. Menjalankan perintah `python manage.py loaddata initial_watchlist.json`
9. Membuat fungsi `show_my_watchlist`, `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada views.py yang berada pada folder mywatchlist
10. Membuat folder bernama templates di dalam folder mywatchlist, lalu saya membuat *file* bernama `mywatchlist.html` di dalam folder templates yang berisi *file* html.
11. Membuat *file* `urls.py` pada folder mywatchlist yang berisi potongan kode sebagai berikut:
![](mywatchlist\assets\Screenshot 2022-09-22 070421.jpg)
12. Mendaftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan kode `path('mywatchlist/', include('mywatchlist.urls')),`

# Postman
_HTML_
![](mywatchlist\assets\html.jpg)
_JSON_
![](mywatchlist\assets\json.jpg)
_XML_
![](mywatchlist\assets\xml.jpg)
