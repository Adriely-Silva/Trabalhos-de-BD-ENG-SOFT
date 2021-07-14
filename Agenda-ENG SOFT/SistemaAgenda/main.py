from flask import Flask
from flask_restful import Api

from agenda_controlador import AgendaControlador, AgendasControlador
from conta_controlador import ContaControlador,  ContasControlador, LoginControlador
from contato_controlador import ContatoControlador, ContatosControlador
from grupo_controlador import GrupoControlador, GruposControlador
from grupocontato_controlador import GrupoContatoControlador

app = Flask(__name__) #Inicializa a aplicação
api = Api(app)

api.add_resource(LoginControlador, '/login')

api.add_resource(ContasControlador, '/conta')
api.add_resource(ContaControlador, '/conta/<conta_id>')

api.add_resource(AgendasControlador, '/agenda')
api.add_resource(AgendaControlador, '/agenda/<agenda_id>')

api.add_resource(ContatosControlador, '/contato')
api.add_resource(ContatoControlador, '/contato/<contato_id>')

api.add_resource(GruposControlador, '/grupo')
api.add_resource(GrupoControlador, '/grupo/<grupo_id>')

api.add_resource(GrupoContatoControlador, '/grupo_contato')

if __name__ == '__main__':
    app.run() #Executa a aplicação