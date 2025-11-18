from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Cliente, Empleado, Proyecto, Campana, Factura
from datetime import datetime
from sqlalchemy.orm import joinedload

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agencia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Rutas para Cliente
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes)

@app.route('/clientes/create', methods=['GET', 'POST'])
def create_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        empresa = request.form['empresa']
        correo = request.form['correo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        fecha_registro = datetime.strptime(request.form['fecha_registro'], '%Y-%m-%d').date()
        estado = request.form['estado']
        cliente = Cliente(nombre=nombre, empresa=empresa, correo=correo, telefono=telefono, direccion=direccion, fecha_registro=fecha_registro, estado=estado)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente creado exitosamente')
        return redirect(url_for('clientes'))
    return render_template('clientes/create.html')

@app.route('/clientes/<int:id>')
def show_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template('clientes/show.html', cliente=cliente)

@app.route('/clientes/<int:id>/edit', methods=['GET', 'POST'])
def edit_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.empresa = request.form['empresa']
        cliente.correo = request.form['correo']
        cliente.telefono = request.form['telefono']
        cliente.direccion = request.form['direccion']
        cliente.fecha_registro = datetime.strptime(request.form['fecha_registro'], '%Y-%m-%d').date()
        cliente.estado = request.form['estado']
        db.session.commit()
        flash('Cliente actualizado exitosamente')
        return redirect(url_for('clientes'))
    return render_template('clientes/edit.html', cliente=cliente)

@app.route('/clientes/<int:id>/delete', methods=['POST'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente eliminado exitosamente')
    return redirect(url_for('clientes'))

# Rutas para Empleado
@app.route('/empleados')
def empleados():
    empleados = Empleado.query.all()
    return render_template('empleados/index.html', empleados=empleados)

@app.route('/empleados/create', methods=['GET', 'POST'])
def create_empleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        puesto = request.form['puesto']
        correo = request.form['correo']
        telefono = request.form['telefono']
        fecha_contratacion = datetime.strptime(request.form['fecha_contratacion'], '%Y-%m-%d').date()
        salario = float(request.form['salario'])
        area = request.form['area']
        empleado = Empleado(nombre=nombre, puesto=puesto, correo=correo, telefono=telefono, fecha_contratacion=fecha_contratacion, salario=salario, area=area)
        db.session.add(empleado)
        db.session.commit()
        flash('Empleado creado exitosamente')
        return redirect(url_for('empleados'))
    return render_template('empleados/create.html')

@app.route('/empleados/<int:id>')
def show_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    return render_template('empleados/show.html', empleado=empleado)

@app.route('/empleados/<int:id>/edit', methods=['GET', 'POST'])
def edit_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.puesto = request.form['puesto']
        empleado.correo = request.form['correo']
        empleado.telefono = request.form['telefono']
        empleado.fecha_contratacion = datetime.strptime(request.form['fecha_contratacion'], '%Y-%m-%d').date()
        empleado.salario = float(request.form['salario'])
        empleado.area = request.form['area']
        db.session.commit()
        flash('Empleado actualizado exitosamente')
        return redirect(url_for('empleados'))
    return render_template('empleados/edit.html', empleado=empleado)

@app.route('/empleados/<int:id>/delete', methods=['POST'])
def delete_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    flash('Empleado eliminado exitosamente')
    return redirect(url_for('empleados'))

# Rutas para Proyecto
@app.route('/proyectos')
def proyectos():
    proyectos = Proyecto.query.all()
    return render_template('proyectos/index.html', proyectos=proyectos)

@app.route('/proyectos/create', methods=['GET', 'POST'])
def create_proyecto():
    clientes = Cliente.query.all()
    empleados = Empleado.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_entrega = datetime.strptime(request.form['fecha_entrega'], '%Y-%m-%d').date()
        presupuesto = float(request.form['presupuesto'])
        estado = request.form['estado']
        cliente_id = int(request.form['cliente_id'])
        empleado_id = int(request.form['empleado_id'])
        proyecto = Proyecto(nombre=nombre, fecha_inicio=fecha_inicio, fecha_entrega=fecha_entrega, presupuesto=presupuesto, estado=estado, cliente_id=cliente_id, empleado_id=empleado_id)
        db.session.add(proyecto)
        db.session.commit()
        flash('Proyecto creado exitosamente')
        return redirect(url_for('proyectos'))
    return render_template('proyectos/create.html', clientes=clientes, empleados=empleados)

@app.route('/proyectos/<int:id>')
def show_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    return render_template('proyectos/show.html', proyecto=proyecto)

@app.route('/proyectos/<int:id>/edit', methods=['GET', 'POST'])
def edit_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    clientes = Cliente.query.all()
    empleados = Empleado.query.all()
    if request.method == 'POST':
        proyecto.nombre = request.form['nombre']
        proyecto.fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        proyecto.fecha_entrega = datetime.strptime(request.form['fecha_entrega'], '%Y-%m-%d').date()
        proyecto.presupuesto = float(request.form['presupuesto'])
        proyecto.estado = request.form['estado']
        proyecto.cliente_id = int(request.form['cliente_id'])
        proyecto.empleado_id = int(request.form['empleado_id'])
        db.session.commit()
        flash('Proyecto actualizado exitosamente')
        return redirect(url_for('proyectos'))
    return render_template('proyectos/edit.html', proyecto=proyecto, clientes=clientes, empleados=empleados)

@app.route('/proyectos/<int:id>/delete', methods=['POST'])
def delete_proyecto(id):
    proyecto = Proyecto.query.get_or_404(id)
    db.session.delete(proyecto)
    db.session.commit()
    flash('Proyecto eliminado exitosamente')
    return redirect(url_for('proyectos'))

# Rutas para Campana
@app.route('/campanas')
def campanas():
    campanas = Campana.query.all()
    return render_template('campanas/index.html', campanas=campanas)

@app.route('/campanas/create', methods=['GET', 'POST'])
def create_campana():
    clientes = Cliente.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        objetivo = request.form['objetivo']
        fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        cliente_id = int(request.form['cliente_id'])
        campana = Campana(nombre=nombre, objetivo=objetivo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, cliente_id=cliente_id)
        db.session.add(campana)
        db.session.commit()
        flash('Campaña creada exitosamente')
        return redirect(url_for('campanas'))
    return render_template('campanas/create.html', clientes=clientes)

@app.route('/campanas/<int:id>')
def show_campana(id):
    campana = Campana.query.get_or_404(id)
    return render_template('campanas/show.html', campana=campana)

@app.route('/campanas/<int:id>/edit', methods=['GET', 'POST'])
def edit_campana(id):
    campana = Campana.query.get_or_404(id)
    clientes = Cliente.query.all()
    if request.method == 'POST':
        campana.nombre = request.form['nombre']
        campana.objetivo = request.form['objetivo']
        campana.fecha_inicio = datetime.strptime(request.form['fecha_inicio'], '%Y-%m-%d').date()
        campana.fecha_fin = datetime.strptime(request.form['fecha_fin'], '%Y-%m-%d').date()
        campana.cliente_id = int(request.form['cliente_id'])
        db.session.commit()
        flash('Campaña actualizada exitosamente')
        return redirect(url_for('campanas'))
    return render_template('campanas/edit.html', campana=campana, clientes=clientes)

@app.route('/campanas/<int:id>/delete', methods=['POST'])
def delete_campana(id):
    campana = Campana.query.get_or_404(id)
    db.session.delete(campana)
    db.session.commit()
    flash('Campaña eliminada exitosamente')
    return redirect(url_for('campanas'))

# Rutas para Factura
@app.route('/facturas')
def facturas():
    facturas = Factura.query.options(joinedload(Factura.cliente), joinedload(Factura.proyecto)).all()
    return render_template('facturas/index.html', facturas=facturas)

@app.route('/facturas/create', methods=['GET', 'POST'])
def create_factura():
    clientes = Cliente.query.all()
    proyectos = Proyecto.query.all()
    if request.method == 'POST':
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        monto = float(request.form['monto'])
        metodo_pago = request.form['metodo_pago']
        cliente_id = int(request.form['cliente_id'])
        proyecto_id = int(request.form['proyecto_id'])
        factura = Factura(fecha=fecha, monto=monto, metodo_pago=metodo_pago, cliente_id=cliente_id, proyecto_id=proyecto_id)
        db.session.add(factura)
        db.session.commit()
        flash('Factura creada exitosamente')
        return redirect(url_for('facturas'))
    return render_template('facturas/create.html', clientes=clientes, proyectos=proyectos)

@app.route('/facturas/<int:id>')
def show_factura(id):
    factura = Factura.query.options(joinedload(Factura.cliente), joinedload(Factura.proyecto)).get_or_404(id)
    return render_template('facturas/show.html', factura=factura)

@app.route('/facturas/<int:id>/edit', methods=['GET', 'POST'])
def edit_factura(id):
    factura = Factura.query.options(joinedload(Factura.cliente), joinedload(Factura.proyecto)).get_or_404(id)
    clientes = Cliente.query.all()
    proyectos = Proyecto.query.all()
    if request.method == 'POST':
        factura.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d').date()
        factura.monto = float(request.form['monto'])
        factura.metodo_pago = request.form['metodo_pago']
        factura.cliente_id = int(request.form['cliente_id'])
        factura.proyecto_id = int(request.form['proyecto_id'])
        db.session.commit()
        flash('Factura actualizada exitosamente')
        return redirect(url_for('facturas'))
    return render_template('facturas/edit.html', factura=factura, clientes=clientes, proyectos=proyectos)

@app.route('/facturas/<int:id>/delete', methods=['POST'])
def delete_factura(id):
    factura = Factura.query.get_or_404(id)
    db.session.delete(factura)
    db.session.commit()
    flash('Factura eliminada exitosamente')
    return redirect(url_for('facturas'))

if __name__ == '__main__':
    app.run(debug=True)
