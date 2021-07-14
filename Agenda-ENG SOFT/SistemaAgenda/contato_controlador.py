from flask_restful import reqparse, abort, Resource, fields, marshal_with

from contato_dao import ContatoDao
from contato import Contato

resource_fields = {
    'id' : fields.String('', 'id'),
    'nome': fields.String('', 'nome'),
    'telefone': fields.String('', 'telefone'),
    'endereco': fields.String('', 'endereco'),
    'email': fields.String('', 'email'),
    'cidade': fields.String('', 'cidade'),
    'cep': fields.String('', 'cep'),
    'id da agenda': fields.String('', 'id_agenda')
}

contatoDao = ContatoDao()

def encontrar_contato(contato_id):
    for contato in contatoDao.consultar():
        if contato_id == contato.id:
            return contato
    return None

def cancelar_contato_se_nao_existir(contato_id):
    if (encontrar_contato(contato_id) == None):
        abort(404, message="Contato {} não existe".format(contato_id))

parser = reqparse.RequestParser()
parser.add_argument('nome', required = True, help = "Este campo é obrigatório")
parser.add_argument('telefone', required = True, help = "Este campo é obrigatório")
parser.add_argument('endereco', required = True, help = "Este campo é obrigatório")
parser.add_argument('email', required = True, help = "Este campo é obrigatório")
parser.add_argument('cidade', required = True, help = "Este campo é obrigatório")
parser.add_argument('cep', required = True, help = "Este campo é obrigatório")
parser.add_argument('id da agenda', type = int, required = True, help = "Este campo é obrigatório")

buscar_parser = reqparse.RequestParser()
buscar_parser.add_argument('nome')
buscar_parser.add_argument('cidade')
buscar_parser.add_argument('cep')

class ContatoControlador(Resource):
    @marshal_with(resource_fields)
    def get(self, contato_id):
        cancelar_contato_se_nao_existir(int(contato_id))
        return encontrar_contato(int(contato_id))

    def delete(self, contato_id):
        cancelar_contato_se_nao_existir(int(contato_id))
        contatoDao.excluir(encontrar_contato(int(contato_id)))
        return '', 204

    @marshal_with(resource_fields)
    def put(self, contato_id):
        args = parser.parse_args()
        contato = encontrar_contato(int(contato_id))
        contato.nome = args['nome']
        contato.telefone = args['telefone']
        contato.endereco = args['endereco']
        contato.email = args['email']
        contato.cidade = args['cidade']
        contato.cep = args['cep']
        contato.agenda = args['id da agenda']
        contatoDao.atualizar(contato)
        return contato, 200

class ContatosControlador(Resource):

    @marshal_with(resource_fields)
    def get(self):
        args = buscar_parser.parse_args()
        if (args['nome'] != None):
            return contatoDao.buscar_nome(args['nome'])
        elif (args['cidade'] != None):
            return contatoDao.buscar_cidade(args['cidade'])
        elif (args['cep'] != None):
            return contatoDao.buscar_cep(args['cep'])
        else:
            return contatoDao.consultar()
        
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        serial = contatoDao.serial()
        contato = Contato(serial, args['nome'], args['telefone'], args['endereco'], args['email'], args['cidade'], args['cep'], args['id da agenda'])
        contatoDao.inserir(contato)
        return contato, 201