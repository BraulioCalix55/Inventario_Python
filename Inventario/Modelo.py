from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Crear la base de datos SQLite
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True muestra las consultas en consola

# Base para los modelos de datos
Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    cantidad = Column(Integer, default=0)
    descripcion = Column(String)

    # Función para agregar un producto
    @classmethod
    def agregar_producto(cls, nombre, categoria, cantidad, descripcion, session):
        nuevo_producto = cls(
            nombre=nombre,
            categoria=categoria,
            cantidad=cantidad,
            descripcion=descripcion
        )
        session.add(nuevo_producto)
        session.commit()
        print("Producto agregado correctamente.")

    # Función para obtener todos los productos
    @classmethod
    def obtener_productos(cls, session):
        productos = session.query(cls).all()
        return productos

    # Función para obtener un producto por ID
    @classmethod
    def obtener_producto_por_id(cls, producto_id, session):
        producto = session.query(cls).filter(cls.id == producto_id).first()
        return producto

    # Función para actualizar un producto
    @classmethod
    def actualizar_producto(cls, producto_id, nombre=None, categoria=None, cantidad=None, descripcion=None, session=None):
        producto = session.query(cls).filter(cls.id == producto_id).first()
        if producto:
            if nombre:
                producto.nombre = nombre
            if categoria:
                producto.categoria = categoria
            if cantidad is not None:
                producto.cantidad = cantidad
            if descripcion:
                producto.descripcion = descripcion
            session.commit()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # Función para eliminar un producto
    @classmethod
    def eliminar_producto(cls, producto_id, session):
        producto = session.query(cls).filter(cls.id == producto_id).first()
        if producto:
            session.delete(producto)
            session.commit()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Función para agregar datos de prueba solo si la tabla está vacía
    @classmethod
    def agregar_datos_prueba(cls, session):
        if session.query(cls).count() == 0:
            productos_prueba = [
                cls(nombre="Camiseta", categoria="Ropa", cantidad=50, descripcion="Camiseta de algodón"),
                cls(nombre="Zapatos", categoria="Calzado", cantidad=30, descripcion="Zapatos deportivos"),
                cls(nombre="Mochila", categoria="Accesorios", cantidad=15, descripcion="Mochila de nylon"),
            ]
            session.add_all(productos_prueba)
            session.commit()
            print("Datos de prueba agregados correctamente.")
        else:
            print("Los datos de prueba ya existen en la base de datos.")


# Crear la sesión de la base de datos
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)
'''''
# Llamar a la función para agregar datos de prueba
Producto.agregar_datos_prueba(session)

# Ejemplo de uso: agregar un producto nuevo
Producto.agregar_producto("Pantalón", "Ropa", 100, "Pantalón de mezclilla", session)

# Ejemplo de uso: obtener todos los productos
productos = Producto.obtener_productos(session)
print(productos)

# Ejemplo de uso: obtener un producto por id
producto = Producto.obtener_producto_por_id(1, session)
print(producto)

# Ejemplo de uso: actualizar un producto
Producto.actualizar_producto(1, nombre="Camiseta nueva", categoria="Ropa", cantidad=60, descripcion="Camiseta de algodón mejorada", session=session)

# Ejemplo de uso: eliminar un producto
Producto.eliminar_producto(3, session)

'''
# Cerrar la sesión
session.close()
