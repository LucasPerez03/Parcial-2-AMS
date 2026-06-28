from models import login_manager, Usuarios

@login_manager.user_loader  
def load_user(user_id):
    return Usuarios.query.get(int(user_id))