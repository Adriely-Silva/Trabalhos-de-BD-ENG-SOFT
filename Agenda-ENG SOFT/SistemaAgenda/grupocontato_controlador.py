from flask_restful import reqparse, abort, Resource, fields, marshal_with

from grupocontato import GrupoContato
from grupocontato_dao import GrupoContatoDao
from grupo_dao import GrupoDao
from contato_dao import ContatoDao

grupocontatoDao = GrupoContatoDao()
grupoDao = GrupoDao()
contatoDao = ContatoDao()

parser = reqparse.RequestParser()
parser.add_argument('grupo', required = True, help = "Este campo é obrigatório")
parser.add_argument('contato', required = True, help = "Este campo é obrigatório")

def encontrar_grupo(grupo_id):
    for grupo in grupoDao.consultar():
        if grupo_id == grupo.id:
            return grupo
    return None

def cancelar_grupo_se_nao_existir(grupo_id):
    if (encontrar_grupo(grupo_id) == None):
        abort(404, message="Grupo {} não existe".format(grupo_id))

def encontrar_contato(contato_id):
    for contato in contatoDao.consultar():
        if contato_id == contato.id:
            return contato
    return None

def cancelar_contato_se_nao_existir(contato_id):
    if (encontrar_contato(contato_id) == None):
        abort(404, message="Contato {} não existe".format(contato_id))

class GrupoContatoControlador(Resource):
    def post(self):
        args = parser.parse_args()
        cancelar_grupo_se_nao_existir(int(args['grupo']))
        cancelar_contato_se_nao_existir(int(args['contato']))
        grupocontato = GrupoContato(args['grupo'], args['contato'])
        resultado = grupocontatoDao.consultar(grupocontato)
        if resultado == None:
            grupocontatoDao.inserir(grupocontato)
            return "Contato foi adicionado no grupo", 201
        else:
            return "Contato já inserido no grupo", 400
    
    def delete(self):
        args = parser.parse_args()
        cancelar_grupo_se_nao_existir(int(args['grupo']))
        cancelar_contato_se_nao_existir(int(args['contato']))
        grupocontato = GrupoContato(args['grupo'], args['contato'])
        grupocontatoDao.excluir(grupocontato)
        return '', 204