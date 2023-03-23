from products import productos
from flask import Flask, jsonify, json, request

app = Flask(__name__)

# Creando la función de qué hacer cuando el usuario haga la petición


@app.route('/ping')
def ping():
    # Así se evita que haya conflicto cuando hayan carácteres no alfa númericos
    message = {"Message": "Para ganar dejé todo de lado"}
    return json.dumps(message, ensure_ascii=False).encode('utf8')
# Creando la función de qué hacer cuando el usuario haga la peticion


@app.route('/products', methods=["GET"])
def obtener_products():
    return jsonify({"Products": productos, "message": "Product's List"})


@app.route('/products/<string:product_name>')
def get_Product(product_name):
    product_found = [
        product for product in productos if product['name'] == product_name]
    if (len(product_found) > 0):
        return jsonify({"Product": product_found[0]})
    return jsonify({"message": "Product not found"})

# Puede tener el mismo nombre que la anterior, porque ambas tienen distintos metodos HTTP
@app.route('/products', methods=['POST'])
def addProducts():
    new_product = {
        "name": request.json["name"],
        "presio": request.json["presio"],
        "cantidad": request.json["cantidad"]
    }
    productos.append(new_product)
    return jsonify({"Message":"Producto agregado satisfactoriamente", "Producto agregado:": productos})

# Este script sirve para actualizar el programa cada que hayan cambios
if __name__ == "__main__":
    app.run(debug=True, port=5000)
