import json
if __name__ == '__main__':


    # Ruta del archivo JSON
    archivo_json = 'productos.json'

    # Cargar el archivo JSON
    with open(archivo_json, 'r', encoding='utf-8') as archivo:
     productos = json.load(archivo)

    # Recorrer e imprimir los datos de cada producto
    for producto in productos:
        print(f"ID Producto: {producto.get('id_producto')}")
        print(f"Nombre: {producto.get('nombre_producto')}")
        print(f"Categoría: {producto.get('categoria')}")
        print(f"Precio: {producto.get('precio')}")
        print(f"Cantidad Vendida: {producto.get('cantidad_vendida')}")
        print(f"Fecha de Venta: {producto.get('fecha_venta')}")
        print("-" * 40)
