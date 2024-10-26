from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

animais = {
    "Cachorro" : "animais/cachorro.jpg",
    "Gato" : "animais/gato.jpg",
    "Leão" : "animais/leao.jpg",
    "Cavalo" : "animais/cavalo.jpg",
    "Peixe" : "animais/peixe.jpg",
    "Pato" : "animais/pato.jpg",
    "Sapo" : "animais/sapo.jpg",
    "Vaca" : "animais/vaca.jpg",
    "Porco" : "animais/porco.jpg",
    "Coelho" : "animais/coelho.jpg",
    "Galinha" : "animais/galinha.jpg",
    "Rato" : "animais/rato.jpg",
    "Elefante" : "animais/elefante.jpg",
    "Tigre" : "animais/tigre.jpg",
    "Panda" : "animais/panda.jpg",
    "Macaco" : "animais/macaco.jpg",
    "Urso" : "animais/urso.jpg",
    "Jacaré" : "animais/jacare.jpg",
    "Zebra" : "animais/zebra.jpg",
    "Girafa" : "animais/girafa.jpg"
}
Cores = {
    "Vermelho": "cores/vermelho.jpg",
    "Azul": "cores/azul.jpg",
    "Verde": "cores/verde.png",
    "Amarelo": "cores/amarelo.png",
    "Laranja": "core/laranja.png",
    "Rosa": "cores/rosa.jpg",
    "Roxo": "cores/roxo.png",
    "Marrom": "cores/marrom.png",
    "Preto": "cores/pretos.jpg",
    "Branco": "cores/branco.jpg"
}

Objetos = {
    "Mesa": "objetos/mesa.jpg",
    "Cama": "objetos/cama.jpg",
    "Sofá": "objetos/sofa.jpg",
    "Copo": "objetos/copo.jpg",
    "Prato": "objetos/prato.jpg",
    "Faca": "objetos/faca.jpg",
    "Colher": "objetos/colher.jpg",
    "Garrafa": "objetos/garrafa.jpg",
    "Livro": "objetos/livro.jpg",
    "Pente": "objetos/pente.jpg",
    "Bola": "objetos/bola.jpg",
    "Lápis": "objetos/lapis.jpg",
    "Papel": "objetos/papel.jpg",
    "Toalha": "objetos/toalha.jpg",
    "Chave": "objetos/chave.jpg",
    "Cadeira": "objetos/cadeira.jpg",
    "Janela": "objetos/janela.jpg",
    "Balde": "objetos/balde.jpg",
    "Escova": "objetos/escova.jpg",
    "Tesoura": "objetos/tesoura.jpg"
}
Esporte = {
    "Futebol": "esporte/futebol.jpg",
    "Basquete": "esporte/basquete.jpg",
    "Vôlei": "esporte/volei.jpg",
    "Tênis": "esporte/tenis.jpg",
    "Natação": "esporte/natacao.jpg",
    "Corrida": "esporte/corrida.jpg",
    "Boxe": "esporte/boxe.jpg",
    "Golfe": "esporte/golfe.jpg",
    "Judô": "esporte/judo.jpg",
    "Dança": "esporte/danca.jpg",
    "Skate": "esporte/skate.jpg",
    "Patins": "esporte/patins.jpg",
    "Pular": "esporte/pular.jpg",
    "Peteca": "esporte/peteca.jpg",
    "Queimada": "esporte/queimada.jpg",
    "Bambolê": "esporte/bambole.jpg",
    "Esconde": "esporte/esconde.jpg",
    "Correr": "esporte/correr.jpg",
    "Bicicleta": "esporte/bicicleta.jpg",
    "Corda": "esporte/corda.jpg"
}

Frutas = {
    "Maçã": "frutas/maca.jpg",
    "Pera": "frutas/pera.jpg",
    "Uva": "frutas/uva.jpg",
    "Manga": "frutas/manga.jpg",
    "Banana": "frutas/banana.jpg",
    "Melão": "frutas/melao.jpg",
    "Morango": "frutas/morango.jpg",
    "Laranja": "frutas/laranja.jpg",
    "Limão": "frutas/limao.jpg",
    "Mamão": "frutas/mamao.jpg",
    "Coco": "frutas/coco.jpg",
    "Abacate": "frutas/abacate.jpg",
    "Abacaxi": "frutas/abacaxi.jpg",
    "Melancia": "frutas/melancia.jpg",
    "Ameixa": "frutas/ameixa.jpg",
    "Amora": "frutas/amora.jpg",
    "Pêssego": "frutas/pessego.jpg",
    "Cereja": "frutas/Cereja.jpg",
    "Caju": "frutas/caju.jpg",
    "Goiaba": "frutas/goiaba.jpg"
}

Corpo = {
    "Cabeça": "corpo/cabeca.jpg",
    "Braço": "corpo/braco.jpg",
    "Perna": "corpo/perna.jpg",
    "Mão": "corpo/mao.jpg",
    "Pé": "corpo/pe.jpg",
    "Olho": "corpo/olho.jpg",
    "Boca": "corpo/boca.jpg",
    "Dente": "corpo/dente.jpg",
    "Nariz": "corpo/nariz.jpg",
    "Orelha": "corpo/orelha.jpg",
    "Cabelo": "corpo/cabelo.jpg",
    "Unha": "corpo/unha.jpg",
    "Barriga": "corpo/barriga.jpg",
    "Língua": "corpo/lingua.jpg",
    "Costas": "corpo/costas.jpg",
    "Bochecha": "corpo/bochecha.jpg",
    "Joelho": "corpo/joelho.jpg",
    "Calcanhar": "corpo/calcanhar.jpg",
    "Pulso": "corpo/pulso.jpg"
}


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__' :
    app.run(debug=True)

