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

| Tugas Sebelumnya --> | [Tugas 2](https://github.com/hyvos07/celestia/wiki/Tugas-2) | [Tugas 3](https://github.com/hyvos07/celestia/wiki/Tugas-3) |
|-|-|-|

<br>

## Tugas 4
### Implementasi Autentikasi, *Session*, dan *Cookies* pada tugas ini

sesuatuuu


### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

Pada suatu *project* Django, `HttpResponseRedirect()` dan `redirect()` sama-sama berfungsi untuk mengalihkan *user* ke suatu URL lain yang ada di `urls.py`. Namun, terdapat perbedaan di antara keduanya, yaitu:

1. Perintah `HttpResponseRedirect()`

    `HttpResponseRedirect()` adalah sebuah *method* yang digunakan untuk membuat *response* HTTP yang mengarahkan *user* ke URL yang dimasukkan di dalamnya. `HttpResponseRedirect()` hanya bisa menerima URL yang ingin dituju, bukan nama *views* atau *model*. Contoh penggunaannya ada di *views* `login_user()`.
    ``` python
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))  # reverse() disini mengembalikan URL dari views show_main
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```

2. Perintah `redirect()`

    `redirect()` adalah *shortcut method* yang lebih sederhana dan lebih fleksibel dari `HttpResponseRedirect()`. Fungsi ini sebenarnya juga menggunakan `HttpResponseRedirect()` di dalamnya. Namun, berbeda dengan `HttpResponseRedirect()`, `redirect()` dapat menerima URL, nama view, bahkan sebuah objek model dan akan mengarahkan *user* ke URL yang sesuai. Contoh penggunaannya pada *views* `register()` dapat dilihat di bawah berikut.
    ``` python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')   # redirect() dapat menerima nama views secara langsung
        context = {'form':form}
        return render(request, 'register.html', context)
    ```

    **Lalu, apa bedanya?** Jika dilihat pada penggunaan kedua *method* tersebut, method `redirect()` lebih mudah dan efisien untuk digunakan, sehingga membuatnya lebih sering digunakan pada saat kita hanya perlu berganti *views* atau *page* yang ada di platform kita. 
    
    Berbeda dengan `redirect()`, *method* `HttpResponseRedirect()` lebih sering digunakan saat kita memerlukan kontrol yang lebih spesifik pada *response* yang kita akan kirim ke sisi *user*. Seperti pada *views* `login_user()` di atas, kita perlu menyimpan *cookies* berupa `last_login` pada *browser* *user*, sehingga kita lebih cocok untuk menggunakan `HttpResponseRedirect()` untuk proses ini.

    **Jika `redirect()` itu sendiri menggunakan dan mengembalikan hal yang sama dengan `HttpResponseRedirect()` di dalamnya, bukankah `redirect()` saja juga bisa digunakan untuk menyimpan *cookies*?** Ya, `redirect()` bisa digunakan untuk melakukan modifikasi dan menambah *header*, *cookies*, status *response*, maupun komponen lainnya sama seperti `HttpResponseRedirect()`. Contohnya seperti ada di bawah berikut.
    ``` python
    # Kode lain ...
    response = redirect("main:show_main")
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
    ```
    Walaupun begitu, `redirect()` dinilai tidak terlalu cocok untuk mendapatkan kontrol penuh dalam memodifikasi *response* yang kita miliki. `HttpResponseRedirect()` dapat memberikan kontrol yang lebih baik atas *response* HTTP, termasuk pengaturan *cookie*. Oleh karena itu, `HttpResponseRedirect()` lebih sering digunakan saat kita perlu memanipulasi *cookie* atau melakukan modifikasi komponen *response* lainnya.


### Cara Kerja Penghubungan Model `Product` dengan `User`

Pada Tugas 4 ini, terdapat penghubungan *model* `Product` yang dimiliki oleh aplikasi `main` dengan data `User` sebagai suatu *field* baru di `Product`. Dengan adanya penghubungan ini, suatu `Product` sekarang dimiliki oleh seorang `User` di *database* yang kita miliki. Cara kerja penghubungan kedua *model* ini adalah dengan meng-*assign* sebuah *entity* `User` sebagai ***Foreign Key*** pada model `Product`. Penggabungan tersebut dilakukan dengan menambah *field* pada *model* seperti demikian.
```python
from django.contrib.auth.models import User

class Product(models.Model): 
    # Other attribute...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other attribute...
```

Pada potongan kode di atas, model `Product` akan ditambahkan informasi `User` yang menjadi pemilik dari produk tersebut di database. Penambahan ini dilakukan dengan menambah *field* `user`, yang diisi dengan sebuah *Foreign Key* berupa model dari `User` yang menambahkan produk tersebut.

**Apa itu Foreign Key?** *Foreign Key* adalah sebuah tipe *field* yang berguna untuk membuat sebuah hubungan (dalam kasus ini) ***many-to-one*** antara *model* `Product` dan `User`. Dengan menggunakan konfigurasi *Foreign Key* seperti yang ada di dalam *project* ini, sebuah `Product` dapat memiliki hubungan dengan hanya satu `User`, sedangkan seorang `User` dapat memiliki banyak `Product` yang ia miliki di dalam *database*. 

Pada inisiasi *Foreign Key* di atas, terdapat pula parameter `on_delete` yang diisi dengan `models.CASCADE` pada `models.ForeignKey()`. Opsi `models.CASCADE` menandakan jika data seorang *user* di *database* dihapus, maka seluruh produk yang *user* tersebut miliki di *database* juga akan dihapus bersamanya. Hal ini dilakukan untuk mencegah adanya entri produk "terlantar" yang tidak memiliki pemilik.


### *Authentication* vs *Authorization*

- ***Authentication***

    Authentication atau autentikasi merupakan sebuah proses untuk **memverifikasi identitas dari seorang *user***. Proses autentikasi memastikan bahwa *user* yang sedang mengakses platform kita adalah memang seseorang yang mereka klaim. Proses autentikasi biasanya dilakukan dengan meminta *user* untuk memasukkan kredensial akun atau identitasnya, seperti sebuah *username* dan *password*. Proses ini terjadi setelah seorang *user* melakukan percobaan *login* pada sistem kita.

    Di dalam Django, pada saat seorang *user* sudah melakukan aktivitas *login*, proses autentikasi akan dilakukan. Django memeriksa kredensial *user*, contohnya *form login*. Jika kredensial yang dimasukkan *user* valid, Django akan membuat *session* untuk *user* yang terautentikasi tersebut dan mengaitkan identitas *user* dengan *session* tersebut.

    Pada *project* ini, proses autentikasi dilakukan secara otomatis dengan sistem autentikasi bawaan dari Django. Proses login ini terjadi pada *views* `login_user()` di `views.py`.
    ```python
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```
    Sistem bawaan yang dimiliki oleh Django untuk mengautentikasi *user* yang akan *login* berasal dari *method* `AuthenticationForm()`. *Method* tersebut dapat diproses otomatis oleh Django menjadi *form login* dengan menambahkan `{{ form.as_table }}` pada *template* HTML yang bersangkutan. Saat *user* berhasil *login*, Django akan membuat entri *session* di *database* (menggunakan *middleware session*), dan mengaitkannya dengan ID dari *user* yang terautentikasi.

2. *Authorization*

    Berbeda dengan autentikasi, *authorization* atau otorisasi adalah sebuah proses **memverifikasi hak akses *user* terhadap sumber daya atau tindakan tertentu**. Django akan menentukan apa saja aktivitas yang diizinkan untuk dilakukan oleh *user* tersebut setelah mereka berhasil terautentikasi. Seorang *user* yang sudah login dapat memiliki akses ke dashboard *admin*, sementara *user* lain mungkin hanya bisa mengakses halaman biasa saja. *User* yang memiliki hak sebagai *admin* dapat mengakses panel *admin*, sementara *user* biasa hanya dapat mengakses profilnya sendiri.

    Pada *project* ini, terdapat *authorization* pada saat seorang *user* ingin mengakses halaman utama dari situs web ini.  Otorisasi tersebut terletak pada decorator `@login_required(login_url='/login')` yang mengatur *user* yang belum *login* untuk login terlebih dahulu di /login, yaitu path di `urls.py` yang mengarah pada halaman login. Contoh dari authorization tersebut adalah sebagai berikut.
    ```python
    @login_required(login_url='/login')
    def show_main(request):
        mood_entries = MoodEntry.objects.filter(user=request.user)
        ...
    ```
    Selain decorator `@login_required()`, terdapat juga decorator-decorator otorisasi lainnya seperti `@permission_required`.
    
    <br>
    Singkatnya,
    
    ***Authentication*** --> menjawab pertanyaan “Siapa Anda?”<br>
    ***Authorization*** --> menjawab pertanyaan “Apa yang boleh Anda lakukan?”


### Bagaimana Django mengingat *user* yang telah login? 

Django mengingat *user* yang telah login melalui mekanisme ***session***. Session membantu Django untuk mempertahankan status dan data dari *user* selama mereka mengirim berbagai *request* HTTP. Saat *user* berhasil *login*, Django akan membuat sebuah *session* dan memberikan sebuah *session* cookie kepada *browser* pengguna. *Cookie* ini akan dikirimkan kembali ke *server* pada setiap permintaan berikutnya, sehingga Django dapat mengidentifikasi pengguna tersebut tanpa harus *login* untuk setiap aksi di aplikasi kita.


### Jelaskan kegunaan lain dari *cookies* dan apakah semua *cookies* aman digunakan?

Terdapat berbagai macam kegunaan *cookies* untuk berbagai fitur yang disediakan oleh sistem web kita, seperti:
- Penyimpanan preferensi *user*
- Membuat *targeted advertising* (Iklan yang Dipersonalisasi)
- Autentikasi berkelanjutan (*Remember Me*) sehingga *user* tidak perlu login setiap saat.
- dan lainnya.

Walaupun begitu, tidak semua *cookies* yang ditawarkan oleh berbagai situs web di internet selalu aman. Penggunaan *cookies* dapat memunculkan beberapa risiko keamanan, terutama jika tidak dikelola dengan benar. Contoh-contoh dari *cookies* yang tidak aman adalah:

1. **Cross-Site Scripting (XSS) dan Session Hijacking** --> Mengambil *cookies* dari *user* yang berisi hal-hal penting dengan memakai sebuah *script*. Jika *cookie* yang berisi *session* ID dari seorang *user* dicuri, penyerang dapat menggunakan *session* ID tersebut untuk mengambil alih sesi *user* dan bertindak seolah-olah mereka adalah pengguna yang sah.

2. **Cross-Site Request Forgery (CSRF)** --> Penyerang CSRF dapat memaksa *user* yang sudah *login* dan terautentikasi di suatu situs untuk melakukan tindakan yang tidak diinginkan, seperti mentransfer uang atau mengubah pengaturan akun. Serangan ini terjadi ketika penyerang memanfaatkan *session cookie* yang secara otomatis dikirimkan oleh *browser* setiap kali permintaan dibuat ke *server*.

3. **Penyalahgunaan Persistent Cookies dan Privasi Data** --> *Cookies* yang bersifat *persistent* dapat melacak aktivitas pengguna di berbagai *session* atau situs. *Cookies* ini berpotensi mengancam privasi *user*, terutama dalam kasus pelacakan lintas situs untuk tujuan iklan yang agresif.

