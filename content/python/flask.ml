<h1>Flask (framework web)</h1>

<h3>Flask é um pequeno framework web escrito em Python.</h3>

<p>É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, 
mantendo um núcleo simples, porém, extensível.Não possui camada de abstração de banco de dados, 
validação de formulário ou quaisquer outros componentes onde bibliotecas de terceiros pré-existentes fornecem funções comuns. 
No entanto, o Flask oferece suporte a extensões que podem adicionar recursos do aplicativo como se fossem implementados no próprio Flask. 
Existem extensões para mapeadores objeto-relacional, validação de formulário, manipulação de upload, 
várias tecnologias de autenticação aberta e várias ferramentas comuns relacionadas ao framework.</p>

<p>Aplicações que utilizam o framework Flask incluem a própria página da comunidade de desenvolvedores, o Pinterest e o LinkedIn.</p>
<p>Exemplo: <hr>
<small>O código abaixo mostra uma aplicação web simples que imprime na tela do navegador "Olá mundo!": </small>
<pre>
	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
		return "Olá mundo!"

	if __name__ == "__main__":
		app.run()
<pre>
</p>