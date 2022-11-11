from flask import Flask,render_template,request,redirect,flash,url_for
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = "chave-secreta-1234"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'webservices'
mysql=MySQL(app)

banco = {
    'administrador':['cpf','nome','email','pass'],
    'carrinho':['id','id_produto','cpf_cliente','quantidade'],
    'cliente':['cpf','nome','email','telefone','pass','endereco'],
    'favoritos':['id_produto','cpf_cliente'],
    'item':['id','id_produto','cpf_cliente','quantidade'],
    'produto':['id','nome','tipo','preco','quantidade'],
    'venda':['id','id_item']}

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/menu/", methods=["POST"])
def menu():
    email = request.form['email']
    senha = request.form['pass']
    
    cur = mysql.connection.cursor()

    sql = f'SELECT email,pass FROM cliente WHERE(email ="{email}")'
    cur.execute(sql)
    retorno =cur.fetchall()
    if retorno != ():
        if retorno[0][1] == senha:
            sql = 'SELECT * FROM produto'
            cur.execute(sql)
            produtos = cur.fetchall()
            cur.close()
            return render_template('menu.html', produtos = produtos)
    else:
        cur.close()
        flash("email ou senha inválido")
        return redirect('/')

@app.route('/menu/pesquisar/', methods=['POST'])
def pesquisar():
    kw = request.form['pesquisa']
    cur = mysql.connection.cursor()
    sql = f'SELECT * FROM produto WHERE(nome = "{kw}")'
    cur.execute(sql)
    produtos = cur.fetchall()
    cur.close()
    return render_template('menu.html', produtos=produtos)

@app.route('/menu/<id>/')
def produto(id):
    sql = f'SELECT * FROM produto WHERE (id ={id})' 
    cur = mysql.connection.cursor()
    cur.execute(sql)
    prod = cur.fetchall()
    cur.close()
    return render_template('produto.html', prod=prod)

@app.route('/menu/<id>/comprar/')
def comprar(id):
    sql = f'SELECT quantidade FROM produto WHERE (id ={id})'
    cur = mysql.connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    qtd = result[0][0] - 1
    sql = f'UPDATE produto SET quantidade={qtd} WHERE(id={id})'
    cur.execute(sql)
    mysql.connection.commit()
    cur.close()
    flash('Compra realizada')
    return redirect(f'/menu/{id}')

@app.route('/cadastrar/')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/verificar/', methods=["POST"])
def verificar():
    cpf = request.form['cpf']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    endereco = request.form['endereco']

    cur = mysql.connection.cursor()
    sql = f'INSERT INTO cliente (cpf,nome,email,telefone,pass,endereco)VALUES("{cpf}","{nome}","{email}","{telefone}","{senha}","{endereco}")'
    cur.execute(sql)
    mysql.connection.commit()
    cur.close()
    flash("Clente cadastrado!")
    return redirect("/")

@app.route('/loginAdm/')
def loginAdm():
    return render_template("loginAdm.html")

@app.route("/menuAdm/", methods=['POST'])
def menuAdm():
    email = request.form['email']
    senha = request.form['pass']

    cur = mysql.connection.cursor()

    sql = f'SELECT email,pass FROM administrador WHERE(email ="{email}")'
    cur.execute(sql)
    retorno =cur.fetchall()
    cur.close()
    if retorno != ():
        if retorno[0][1] == senha:
            return render_template('menuAdm.html')
    
    flash("email ou senha inválido")
    return redirect('/loginAdm/')
@app.route('/menuAdm/<tab>/', methods=['GET'])
def tabela(tab):
    tab = tab.lower()
    if tab in banco.keys():
        cur = mysql.connection.cursor()
        sql = f'SELECT * FROM {tab}'
        cur.execute(sql)
        retorno = cur.fetchall()
        cur.close() 
        dados =[]
        for i in retorno:
            intermediaria = []
            for j in i:
                intermediaria.append(j)
            dados.append(intermediaria)
        return render_template('tabela.html', tabela = tab, dados = dados ,colunas = banco[tab])
    else: 
        return render_template('tabela.html', tabela = 'inexistente')

@app.route("/menuAdm/<tab>/alteratab/", methods=['POST'])
def alteratab(tab):
    chave = request.form['chave']
    
    estrutura = banco[tab]
    valores = ""
    if ('id' not in estrutura[0]) or (estrutura[0] == 'id_cliente') : 
        chave = f'"{chave}"'
    if  "adicionar" in chave:
        campos = ""
        for i in estrutura:
            campos += i+","
            
            if 'id' in  i or 'quantidade' in i or 'preco' in i:
                valores += request.form[i]+","
            else: 
                valores += f'"{request.form[i]}",'
        campos = campos[:-1]
        valores = valores[:-1]  
        sql = f'INSERT INTO {tab} ({campos}) VALUES({valores})'
    elif "excluir" in chave:
        if 'id' in estrutura[0]:
            sql = f'DELETE FROM {tab} WHERE ({estrutura[0]} = {request.form[str(estrutura[0])]})'
        else: 
            sql = f'DELETE FROM {tab} WHERE ({estrutura[0]} = "{request.form[str(estrutura[0])]}")'
    else:
        for i in estrutura:
            item = request.form[i]
            if 'id' in  i or 'quantidade' in i or 'preco' in i:
                valores += i+f'={item}, '
            else: 
                valores += i+f'="{item}", '
        valores = valores.strip()[:-1]    
        sql = f'UPDATE {tab} SET {valores} WHERE {estrutura[0]} = {chave}'
    cur = mysql.connection.cursor()
    cur.execute(sql)
    mysql.connection.commit()
    cur.close()
    return redirect(f'/menuAdm/{tab}/')
    
if __name__=="__main__":
    app.run(host="localhost", port="5000", debug=True)