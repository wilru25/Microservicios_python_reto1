from ninja import NinjaAPI
from usuarios.models import Usuario
from usuarios.schemas import UsuarioSchema, UsuarioCreateSchema
from django.shortcuts import get_object_or_404

api = NinjaAPI()


'''@api.get("/usuarios/")
def list_usuarios(request):
    return list(Usuario.objects.all().values())
'''
@api.get("/usuarios/")
def list_usuarios(request):
    usuarios = Usuario.objects.all()
    return [{"id": usuario.id, "nombre": usuario.nombre, "apellido_paterno": usuario.apellido_paterno, "apellido_materno": usuario.apellido_materno, "edad": usuario.edad, "nombre_cuenta": usuario.nombre_cuenta, "contraseña": usuario.contraseña} for usuario in usuarios]


'''@api.post("/usuarios/")
def create_usuario(request, data: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**data.dict())
    return usuario
'''
@api.post("/usuarios/")
def create_usuario(request, data: UsuarioCreateSchema):
    usuario = Usuario.objects.create(**data.dict())
    return {"id": usuario.id, "nombre": usuario.nombre, "apellido_paterno": usuario.apellido_paterno, "apellido_materno": usuario.apellido_materno, "edad": usuario.edad, "nombre_cuenta": usuario.nombre_cuenta, "contraseña": usuario.contraseña}


'''@api.put("/usuarios/{usuario_id}/")
def update_usuario(request, usuario_id: int, data: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in data.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return usuario
'''
@api.put("/usuarios/{usuario_id}/")
def update_usuario(request, usuario_id: int, data: UsuarioCreateSchema):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    for attr, value in data.dict().items():
        setattr(usuario, attr, value)
    usuario.save()
    return {"id": usuario.id, "nombre": usuario.nombre, "apellido_paterno": usuario.apellido_paterno, "apellido_materno": usuario.apellido_materno, "edad": usuario.edad, "nombre_cuenta": usuario.nombre_cuenta, "contraseña": usuario.contraseña}

'''
@api.delete("/usuarios/{usuario_id}/")
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
'''
@api.delete("/usuarios/{usuario_id}/")
def delete_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return {"success": True}
