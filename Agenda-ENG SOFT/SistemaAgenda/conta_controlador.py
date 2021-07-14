from flask_restful import reqparse, abort, Resource, fields, marshal_with

from conta_dao import ContaDao
from conta import Conta

resource_fields = {
    'id': fields.String('', 'id'),
    'nome': fields.String('', 'nome'),
    'email': fields.String('', 'email'),
    'senha': fields.String('', 'senha')
}

contaDao = ContaDao()

def encontrar_conta(conta_id):
    for conta in contaDao.consultar():
        if conta_id == conta.id:
            return conta
    return None

def cancelar_conta_se_nao_existir(conta_id):
    if (encontrar_conta(conta_id) == None):
        abort(404, message="Conta {} não existe".format(conta_id))

parser = reqparse.RequestParser()
parser.add_argument('nome', required = True, help = "Este campo é obrigatório")
parser.add_argument('email', required = True, help = "Este campo é obrigatório")
parser.add_argument('senha', required = True, help = "Este campo é obrigatório")

login_parser = reqparse.RequestParser()
login_parser.add_argument('id', required = True, help = "Este campo é obrigatório")
login_parser.add_argument('senha', required = True, help = "Este campo é obrigatório")

class ContaControlador(Resource):
    @marshal_with(resource_fields)
    def get(self, conta_id):
        cancelar_conta_se_nao_existir(int(conta_id))
        return encontrar_conta(int(conta_id))

    def delete(self, conta_id):
        cancelar_conta_se_nao_existir(int(conta_id))
        contaDao.excluir(encontrar_conta(int(conta_id)))
        return '', 204

    @marshal_with(resource_fields)
    def put(self, conta_id):
        args = parser.parse_args()
        conta = encontrar_conta(int(conta_id))
        conta.nome = args['nome']
        conta.email = args['email']
        conta.senha = args['senha']
        contaDao.atualizar(conta)
        return conta, 201

class ContasControlador(Resource):
  
    @marshal_with(resource_fields)
    def get(self):
        return contaDao.consultar()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        serial = contaDao.serial()
        conta = Conta(serial, args['nome'], args['email'], args['senha'])
        contaDao.inserir(conta)
        return conta, 201

class LoginControlador(Resource):
    def post(self):
        args = login_parser.parse_args()
        login = contaDao.login(args['id'], args['senha'])
        if login != None:
            return login, 200
        else:
            return "Id ou Senha inválidos", 401