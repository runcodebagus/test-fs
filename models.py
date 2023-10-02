# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definisi model untuk tabel "Transaksi"
class Transaksi(db.Model):
    transaksi_id = db.Column(db.Integer, primary_key=True)
    tanggal_transaksi = db.Column(db.Date)
    customer_address_id = db.Column(db.Integer, db.ForeignKey('customer_address.address_id'))

    def __init__(self, tanggal_transaksi, customer_address_id):
        self.tanggal_transaksi = tanggal_transaksi
        self.customer_address_id = customer_address_id

# Definisi model untuk tabel "Customer"
class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    nama_pelanggan = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, nama_pelanggan, email):
        self.nama_pelanggan = nama_pelanggan
        self.email = email

# Definisi model untuk tabel "Customer_Address"
class Customer_Address(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    alamat = db.Column(db.String(255))
    kota = db.Column(db.String(255))
    kode_pos = db.Column(db.String(10))

    def __init__(self, customer_id, alamat, kota, kode_pos):
        self.customer_id = customer_id
        self.alamat = alamat
        self.kota = kota
        self.kode_pos = kode_pos
