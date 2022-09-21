# Tugas 2 Assignment
# Dhafiano Fadeyka Ghani Wiweko
# 2106751631

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html?

![katalog_bagan_dhafiano](https://user-images.githubusercontent.com/112342752/190219303-a42293aa-0b34-4911-a8cc-2a71f6896202.jpg)

Pada awalnya akan user akan mengakses Django dengan menggunakan link yang telah diberikan dari template, kemudian terdapat beberapa file yang muncul diantaranya urls.py, views.py, models.py dan beberapa berkas html. Pada dasarnya file-file tersebut berkaitan satu sama lainnya yang dimana models.py akan mengambil semua data dari hasil penyebaran perintah yang telah dilakukan oleh URL(urls.py) kepada tampilan (views.py)-nya.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Digunakannya virtual environment agar memudahkan bagi user untuk membagi kode-kode yang dikhususkan pada bagian-bagian tertentu, sehingga membuat user tidak bingung untuk melihat/memperbaiki kodenya. Kita sebagai user sebetulnya tidak masalah ingin jika membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi balik lagi bahwa untuk membuat aplikasi web itu membutuhkan susunan kode yang tidak sedikit, sehingga sebaiknya terdapat pemisahan kepada kode-kode yang telah dibuat.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas?

Awalnya saya mengcopy link dan clone untuk mendapatkan template di PBP Fasilkom Github. Selanjutnya ketika saya mendapatkan file2nya saya mengisi kode ke beberapa file yang dianjurkan seperti views.py, urls.py, dan beberapa html. Setelah itu, saya git commit push ke repositori baru yang telah saya buat, kemudian membuat repo lagi untuk mendeploy kepada heroku agar web juga dapat berjalan pada app heroku, kemudian ketika semua itu selesai saya membuat file README.md dan mengisi pertanyaan yang dikasih pada poin ke-5.



https://pbp-dhafiano.herokuapp.com/katalog/
