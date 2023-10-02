import unittest
from app import app, db, Transaksi

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_transaksi(self):
        data = {
            "tanggal_transaksi": "2023-10-01",
            "customer_address_id": 1
        }
        response = self.app.post('/create_transaksi', json=data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
