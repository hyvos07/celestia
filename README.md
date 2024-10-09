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

| Tugas Sebelumnya: | [Tugas 2](https://github.com/hyvos07/celestia/wiki/Tugas-2) | [Tugas 3](https://github.com/hyvos07/celestia/wiki/Tugas-3) | [Tugas 4](https://github.com/hyvos07/celestia/wiki/Tugas-4) | [Tugas 5](https://github.com/hyvos07/celestia/wiki/Tugas-5) |
|-|-|-|-|-|

<br>

## Tugas 6
### Implementasi Penggunaan JavaScript dan AJAX

1. AJAX `GET`
    - Mengubah kode *cards* sehingga dapat mendukung jenis data yang berbeda dari proses fetch AJAX, dengan cara:
        - Mengambil data dilakukan dengan AJAX lewat method `fetch`
            ```js
            async function getAllProduct(){
                return fetch("{% url 'main:show_json' %}").then((res) => res.json())
            }

            async function refreshAllProduct() {
                document.getElementById("product_cards").innerHTML = "";
                document.getElementById("product_cards").className = "";
                
                const allProduct = await getAllProduct();
                ...
            ```
        - Kode *cards* yang disesuaikan dengan cara ini
            ```html
            <div class="max-w-[400px] sm:max-w-[350px] flex-grow-0 flex-shrink-0 w-full use-poppins">
                <div class="flex flex-col h-full rounded-[16px] overflow-hidden shadow-lg bg-white p-6">
                    <div class="overflow-hidden border border-gray-200 rounded-[16px]">
                        <img class="w-full h-[350px] object-cover object-center transition-transform duration-300 ease-in-out hover:scale-110" src=${image} alt="Product Image">
                    </div>

                    <div class="flex-grow flex flex-col justify-between">
                        <div class="flex-grow-0">
                            <div class="font-semibold text-lg mt-4 mb-2 text-black line-clamp-2">
                                ${name}
                            </div>

                            <div class="text-lg font-semibold text-green-700 my-4">IDR ${price.toLocaleString()}</div>

                            <p class="text-gray-600 text-base mb-4 line-clamp-2">
                                ${description}
                            </p>
                        </div>

                        <div>
                            <div class="text-gray-500">
                                Stock: 
                                {% if product.stock != 0 %}
                                    <span class="font-semibold text-gray-800">${stock}</span>
                                {% else %}
                                    <span class="font-semibold text-[#ff0000]">Empty</span>
                                {% endif %}
                            </div>

                            <div class="flex flex-row gap-3 mt-6">
                                <button onclick="location.href='/edit-product/${item.pk}'" class="bg-[#1d2736] text-white py-3 px-4 rounded-md hover:bg-[#2c3a4f] transition-colors duration-300 w-full">
                                    Edit
                                </button>
                                <button onclick="location.href='/delete-product/${item.pk}'" class="bg-red-700 text-white py-3 px-4 rounded-md hover:bg-[#cc0000] transition-colors duration-300 w-full">
                                    Delete
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            ```
    - Modifikasi pengambilan data dari `show_json` dan `show_xml` menjadi khusus milik user tersebut saja, yaitu mengubah *line* ini:
        ```python
        data = Product.objects.all()
        ```
        menjadi seperti ini.
        ```python
        data = Product.objects.filter(user=request.user)
        ```
- AJAX `POST`
    - Membuat sebuah *button* yang membuka *modal* dengan *form* untuk menambahkan produk baru
        ```html
        <div class="mt-12 mb-4">
            <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-[#5038bc] hover:bg-[#45349f] text-white font-semibold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-10 use-poppins" onclick="showModal();">
                <p id="decideTextButton"></p>
            </button>
        </div>
        ```
        *Catatan: Tag `deciceTextButton` akan dikontrol isinya saat melakukan *fetching* data di `refreshAllProduct()`.*
        ```js
        let haveProduct = false;

        ...

        document.getElementById("decideTextButton").innerText = haveProduct ? "Have More?" : "Add Your First Product!";
        ```
        Button ini akan menampilkan sebuah *modal* yang memiliki kode berikut.
        ```html
        <!-- Modal -->
        <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-gray-800 bg-opacity-50 transition-opacity duration-300 ease-out">
            <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 my-16 sm:mx-0 max-h-[80vh] flex flex-col">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 border-b rounded-t sticky top-0 bg-white z-10">
                    <h3 class="text-xl font-semibold text-gray-900 use-poppins">
                        Add New Product
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only use-poppins">Close</span>
                    </button>
                </div>
        
                <!-- Scrollable form content -->
                <div class="overflow-y-auto px-6 py-4 space-y-6 form-style flex-1">
                    <form id="addProductForm">
                        <div class="mb-4">
                            <label for="name" class="block text-sm font-medium text-gray-700 use-poppins">Name</label>
                            <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="price" class="block text-sm font-medium text-gray-700 use-poppins">Price</label>
                            <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="description" class="block text-sm font-medium text-gray-700 use-poppins">Description</label>
                            <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required></textarea>
                        </div>
                        <div class="mb-4">
                            <label for="stock" class="block text-sm font-medium text-gray-700 use-poppins">Stock</label>
                            <input type="number" id="stock" name="stock" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="chara" class="block text-sm font-medium text-gray-700 use-poppins">Chara</label>
                            <input type="text" id="chara" name="chara" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="game" class="block text-sm font-medium text-gray-700 use-poppins">Game</label>
                            <input type="text" id="game" name="game" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="category" class="block text-sm font-medium text-gray-700 use-poppins">Category</label>
                            <input type="text" id="category" name="category" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required>
                        </div>
                        <div class="mb-4">
                            <label for="image" class="block text-sm font-medium text-gray-700 use-poppins">Image URL</label>
                            <textarea id="image" name="image" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-[#171e2a] text-black" required></textarea>
                        </div>
                    </form>
                </div>
        
                <!-- Modal footer -->
                <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end sticky bottom-0 bg-white z-10">
                    <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-semibold py-2 px-4 rounded-lg use-poppins" id="cancelButton">Cancel</button>
                    <button type="submit" id="submitMoodEntry" form="addProductForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-semibold py-2 px-4 rounded-lg use-poppins">Save</button>
                </div>
            </div>
        </div>
        ```
        yang akan di-*trigger* kemunculannya lewat 2 fungsi di bawah ini.
        ```js
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        function showModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modal.classList.remove('hidden'); 
            setTimeout(() => {
                modalContent.classList.remove('opacity-0', 'scale-95');
                modalContent.classList.add('opacity-100', 'scale-100');
            }, 50); 
        }

        function hideModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modalContent.classList.remove('opacity-100', 'scale-100');
            modalContent.classList.add('opacity-0', 'scale-95');

            setTimeout(() => {
                modal.classList.add('hidden');
            }, 150); 
        }
        ```

    - Membuat fungsi *views* baru bernama `create_product_ajax` untuk menerima *request* POST yang berasal dari AJAX.
        ```python
        @csrf_exempt
        @require_POST
        def create_product_ajax(request):
            name = strip_tags(request.POST.get("name"))
            price = strip_tags(request.POST.get("price"))
            description = strip_tags(request.POST.get("description"))
            stock = strip_tags(request.POST.get("stock"))
            chara = strip_tags(request.POST.get("chara"))
            game = strip_tags(request.POST.get("game"))
            category = strip_tags(request.POST.get("category"))
            image = strip_tags(request.POST.get("image"))
            
            user = request.user

            new_product = Product(
                name=name,
                price=price,
                description=description,
                stock=stock,
                chara=chara,
                game=game,
                category=category,
                image=image,
                user=user
            )
            
            new_product.save()

            return HttpResponse(b"Successfully Created", status=201)
        ```
    - Membuat *path* baru yang akan menjadi tempat mengirim *request* dari *views* yang baru di atas, dengan nama `/create-product-ajax/`.
        ```python
        ...
        path('create-product-ajax', create_product_ajax, name='create_product_ajax'),
        ...
        ```
        Setelah menambahkan *path* tersebut, tombol *Save* pada modal sekarang akan menjalankan fungsi di bawah berikut yang memakai `create_product_ajax` jika ditekan.
        ```js
        function addProduct() {
            fetch("{% url 'main:create_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#addProductForm')),
            }).then(response => refreshAllProduct()) // Melakukan refresh page lagi secara asinkronus

            document.getElementById("addProductForm").reset(); 
            
            hideModal();

            return false;
        }
        ```
        Di dalam *function* tersebut, setelah melakukan *fetch* data dari semua produk, akan dijalankan *function* `refreshAllProduct()` setelah semua data selesai diambil.

Dalam mengimplementasikan `GET` dan `POST` dari AJAX, projek ini juga memastikan setiap data yang dikirim oleh pengguna aman dari serangan XSS. Contohnya dengan mengimplementasikan `strip_tags` yang menghilangkan tags HTML pada *input* pengguna dari sisi *backend* serta `DOMPurify` yang juga membersihkan data seperti tag yang tidak diperlukan pada sisi *frontend*.
- Implementasi `strip_tags`
    Di `views.py`
    ```python
    @csrf_exempt
    @require_POST
    def create_product_ajax(request):
        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        description = strip_tags(request.POST.get("description"))
        stock = strip_tags(request.POST.get("stock"))
        chara = strip_tags(request.POST.get("chara"))
        game = strip_tags(request.POST.get("game"))
        category = strip_tags(request.POST.get("category"))
        image = strip_tags(request.POST.get("image"))
        ...
    ```
    Di `forms.py`
    ```python
    ...
    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data['price']
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        return strip_tags(stock)
    
    def clean_chara(self):
        chara = self.cleaned_data['chara']
        return strip_tags(chara)
    
    def clean_game(self):
        game = self.cleaned_data['game']
        return strip_tags(game)
    
    def clean_category(self):
        category = self.cleaned_data['category']
        return strip_tags(category)
    
    def clean_image(self):
        image = self.cleaned_data['image']
        return strip_tags(image)
    ```
- Implementasi `DOMPurify`
    ```js
    ...
    classNameString = "flex flex-wrap gap-6 w-full py-8 justify-center"
    allProduct.forEach((item) => {
        const name = DOMPurify.sanitize(item.fields.name);
        const price = DOMPurify.sanitize(item.fields.price);
        const description = DOMPurify.sanitize(item.fields.description);
        const stock = DOMPurify.sanitize(item.fields.stock);
        const image = DOMPurify.sanitize(item.fields.image);
    ...
    ```


### Manfaat dari Penggunaan JavaScript di Aplikasi Web

JavaScript adalah bahasa pemrograman yang sering digunakan dalam pengembangan aplikasi web modern, karena JavaScript memiliki berbagai kegunaan  yang tidak selalu bisa dicapai hanya dengan mengandalkan HTML dan CSS. Berikut beberapa contoh dari keuntungan yang bisa didapat dengan menggunakan JavaScript di aplikasi web yang kita miliki.

1. **Web yang Interaktif**
    Kehadiran JavaScript pada aplikasi web kita dapat mendukung keinteraktifan yang diperlukan di dalam suatu halaman web. Daripada membuat berbagai kode HTML yang berbeda untuk kondisi yang berbeda-beda, kita dapat memanfaatkan DOM *manipulation* dari JavaScript untuk mengubah sebagian kode dari HTML kita, yang membuatnya semakin interaktif berdasarkan dari apa yang dilakukan oleh *user*, seperti klik, *hover*, dan *input*. JavaScript juga bisa membuat animasi di tag yang kita pilih.

2. ***User Experience* (UX) yang Lebih Baik**
    Dengan JavaScript, kita sebagai *developer* dapat meningkatkan kenyamanan *user* aplikasi web kita dengan membuat aplikasi web kita menjadi lebih dinamis dan responsif. Misalnya, validasi dari *form* yang digunakan oleh *user* dapat dilakukan secara *real-time* tanpa perlu memuat ulang halaman web.

3. **Asynchronous Programming**
    Dengan menggunakan AJAX (*Asynchronous JavaScript and XML*), JavaScript memungkinkan kita untuk melakukan *request* HTTP secara asinkronus, yang membuat proses pengambilan data tidak akan mempengaruhi proses lainnya dan meningkatkan pengalaman pengguna saat memakai aplikasi web kita.

4. **Kompatibilitas Lintas Platform**
    JavaScript dapat dijalankan di hampir semua *browser* modern, bahkan di *browser mobile* sekalipun. Hal ini membuat JavaScript sangat kompatibel dan mudah diintegrasikan ke dalam berbagai jenis aplikasi web.

Dari manfaat-manfaat yang dijelaskan di atas, seharusnya sudah jelas banyak manfaat yang dimiliki oleh JavaScript, sehingga membuatnya menjadi salah satu bahasa pemrograman yang paling populer dan penting dalam pengembangan aplikasi web modern.


### Fungsi dari Penggunaan `await` ketika Menggunakan `fetch()`

Ketika kita menggunakan `await` dengan `fetch()`, kita memberitahu JavaScript untuk menunggu hingga operasi `fetch` diselesaikan sebelum lanjut ke kode berikutnya. Notasi `await` ini memungkinkan kita untuk menulis kode yang terlihat dan berperilaku seperti kode yang sinkronus, walaupun kode tersebut tetao berjalan secara asinkronus.

Jika kita tidak menggunakan `await` pada `fetch()`, Seluruh rangkaian kode tersebut akan tetap berjalan ke baris selanjutnya tanpa melakukan pengecekan pada data yang diambil pada fungsi `fetch()` sebelumnya. Hal ini bisa menyebabkan masalah pada kode-kode di baris berikutnya, jika mereka menggunakan data yang bisa saja pada saat itu belum tersedia.

Contoh penggunaan `fetch()` tanpa `await`
```js
const response = fetch('https://jokesbapak2.reinaldyrafli.com/api/today/');
console.log(response); // Baris ini belum tentu akan mengembalikan data yang diambil oleh fetch()
```

Solusi tanpa menggunakan `await` untuk tetap bisa mendapatkan hasil data setelah proses `fetch()` tersebut selesai, kita harus menggunakan metode `.then()` yang menandakan operasi yang akan dilakukan secara asinkronus (bersamaan dengan `fetch()`) setelah *fetch* selesai.
```js
fetch('https://jokesbapak2.reinaldyrafli.com/api/today/')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Fetch error:', error));
```


### Kegunaan *Decorator* `csrf_exempt`

*Decorator* `csrf_exempt` ditempatkan pada saat menjalankan `create_product_ajax`, agar memberitahu Django untuk tidak perlu mengecek keberadaan `csrf_token` pada POST *request* yang dikirimkan lewat fungsi tersebut. Tanpa adanya *decorator* ini, secara *default* AJAX tidak memiliki `csrf_token` saat melakukan *request* POST. Maka dari itu, kita perlu menambahkan *decorator* `@csrf_exempt` di atas *views* yang membutuhkannya, sehingga dapat menonaktifkan pengecekan CSRF pada *view* tersebut.

*Decorator* `csrf_exempt` juga bisa diimplementasikan pada *views* yang memang sudah terpercaya dan tidak memerlukan `csrf_token` untuk mengirim *request* POST ke *server*. Jika *views* tersebut belum tentu aman, sebaiknya *decorator* ini tidak ditambahkan agar menjamin keamanan dari aplikasi web kita.


### Pembersihan Data Input pada Front-End dan Back-End

Pembersihan data yang dilakukan di kedua sisi *front-end* dan *back-end* memiliki alasannya sendiri. Jika pembersihan hanya dilakukan di *front-end*, maka belum tentu data yang ada di dalam *database* bisa aman saat *user* melakukan *insertion data* ke dalam *server*. *User* yang nakal masih bisa memanipulasi *input* yang ia kirim ke *server*, yang dapat membuat data yang tidak aman tersebut tersimpan ke dalam *server* dan menjadi berbahaya bagi aplikasi web kita maupun untuk *user* lain yang mengakses aplikasi web kita. Untuk menjaga keintegritasan data di kedua sisi, diperlukan pembersihan di *back-end* juga supaya keamanan dari data yang dimiliki oleh aplikasi web kita lebih aman.