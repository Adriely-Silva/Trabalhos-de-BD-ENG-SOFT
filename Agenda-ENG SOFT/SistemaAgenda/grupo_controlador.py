from flask_restful import reqparse, abort, Resource, fields, marshal_with

from grupo_dao import GrupoDao
from grupo import Grupo

resource_fields = {
    'nome': fields.String('', 'nome')
}

grupoDao = GrupoDao()

def encontrar_grupo(grupo_id):
    for grupo in grupoDao.consultar():
        if grupo_id == grupo.id:
            return grupo
    return None

def cancelar_grupo_se_nao_existir(grupo_id):
    if (encontrar_grupo(grupo_id) == None):
        abort(404, message="Grupo {} não existe".format(grupo_id))

parser = reqparse.RequestParser()
parser.add_argument('nome', required = True, help = "Este campo é obrigatório")

class GrupoControlador(Resource):
    @marshal_with(resource_fields)
    def get(self, grupo_id):
        cancelar_grupo_se_nao_existir(int(grupo_id))
        return encontrar_grupo(int(grupo_id))

    def delete(self, grupo_id):
        cancelar_grupo_se_nao_existir(int(grupo_id))
        grupoDao.excluir(encontrar_grupo(int(grupo_id)))
        return '', 204

    @marshal_with(resource_fields)
    def put(self, grupo_id):
        args = parser.parse_args()
        grupo = encontrar_grupo(int(grupo_id))
        grupo.nome = args['nome']
        grupoDao.atualizar(grupo)
        return grupo, 201

class GruposControlador(Resource):

    @marshal_with(resource_fields)
    def get(self):
        return grupoDao.consultar()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        serial = grupoDao.serial()
        grupo = Grupo(serial, args['nome'])
        grupoDao.inserir(grupo)
        return grupo, 201