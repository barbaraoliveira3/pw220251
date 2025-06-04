from app import app
from flask import render_template, request, jsonify, redirect, url_for
from sqlalchemy.orm import sessionmaker

from model.conexao import engine
from model.usuario import usuario

SesssioLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



@app.route('/usuarios/novo', methods=['GET'])
def novo():
    db = SesssioLocal()
    usuarios = db.query(usuario).all();
    return render_template("index.html",obj=usuarios)

@app.route("/usuario/delete/<int:id>", methods=['GET'])
def delete_usuarios(id):
    db = SesssioLocal()
    obj = db.query(usuario).get(id)
    if (obj):
        db.delete(obj)
        db.commit()
        return redirect(url_for("novo", msg="apagado com sucesso"))
    else:
         return redirect(url_for("novo", msg="apagado com sucesso"))

@app.route('/usuarios/salvar', methods=['POST'])
def create():
    try:
        db = SesssioLocal()
        usu = usuario(nome=request.form['nome'],
                      data=request.form['aniversario'])

        db.add(usu)
        db.commit()
        msg ="salvo com sucesso"
        return redirect(url_for('novo', msg=msg))
        #return jsonify({'msg': 'Salvo+com+sucesso'}), 200
    except Exception as e:
        return jsonify({'msg': e}), 404
    return jsonify({'msg':'salvo com sucesso'}), 200
