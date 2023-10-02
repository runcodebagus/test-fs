from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/create_transaksi', methods=['GET', 'POST'])
def create_transaksi():
    data = request.get_json()
    tanggal_transaksi = data['tanggal_transaksi']
    customer_address_id = data['customer_address_id']

    transaksi = Transaksi(tanggal_transaksi=tanggal_transaksi, customer_address_id=customer_address_id)

    db.session.add(transaksi)
    db.session.commit()

    return jsonify({"message": "Transaksi berhasil dibuat!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)