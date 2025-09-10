# El Football - Toko Perlengkapan Sepak Bola
## Tugas Individu PBP - Kelas C - 2406431510 - Muhammad Azka Awliya 

Aplikasi dapat diakses melalui tautan berikut: https://muhammad-azka41-elfootball.pbp.cs.ui.ac.id/ \
Nama Aplikasi: El Football

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat Proyek Django Baru
   
   ```
   django-admin startproject el_football
   ```

2. Membuat Aplikasi Baru dengan Nama main

    ```
    python manage.py startapp main
    ```

    Folder main otomatis membentuk beberapa file standar django seperti _ _ init _ _.py, admin.py, apps.py, models.py, tests.py, urls.py, dan views.py.

3. Melakukan Routing Aplikasi main ke Proyek

    - Menambah main ke dalam INSTALLED_APPS di settings.py
    - Membuat file urls.py di dalam folder app main
    - Menghubungkan urls.py milik main ke urls.py milik el_football (folder proyek).

4. Membuat Model Product pada models.py

    ```
    import uuid
    from django.db import models

    class product(models.Model):
        CATEGORY_CHOICES = [
            ('baju', 'Baju'),
            ('sepatu', 'Sepatu'),
            ('bola', 'Bola'),
            ('merch', 'Merch')
        ]

        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        thumbnail = models.URLField(blank=True, null=True)
        category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
        is_featured = models.BooleanField(default=False)
    ```

5. Membuat Fungsi di views.py
   
   ```
   from django.shortcuts import render

    def show_main(request):
        context = {
            'npm': '2406431510',
            'name' : ' Muhammad Azka Awliya',
            'class' : 'PBP C'
        }

        return render(request, "main.html", context)
   ```

6. Membuat Routing di main/urls.py

    ```
    from django.urls import path, include
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('', include('main.urls'))
    ]
    ```

7. Membuat Folder 'templates' dan file main.html di Dalamnya
   
   ```
    <h1>El Football</h1>
    <h3>High Quality yet Affordable Football Shop in Town!</h3>

    <h3>Hello, </h5>
    <h3>{{name}}</h3>

    <nav class="navbar">
        <ul>
            <li><a href="menu">Home</a></li>
            <li><a href="menu">About Us</a></li>
            <li><a href="menu">Discover</a></li>
            <li><a href="menu">Deals</a></li>
            <li><a href="menu">Contact Us</a></li>
        </ul>

        <p>OO Design</p>
    </nav>
   ```

8. Melakukan Deployment ke PWS

    Pada proyek ini, saya menggunakan branch main. Tidak lupa menambahkan file .gitignore untuk tidak memasukkan .env dan .env.prod sebagai target file yang akan di-push oleh git.

    ```
    git init
    git add . 
    git commit -m "Progress Tugas Individu"
    git push origin main
    git push pws main
    ```


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![alt text](alur.png)

- **urls.py** \
  Bekerja sebagai router yang menentukan view function atau class-based view dimana harus dipanggil setiap request.

- **views.py** \
  Menjadi penghubung utama antara URL, database (model.py) dan tampilan (main.html). View menerima request dari urls.py lalu dapat ambil data dari models.py datau kirim data ke main.html.

- **models.py** \
  Digunakan untuk menfefinisikan struktur database dengan konsep Object-Relational Mapping (ORM).

- **main.html** \
  Berupa file HTML namun mendukung Django Template Language (DTL).

## 3. Jelaskan peran settings.py dalam proyek Django!

**settings.py** adalah pusat konfigurasi proyek dan mendefinisikan cara kerja proyek (database, apps, keamanan, lokasi, template, dan lain sebagainya). Perannya meliputi:

**INSTALLED_APPS**: daftar aplikasi (app) yang aktif dalam proyek — Django akan memuatnya (migrations, admin, template lookup).

**DATABASES**: konfigurasi koneksi database.

**TEMPLATES**: pengaturan engine template, direktori DIRS, context processors.

**MIDDLEWARE**: middleware stack yang memproses request/response (security, session, csrf, dll).

**STATIC & MEDIA**: lokasi file statis HTML dan file upload media.

**DEBUG & ALLOWED_HOSTS**: mode pengembangan/production dan host yang diperbolehkan untuk melayani request.

**SECRET_KEY**: kunci kriptografi untuk session dan security — harus dirahasiakan (jangan commit ke repo publik).

**LOGGING / EMAIL / AUTHENTICATION BACKENDS**: berbagai konfigurasi lain untuk logging, email, otentikasi, dsb.

## 4. Bagaimana cara kerja migrasi database di Django?

a. **Definisikan model di models.py**. Model adalah kelas Python yang mewakili tabel DB.

b. **Buat migration**: 

Django mendeteksi perubahan pada model dan membuat file migration (mis. 0001_initial.py) yang berisi operasi (CreateModel, AddField, AlterField, dsb).
Migration adalah file Python yang mendeskripsikan transformasi skema.
  
    ```
    python manage.py makemigrations
    ```

c. **Terapkan migration**: 

Django menjalankan operasi migration terhadap database target, membuat/ubah tabel sesuai instruksi migration.
Riwayat migration disimpan di tabel django_migrations sehingga Django tahu migrasi mana yang sudah diterapkan.

    
    ```
    python manage.py migrate
    ```

d. **Mengubah model later**: buat perubahan pada models.py, jalankan makemigrations lagi (membuat migration baru seperti 0002_auto...), lalu migrate untuk menerapkannya.

e. **Operasi lanjutan**: ada operasi lanjutan seperti RunPython untuk melakukan data migration, squashmigrations untuk menggabungkan banyak migration menjadi satu, dan rollback memakai migrate app_name migration_name.

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

a. **“Batteries-included”**: banyak fitur built-in (ORM, admin site, autentikasi, forms, i18n, dsb) sehingga fokus belajar pada konsep web tanpa harus memilih banyak library eksternal.

b. **ORM**: memudahkan interaksi DB tanpa SQL mentah pada tahap awal.

c. **Admin otomatis**: CRUD untuk model bisa langsung tersedia lewat admin, berguna untuk prototyping dan belajar.

d. **Arsitektur jelas (MTV)**: memaksa pemisahan concerns — Model (data), Template (UI), View (logika) — konsep yang mudah dipahami dan berlaku di framework lain juga.

e. **Dokumentasi & komunitas besar**: banyak tutorial, plugin, dan sumber belajar.

f. **Keamanan**: banyak fitur keamanan standar tersedia (CSRF protection, XSS protection, password hashing).

g. **Skalabilitas & produksi-ready**: proyek kecil cepat dibuat, dan framework ini mampu digunakan di proyek besar juga.

h. **Konsistensi**: Django punya konvensi dan struktur proyek yang konsisten sehingga memudahkan pemula mengikuti best practices.

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Selama tutorial 1, asisten dosen turut membantu saya dalam menghadapi suatu permasalahan terutama pada migrasi data. Dari situ saya belajar bahwa setiap penambahan data, diperlukan migrasi basis data setiap perubahan berkala. Asisten dosen membantu saya dengan bahasa yang mudah dipahami, step-by-step, dan well structured. Namun saya memiliki saran untuk menambahkan section khusus untuk mengatasi beberapa error yang biasanya terjadi pada mahasiswa. Sejauh ini, kinerja asisten dosen sudah cukup baik. Terima kasih tim asisten dosen dan tim dosen.