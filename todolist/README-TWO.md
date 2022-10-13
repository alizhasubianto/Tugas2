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
Melalui *browser*, AJAX akan meminta data dari *web server*, JavaScript, dan HTML DOM untuk menampilkan data, lalu data tersebut akan dikirimkan oleh AJAX menggunakan data teks, JSON, ataupun XML. Di balik layar, data pada halaman *web* akan diperbarui secara asinkronus dengan mengirimkan data ke *server*, artinya kita dapat memperbarui sebagian elemen data pada halaman tanpa harus me*reload* keseluruhan halaman.

## Implementasi *Checklist*
1. Membuat *view* baru yang mengembalikan seluruh data *task* ke dalam bentuk JSON dengan membuat *function* baru yang bernama show_json_by_id dan create_task_ajax yang mengembalikan JsonResponse.
```
@login_required(login_url='/todolist/login/')
@csrf_exempt
def show_json_by_id(request):
    data = Task.objects.filter(user=request.user).order_by('id')
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def create_task_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        task_item = Task.objects.create(
            user=user, 
            title=title, 
            description=description
        )
        task_item.save()
        return JsonResponse({"instance": "Task successfully added!"}, status=200)
```
2. Membuat *path* /todolist/json yang mengarah ke *view* baru dengan menambahkan *routing* `/json` dan `/add` di variabel urlpatterns di *file* urls.py yang ada di folder todolist.
3. Membuat modal popup untuk menambahkan *task* yang terhubung dengan tombol Add Task.
4. Menerapkan AJAX GET untuk melakukan pengambilan data *task*.

## Link Heroku
Akses [di sini](https://tugas2-alizha.herokuapp.com/todolist)
