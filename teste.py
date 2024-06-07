from app.Models.model_usuario import tb_usuario
from app import app, database
from datetime import date

with app.app_context():
    # Crea todas las tablas
    #database.create_all()
    
    # Define la fecha de nacimiento correctamente usando date
    # adm = tb_usuario(
    #     nome='Douglas',
    #     sobre_nome='Santos de Jesus',
    #     email='douglas.santosads@outlook.com',
    #     cpf='36641671801',
    #     data_nascimento=date(1997, 8, 27),  # Fecha definida correctamente
    #     telefone='11948992593',
    #     senha='123'
    # )
    
    # # Añade el nuevo usuario a la sesión y comitea
    # database.session.add(adm)
    # database.session.commit()
    
    # users = tb_usuario.query.filter_by(email='douglas.santosads@outlook.com',senha='123').first()
    users = tb_usuario.query.all()
    print(users)
    