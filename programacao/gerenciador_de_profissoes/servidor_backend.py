from config import *
from profissao import Profissao

@app.route("/")
def inicio():
    return 'Sistema para cadastrar profissões. '+\
        '<a href="/listar_profissoes">Listar Profissões</a>'

@app.route("/listar_profissoes")
def listar_profissoes():
    profissoes = db.session.query(Profissao).all()
    profissao_em_json = [ x.json() for x in profissoes ]
    # formato json
    return jsonify(profissao_em_json)

app.run(debug=True)