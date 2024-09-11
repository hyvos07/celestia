<a id="readme-top"></a>

# <p align="center"><img src="assets\logo\Horizontal.png" style="max-width: 350px;" alt="Celestia"></p>

Celestia is a Hoyoverse Official Merchandise E-Commerce that offers some products officially made by Hoyoverse. This Project was made for one of the task in <a href="https://pbp-fasilkom-ui.github.io/ganjil-2025/"> Pemrograman Berbasis Platform (PBP) Gasal 2024/2025</a>.

<br>

> **Note:** <br> This is not an actual online shop for Hoyoverse Merchandise.

<br>

# ⚙️ Deployment and Usage
The deployed project is on PWS (Pacil Web Service), which can be accessed [here](http://daniel-liman-celestia.pbp.cs.ui.ac.id/).

If you want to try and run the project from your local device, open http://127.0.0.1:8000 or http://localhost:8000 with your browser to see the result.

<br>

# 📝 Assignment
**Nama**    : Daniel Liman<br>
**NPM**     : 2306220753<br>
**Kelas**   : PBP F
<br>
<br>

## Tugas 2
### Step by Step Pembuatan Project Django
1. Membuat direktori baru bernama `celestia` dan inisiasi *local repository* di folder tersebut.

2. Membuat GitHub repository yang dihubungkan dengan *local repository* `celestia`

3. Membuat *virtual environment* baru dan jalankan env tersebut untuk project ini dengan *command*:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
4. Membuat file `requirements.txt` yang berisi:
    ```txt
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    dan meng-*install requirements* tersebut dengan pip.
    ```bash
    pip install -r requirements.txt
    ```

5. Membuat proyek Django baru dengan *command*:
    ```bash
    django-admin startproject celestia .
    ```
    Lalu melakukan beberapa penyesuaian di `settings.py` untuk project yang baru dibuat tersebut.

6. Membuat aplikasi dengan nama `main` pada proyek ini dengan menjalankan *command*:
    ```bash
    python manage.py startapp main
    ```
    setelah dibuat, aplikasi `main` juga perlu ditambahkan ke `celestia/settings.py` pada variable `INSTALLED_APPS` agar dapat menjalankan aplikasi `main` tersebut.

7. Membuat model `Product` dengan atribut sebagai berikut:
    ```python
    name: CharField,
    price: IntegerField,
    description: TextField,
    stock: IntegerField,
    chara: CharField,
    game: CharField,
    category: CharField,
    image: TextField,
    price_with_comma: int,      # Internal Property
    image_URL : String,         # Internal Property
    is_stock_empty: bool,       # Internal Property
    ```
    **N.B.** <br> Ada beberapa *field* yang masih dalam bentuk sederhana, sehingga tidak ada di dalam bentuk aslinya (seperti `image` yang seharusnya menggunakan `ImageField`) agar dapat lebih diperdalam di minggu-minggu berikutnya.

8. Membuat function `show_main()` pada `views.py` untuk bisa me-*return* template HTML bernama `main.html` yang dibuat di direktori `templates`. <br> HTML tersebut akan menampilkan nama aplikasi, data dari `show_main()` dan identitas diri sendiri.

9. Membuat sebuah *routing* pada `urls.py` dalam direktori aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`. Di `urls.py`, ditambahkan `path('', show_main, name='show_main')` ke dalam `urlpatterns` milik aplikasi `main`.

10. Terakhir, *push* kode ke GitHub dan lakukan *deployment* ke PWS agar dapat diakses oleh orang lain. Hasil *deployment* dari proyek ini dapat diakses di bagian [atas](#readme-top).

### Bagan Gambaran Request Client ke Django

<img alt="Django MVT Flow" src="assets\assignment\Django MVT.png" />

Penjelasan lanjutan tentang kaitan `urls.py`, `views.py`, `models.py`, dan berkas HTML untuk sebagai *template*:
- `urls.py` dalam Django Project akan menentukan *views* apa yang perlu dikembalikan ke pihak *client* berdasarkan ***request*** yang dikirim oleh *client*.
- `views.py` menyimpan *business logic* dan pemrosesan data yang diminta pada ***request*** dari *client*. Hasil data dari *views* tersebut dapat dikembalikan bersama dengan tampilan web dari *template* `.html` yang dibuat.
- *Template* HTML berfungsi untuk mengembalikan ***response*** berupa sebuah *web page* kepada *client*, dengan tampilan sesuai dengan apa yang sudah diminta oleh *client* sebelumnya.
- `models.py` berfungsi sebagai jembatan perantara antara *database* dan *views*. Di dalam `models.py`, disimpan bentuk model dari data yang ada di dalam *database*. Dengan `models.py`, `views.py` juga dapat berinteraksi dan mengambil data-data dari *database* sehingga data-data tersebut dapat diproses untuk memenuhi permintaan ***request***.

### Fungsi `git` pada Pengembangan Perangkat Lunak

Dalam proses pengembangan perangkat lunak, `git` memiliki banyak kegunaan pada aspek-aspek yang melibatkan kolaborasi antar sesama *developer* dan manajemen pengelolaan dari suatu proyek *software application*. Aspek-aspek tersebut dapat dijabarkan sebagai berikut.

1. ***Version Control*** <br>
`git` dapat menyimpan perubahan kode dari suatu proyek secara rinci. Setiap kali ada perubahan pada kode, seorang *developer* dapat mencatatnya di `git` sebagai sebuah ***commit***, sehingga *developer* tersebut maupun rekannya dapat mengetahui detail dari siapa, kapan, dan alasan perubahan kode tersebut. Pencatatan dalam bentuk *commit* ini juga mempermudah proses *rollback* ke versi sebelumnya jika ada masalah yang terjadi pada kode sekarang.

2. **Kolaborasi (*Branching and Merging*)** <br>
`git` memiliki sistem percabangan yang dapat memisahkan kode untuk fitur baru, perbaikan bug, dan lainnya. Setiap *developer* yang terlibat dalam proyek dapat membuat cabang atau *branch* baru untuk pekerjaan mereka masing-masing **tanpa mengganggu kode utamanya**. Setelah kode mereka sudah siap, *branch* tersebut dapat digabungkan kembali ke kode utama dengan perintah *merge*.

3. ***Anytime and Anywhere Development*** <br>
Proyek yang menggunakan `git` dapat diinisiasi sebagai *repository* lokal dan disinkronkan dengan *remote repository* seperti GitHub atau GitLab. Hal ini memungkinkan *developer* dan rekannya untuk mengakses, mengubah, dan mengunggah perubahan pada kode dari berbagai lokasi dan *workspace* yang mereka miliki, selama terhubung dengan *remote repository* yang sama.

### Kenapa Django dijadikan *framework* yang pertama kali kami pelajari?

Django cocok digunakan sebagai *framework* pertama yang kami pelajari dalam pembelajaran pengembangan perangkat lunak karena:

1. Django dianggap **lebih mudah untuk digunakan** daripada *framework-framework* lainnya. Hal ini dikarenakan Django memiliki banyak fitur bawaan yang sudah cukup lengkap di dalamnya. Hal ini sejalan dengan *tagline*-nya, yaitu *"The Framework for Perfectionists with Deadlines"* yang menunjukkan bahwa Django dirancang untuk bisa bekerja lebih efisien tanpa perlu menambahkan banyak *library* eksternal.

2. Django **memiliki dokumentasi serta komunitas yang sangat baik dan informatif**, sehingga memudahkan para penggunanya dalam memahami konsep dasar dan cara penggunaan Django. Di dalam dokumentasi Django bahkan mencakup tutorial lengkap untuk membuat proyek sederhana dengan contoh dari kasus nyata, sehingga sangat membantu bagi pemula yang baru belajar.

3. Django menawarkan **keamanan bawaan yang kuat** untuk melindungi aplikasi dari berbagai serangan siber seperti SQL Injection dan Cross-Site Request Forgery (CSRF). Fitur keamanan bawaan ini berguna bagi pemula yang belum familiar dengan ancaman serangan siber dari orang-orang nakal di luar sana.

### Mengapa model pada Django disebut sebagai ORM atau *Object-Relational Mapping*?

Model Django disebut sebagai ORM karena Django memungkinkan kita untuk berinteraksi dengan *database* **menggunakan objek dari Python**. Kita tidak perlu menulis *query* SQL lagi jika ingin berinteraksi dengan *database* yang dikelola oleh Django. Setiap model di Django direpresentasikan sebagai tabel dalam *database*, dengan atribut dari model tersebut sebagai kolom-kolomnya.

Django dapat mengelola konversi antara sintaks dan objek Python ke dalam *query* SQL, maupun sebaliknya. Konversi otomatis ini memudahkan kita dalam melakukan operasi pada *database* seperti membuat, membaca, mengubah, serta menghapus data. Django juga dapat menerima berbagai jenis *database*, sehingga membuat kita tidak perlu khawatir tentang perbedaan antar DBMS yang digunakan.

