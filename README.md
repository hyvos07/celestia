<a id="readme-top"></a>

# <p align="center"><img src="assets\logo\Horizontal.png"   style="width: 100%; max-width: 350px;" alt="Celestia"></p>

Celestia is a Hoyoverse Official Merchandise E-Commerce that offers a wide range of products related by some games that Hoyoverse made. This Project was made for one of the task in [Pemrograman Berbasis Platform (PBP) Gasal 2024/2025](https://pbp-fasilkom-ui.github.io/ganjil-2025/).

> **Note:** <br> This is not an actual online shop for Hoyoverse Merchandise.

<br>
<br>

# ⚙️ Deployment and Usage
This project is deployed on PWS (Pacil Web Service) and can be accessed [here](http://pwsbroken.com).

If you want to try and run the project from your local device, open http://127.0.0.1:8000 or http://localhost:8000 with your browser to see the result.

<br>
<br>

# 📝 Assignment
**Nama**    : Daniel Liman <br>
**NPM**     : 2306220753 <br>
**Kelas**   : PBP F
<p style="font-size: 1px;"> &nbsp; </p> <!-- maaf MD gaada padding nya sih ;-; -->

## Tugas 2
### Step by Step Pembuatan Project Django
1. Membuat direktori baru bernama `celestia` dan inisiasi local repository di folder tersebut.

2. Membuat GitHub repository yang dihubungkan dengan local repository `celestia`

3. Membuat *virtual environment* baru dan jalankan env tersebut untuk project ini dengan command:
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
    dan meng-*install requirements* yang ada di `requirements.txt` tersebut dengan pip
    ```bash
    pip install -r requirements.txt
    ```

5. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject celestia .
    ```
    Lalu melakukan beberapa settings untuk project yang baru dibuat tersebut.

6. Membuat aplikasi dengan nama `main` pada proyek ini dengan menjalankan command:
    ```bash
    python manage.py startapp main
    ```
    setelah dibuat, aplikasi `main` juga perlu ditambahkan ke `celestia/settings.py` pada variable `INSTALLED_APPS`.

7. Membuat model `Product` dengan field-field sebagai berikut:
    ```python
    name: CharField,
    price: IntegerField,
    description: TextField,
    chara: CharField,
    game: CharField,
    category: CharField,
    image: TextField,
    price_with_comma: int,      # Internal Property
    image_URL : String,         # Internal Property
    ```
    **N.B.** <br> Ada beberapa field yang masih dalam bentuk sederhana, sehingga tidak ada di dalam bentuk aslinya (seperti image yang seharusnya ImageField) agar dapat lebih diperdalam di minggu-minggu berikutnya.

8. Membuat function `show_main()` pada `views.py` untuk dikembalikan ke dalam template HTML bernama `main.html` yang dibuat di direktori `templates`. <br> HTML tersebut akan menampilkan nama aplikasi, data dari `show_main()` dan identitas diri sendiri.

9. Membuat sebuah routing pada `urls.py` dalam direktori aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`. Di `urls.py`, ditambahkan `path('', show_main, name='show_main')` ke dalam `urlpatterns` milik aplikasi `main`.

10. Terakhir, push kode ke GitHub dan lakukan *deployment* ke PWS agar dapat diakses oleh orang lain. Hasil deployment dari project ini dapat diakses di bagian [atas](#readme-top).

### Bagan Gambaran Request Client ke Django

<!-- image here -->

### Fungsi `git` pada Pengembangan Perangkat Lunak

<!-- Jawaban here -->

### Kenapa Django dijadikan *framework* yang pertama kali kami pelajari?

<!-- Jawaban here -->

### Alasan Django disebut sebagai DBMS yang ORM

<!-- Jawaban here -->
