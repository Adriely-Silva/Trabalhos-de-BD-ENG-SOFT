from flask_restful import reqparse, abort, Resource, fields, marshal_with

from agenda_dao import AgendaDao
from agenda import Agenda

resource_fields = {
    'id' : fields.String('', 'id'),
    'nome': fields.String('', 'nome'),
    'id da conta': fields.String('', 'id_conta')
}

agendaDao = AgendaDao()

def encontrar_agenda(agenda_id):
    for agenda in agendaDao.consultar():
        if agenda_id == agenda.id:
            return agenda
    return None

def cancelar_agenda_se_nao_existir(agenda_id):
    if (encontrar_agenda(agenda_id) == None):
        abort(404, message="Agenda {} não existe".format(agenda_id))

parser = reqparse.RequestParser()
parser.add_argument('nome', required = True, help = "Este campo é obrigatório")
parser.add_argument('id da conta', type = int, required = True, help = "Este campo é obrigatório")

class AgendaControlador(Resource):
    @marshal_with(resource_fields)
    def get(self, agenda_id):
        cancelar_agenda_se_nao_existir(int(agenda_id))
        return encontrar_agenda(int(agenda_id))

    def delete(self, agenda_id):
        cancelar_agenda_se_nao_existir(int(agenda_id))
        agendaDao.excluir(encontrar_agenda(int(agenda_id)))
        return '', 204

    @marshal_with(resource_fields)
    def put(self, agenda_id):
        args = parser.parse_args()
        agenda = encontrar_agenda(int(agenda_id))
        agenda.nome = args['nome']
        agenda.id_conta = args['id da conta']
        agendaDao.atualizar(agenda)
        return agenda, 201

class AgendasControlador(Resource):
    
    @marshal_with(resource_fields)
    def get(self):
        return agendaDao.consultar()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        serial = agendaDao.serial()
        agenda = Agenda(serial, args['nome'], args['id da conta'])
        agendaDao.inserir(agenda)
        return agenda, 201