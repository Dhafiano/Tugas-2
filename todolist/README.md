# Dhafiano Fadeyka Ghani Wiweko
# 2106751631
# PBP-E
# Tugas 4

# Link web 1 : https://dhafiano-tugas3.herokuapp.com/todolist/login/

dummy data:
![image](https://user-images.githubusercontent.com/112342752/192917646-287401b1-c6cc-4c55-8a2b-1b2c6be0e558.png)
![image](https://user-images.githubusercontent.com/112342752/192917690-3c995308-3e80-4247-bb97-fe792dd1892c.png)

Pertanyaan:

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  
Jawaban:
  
1. Kegunaan dari {% csrf_token %} adalah memberikan keamanan bagi situs web itu sendiri terutama pada bagian-bagian yang terdapat (POST) sehingga bisa mencegah hacker atau pihak usil dalam mengacak-acak isi dari web atau memasangkan virus yang tidak jelas pada web. Jika {% csrf_token %} tidak ada, maka tidak ada keamanan pada URL yang ingin ditargetkan seperti mau di bagian dalam(internal) atau luarnya(eksternal), karena tidak ada keamanan, pihak usil tersebut dapat mudah mengakses dan mengacak-acak URL pada bagian mana saja.
  
2. Tentu saja bisa, kalau pada program yang saya buat, saya menggunakan div untuk membuat kolom-kolom dan dibawahnya saya  menggunakan button untuk membuat tombol menambahkan tasknya sehingga tidak memerlukan lagi {{ form.as_table }}.
  
3. Jadi pertama-tama kita menentukan method apa yang digunakan dan saya mendapatkan bahwa method yang dipakai adalah method POST yang nantinya harus di request terlebih dahulu atau dipanggil, kegunaan POST adalah menampilkan data form yang telah dibuat. Selanjutnya untuk penyimpanannya data pada database kita menggunakan if dan menyusun beberapa kode yang nantinya jika dibuat input, maka beberapa bagian kode tersebut harus ditambahkan dengan method (save()). Dan yang terakhir cara kita menampilkan data yang disimpan dengan menggunakan return render agar terjadi perubahan dalam web sehingga data yang tadi sudah dibuat baru dan disave muncul.

4. - Pertama-tama membuat django-app, yaitu start-app todolist.
   - Membuat models todolist dalam models.py.
   - Kemudian mengisi urlpattern sesuai dengan todolistnya dan menambahkan register dan login pada kodenya.
   - Yang keempat membuat kode agar dapat menampilkan web dalam bentuk form pada views.py.
   - Selanjutnya membuat todolist.html untuk menampilkan hasil task yang sudah ditambahkan.
   - Lalu membuat login.html dan register.html untuk membuat tampilan awal yang nantinya berperan sebagai requirement agar bisa mengakses hasil task.
   - Dan yang terakhir dalam pemrograman kodenya adalah membuat html kolom task agar user dapat mengisi dan menambahkan task baru, kalau disaya namanya create_todolist.html.
   - Setelah semuanya jadi tinggal python manage.py makemigrations, python manage.py migrate, dan python manage.py runserver.
   - Habis itu deploy ke github dan heroku.
