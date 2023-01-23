import mysql.connector

# konfigurasi koneksi ke database
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'uasbp',
    'raise_on_warnings': True
}

# membuat koneksi ke database
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    print("Koneksi Berahasil")
except mysql.connector.Error as err:
    print("Koneksi Gagal: {}".format(err))

# perintah SQL untuk membuat tabel
create_table = """
CREATE TABLE staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    umur INT NOT NULL
)
"""
cursor.execute(create_table)

# menutup koneksi ke database
cursor.close()
cnx.close()
