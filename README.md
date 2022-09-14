**Nama   : Alizha**
**NPM    : 2106652000**
**Kelas  : D**

## TUGAS 2 - PBP

__Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;__
   ![https://raw.githubusercontent.com/alizhasubianto/Tugas2/main/assets/bagan.jpg](assets\bagan.jpg)

__Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?__

<<<<<<< HEAD
   *Virtual environment* adalah _tools_ yang digunakan sebagai wadah untuk mengenkapsulasi serta menampung *package* atau *library* agar tetap terisolasi. Virtual environment dibutuhkan dan berperan penting dalam pembuatan aplikasi *web* untuk mencegah adanya *issues dependency* yang dapat terjadi akibat adanya pembaruan perbedaan versi pada *external library* dari *project* yang satu dengan yang lainnya. Singkatnya, jika kita tidak menggunakan *virtual environtment*, maka kita tidak dapat bekerja menggunakan dua *library* dengan versi yang berbeda. Namun, kita masih tetap dapat membuat aplikasi *web* berbasis Django tanpa menggunakan virtual environment, tetapi saat kita sedang mengerjakan project secara individu, bukan sebagai tim. karena jika mengerjakan project sebagai tim tanpa environment, akan sulit apabila masing-masing individu dalam tim memiliki modul atau versi yang berbeda-beda.

__Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas__

* Hal pertama yang saya lakukan untuk melakukan pengambilan data dari model adalah membuat *function* show_catalog yang menerima parameter request pada *file* views.py yang terdapat pada *folder* katalog dan me*return* render(request, 'katalog.html', context). Data yang ada pada parameter ketiga yaitu variabel context tersebut akan ikut di*render* untuk memunculkan data pada halaman HTML.

* Selanjutnya, saya membuat *routing* untuk memetakan fungsi yang telah dibuat pada views.py, sehingga nantinya halaman HTML dapat ditampilkan pada *browser*, yaitu dengan membuat variabel app_name yang berisikan string katalog, serta membuat variabel url_patterns berisikan list berupa path dengan *route* '' dan fungsi show_catalog dari  views.py dengan argumen 'show_catalog' pada urls.py yang terdapat pada *folder* templates. Setelah itu, aplikasi katalog didaftarkan ke dalam urls.py yang ada pada *folder* project_django dengan menambahkan path('katalog/', include('katalog.urls')) pada variabel url_patterns.

* Selanjutnya, data yang didapatkan, yaitu data yang telah diolah pada models  perlu dipetakan pada katalog.html dengan menambahkan kode { Name } dan { Student_ID }, dan mengisi field pada *template* dengan memanggil method/atribut yang ada pada class catalog_items pada file models.py yang nantinya akan ditampilkan pada halaman HTML.

* Kemudian, yang dilakukan pertama kali saat *deployment* adalah *create new app*. Lalu setelah itu, saya menuliskan nama aplikasi yang akan di*deploy*. Pada tugas ini, saya menggunakan nama tugas2-alizha sebagai nama dari aplikasinya. Setelah aplikasi telah diberi nama, tambahkan Config Vars dengan variabel bernama HEROKU_APP_NAME dan SECRET_KEY sebagai *key*, nama aplikasi dan *key secrets*nya sebagai *value*. Selanjutnya, tambahkan *file* dpl.yml yaitu berkas yang digunakan untuk mengeksekusi *deployment* oleh *runner* di GitHub Actions. Setelah itu, hubungkan *repository-repository* yang ada di github lalu deploy dengan pilih Deploy Branch.
=======
   *Virtual environment* adalah _tools_ yang digunakan sebagai wadah untuk mengenkapsulasi serta menampung *package* atau *library* agar tetap terisolasi. Virtual environment dibutuhkan dan berperan penting dalam pembuatan aplikasi *web* untuk mencegah adanya *issues dependency* yang dapat terjadi akibat adanya pembaruan perbedaan versi pada *external library* dari *project* yang satu dengan yang lainnya. Singkatnya, jika kita tidak menggunakan *virtual environtment*, maka kita tidak dapat bekerja menggunakan dua *library* dengan versi yang berbeda. Namun, kita masih tetap dapat membuat aplikasi *web* berbasis Django tanpa menggunakan 
>>>>>>> d4f6a0d45e78bf88258d0d5d00c61b0fa098c4e3
