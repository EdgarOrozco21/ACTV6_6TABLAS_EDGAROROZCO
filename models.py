from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.Text, nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='activo')

    # Relaciones
    proyectos = db.relationship('Proyecto', backref='cliente', lazy=True)
    campanas = db.relationship('Campana', backref='cliente', lazy=True)
    facturas = db.relationship('Factura', backref='cliente', lazy=True)

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    puesto = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20), nullable=False)
    fecha_contratacion = db.Column(db.Date, nullable=False)
    salario = db.Column(db.Float, nullable=False)
    area = db.Column(db.String(100), nullable=False)

    # Relaciones
    proyectos = db.relationship('Proyecto', backref='empleado', lazy=True)

class Proyecto(db.Model):
    __tablename__ = 'proyecto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)
    presupuesto = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='en_progreso')
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)

    # Relaciones ya definidas en Cliente y Empleado
    facturas = db.relationship('Factura', backref='proyecto', lazy=True)

class Campana(db.Model):
    __tablename__ = 'campana'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    objetivo = db.Column(db.Text, nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    # Relaciones ya definidas en Cliente

class Factura(db.Model):
    __tablename__ = 'factura'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyecto.id'), nullable=False)

    # Relaciones ya definidas en Cliente y Proyecto
