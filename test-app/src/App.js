import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';

class App extends Component {
  constructor(props) {
    super(props);

    // Inisialisasi state untuk menyimpan data produk
    this.state = {
      products: [],
    };
  }

  addProduct = () => {
    const newProduct = {
      productName: "",
      productPrice: 0,
      quantity: 1,
    };

    this.setState((prevState) => ({
      products: [...prevState.products, newProduct],
    }));
  };

  // Menghapus produk berdasarkan indeks
  deleteProduct = (index) => {
    const updatedProducts = [...this.state.products];
    updatedProducts.splice(index, 1);

    this.setState({
      products: updatedProducts,
    });
  };

  // Mengubah data produk (nama, harga, kuantitas)
  handleChange = (event, index) => {
    const { name, value } = event.target;
    const updatedProducts = [...this.state.products];
    updatedProducts[index][name] = name === "quantity" ? Math.max(1, value) : value;

    this.setState({
      products: updatedProducts,
    });
  };

  // Menghitung total per produk
  calculateTotal = (product) => {
    return product.productPrice * product.quantity;
  };

  // Menghitung grand total dari semua produk
  calculateGrandTotal = () => {
    return this.state.products.reduce((total, product) => total + this.calculateTotal(product), 0);
  };

  render() {
    return (
      <div className="App">
        <h1>Test Fullstack</h1>
        <button onClick={this.addProduct}>New</button>
        <table>
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Product Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {this.state.products.map((product, index) => (
              <tr key={index}>
                <td>
                  <input
                    type="text"
                    name="productName"
                    value={product.productName}
                    onChange={(e) => this.handleChange(e, index)}
                  />
                </td>
                <td>
                  <input
                    type="number"
                    name="productPrice"
                    value={product.productPrice}
                    onChange={(e) => this.handleChange(e, index)}
                  />
                </td>
                <td>
                  <input
                    type="number"
                    name="quantity"
                    value={product.quantity}
                    onChange={(e) => this.handleChange(e, index)}
                    min="1"
                  />
                </td>
                <td>{this.calculateTotal(product)}</td>
                <td>
                  {this.state.products.length > 1 && (
                    <button onClick={() => this.deleteProduct(index)}>Delete</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <div className="grand-total">Grand Total: {this.calculateGrandTotal()}</div>
      </div>
    );
  }
}

export default App;
