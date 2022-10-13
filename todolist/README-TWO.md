**Alizha - 2106652000 - PBP D**

# TUGAS 6 PBP: Javascript dan AJAX

##  Jelaskan perbedaan antara *asynchronous programming* dengan *synchronous programming*.
* *Asynchronus programming*
1. Program aplikasi dapat dijalankan secara paralel (*multi-thread*).
2. Dapat mengirimkan lebih dari satu *request* ke *server*
3. Dapat meningkatkan *throughput* karena beberapa operasi dapat dijalankan secara bersamaan
* *Synchronus programming*
1. Hanya dapat menjalankan satu operasi/program pada satu waktu (*single-thread*)
2. Hanya dapat mengirimkan satu *request* dalam satu waktu ke *server* dan membutuhkan waktu hingga *request* dijawab oleh *server*
3. Eksekusi *synchronus programming* lebih lambat dibandingkan *asynchronus programming*

##  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
*Event Driven Programming* adalah salah satu teknik pemrograman yang memiliki konsep kerja tergantung dari kejadian/*event* tertentu. *Event driven programming* juga dapat dianggap sebagai paradigma pemrograman yang alur programnya ditentukan oleh suatu *event*  yang merupakan *output* pengguna atau pesan dari program lainnya.

Contoh penerapan:
Saat *user* menekan tombol save pada modal pop up *add task*, *event* tersebut akan di*handle* oleh AJAX untuk mengirimkan data *task* baru yang sebelumnya ditambahkan ke *server*. Setelah data dikirim ke *server*, AJAX akan meng*update* *task* baru tersebut, sehingga *task* baru akan muncul pada halaman todolist.

## Jelaskan penerapan asynchronous programming pada AJAX.
Melalui *browser*, AJAX akan meminta data dari *web server*, JavaScript, dan HTML DOM untuk menampilkan data, lalu data tersebut akan dikirimkan oleh AJAX menggunakan data teks, JSON, ataupun XML. Di balik layar, secara asinkronus data akan diperbarui dengan mengirimkan data ke *server* di balik layar.

## Implementasi *Checklist*
