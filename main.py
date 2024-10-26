from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file

import io
import random
app = Flask(__name__)

Animais = {
    "Cachorro": "https://images.unsplash.com/photo-1560807707-8cc77767d783",
    "Gato": "https://images.unsplash.com/photo-1592194996308-7b43878e84a6",
    "Leão": "https://plus.unsplash.com/premium_photo-1664304310991-b43610000fc2?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Cavalo": "https://images.unsplash.com/uploads/14136148007774dc82563/ce92d553?q=80&w=1492&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Peixe": "https://images.unsplash.com/photo-1535591273668-578e31182c4f?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Pato": "https://images.unsplash.com/photo-1534627760265-69713192ade4?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Sapo": "https://images.unsplash.com/photo-1636489832249-6c73e5041a9e?q=80&w=1433&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Vaca": "https://images.unsplash.com/photo-1464472186810-92f1e85ac789?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Porco": "https://plus.unsplash.com/premium_photo-1663040364167-b8026d3307dc?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Coelho": "https://plus.unsplash.com/premium_photo-1661832480567-68a86cb46f34?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "Galinha": "https://images.pexels.com/photos/375510/pexels-photo-375510.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Rato": "https://images.pexels.com/photos/51340/rat-pets-eat-51340.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Elefante": "https://images.pexels.com/photos/133394/pexels-photo-133394.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Tigre": "https://images.pexels.com/photos/792381/pexels-photo-792381.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Panda": "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Capivara": "https://images.pexels.com/photos/20107849/pexels-photo-20107849/free-photo-of-capivara.jpeg",
    "Urso": "https://images.pexels.com/photos/3634926/pexels-photo-3634926.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Jacaré": "https://images.pexels.com/photos/769433/pexels-photo-769433.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Zebra": "https://images.pexels.com/photos/763928/pexels-photo-763928.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Girafa": "https://images.pexels.com/photos/802112/pexels-photo-802112.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
}


Cores = {
    "Vermelho": "https://cdn.awsli.com.br/600x450/1775/1775301/produto/186933607/1596d06238.jpg",
    "Azul": "https://vitrinedamadeira.com.br/wp-content/uploads/2022/08/BEN_316_2_1000x1000_31b162935e21c66b0a1de0a834fdea5e.jpg",
    "Verde": "https://cdn.awsli.com.br/998/998959/produto/96150701/c3b75ec4ab.jpg",
    "Amarelo": "https://cdn.awsli.com.br/300x300/1775/1775301/produto/183383049/3e01aab647.jpg",
    "Laranja": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuCTSLcObTj8w0N_oC8tazK8lQ95xEXfjc8w&s",
    "Rosa": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrW-jxhJdbQfdSlrVZg6MoK3ydv5Ou5GcQ5Q&s",
    "Roxo": "https://static.lojadopapel.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/c/scrapbook-neonplus-roxo.jpg",
    "Marrom": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJUQozmEBCCU5ZbBXYJg1nYsnYet9UlM5-kg&s",
    "Preto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlodFLJejUgB9OmVLnGlQwoqMVtnlkZ3teHQ&s",
    "Branco": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqqJ3oioFzLn5CDKriIzzZkpyq24pZeGakZQ&s"
}

Frutas = {
    "Maçã": "https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Pera": "https://images.pexels.com/photos/568471/pexels-photo-568471.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Uva": "https://images.pexels.com/photos/760281/pexels-photo-760281.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Manga": "https://images.pexels.com/photos/5875696/pexels-photo-5875696.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Banana": "https://images.pexels.com/photos/2872755/pexels-photo-2872755.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Melão": "https://www.proativaalimentos.com.br/image/cache/catalog/img_prod/melaoamarelo1_502698640_jpg_1024x1024[1]-1000x1000.jpg",
    "Morango": "https://images.pexels.com/photos/6944172/pexels-photo-6944172.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Laranja": "https://images.pexels.com/photos/161559/background-bitter-breakfast-bright-161559.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Limão": "https://images.pexels.com/photos/161573/background-water-breakfast-bright-161573.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Mamão": "https://images.pexels.com/photos/5945739/pexels-photo-5945739.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Coco": "https://images.pexels.com/photos/322483/pexels-photo-322483.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Abacate": "https://images.pexels.com/photos/557659/pexels-photo-557659.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Abacaxi": "https://images.pexels.com/photos/947879/pexels-photo-947879.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Melancia": "https://images.pexels.com/photos/1313267/pexels-photo-1313267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "Goiaba": "https://images.pexels.com/photos/5945840/pexels-photo-5945840.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
}



animal_index = 0
fruta_index = 0
cores_index = 0
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/animais.html')
def animais():
    global animal_index
    # Verifica se chegou ao fim da lista
    if animal_index >= len(Animais):
        animal_index = 0  # Reinicia o índice

    animal_name = list(Animais.keys())[animal_index]
    image_path = Animais[animal_name]
    animal_index += 1
    return render_template('animais.html', animal_name=animal_name, image_path=image_path)

@app.route('/frutas.html')
def frutas():
    global fruta_index
    # Verifica se chegou ao fim da lista
    if fruta_index >= len(Frutas):
        fruta_index = 0  # Reinicia o índice

    fruta_nome = list(Frutas.keys())[fruta_index]
    imagem = Frutas[fruta_nome]
    fruta_index += 1
    return render_template('frutas.html', fruta_nome=fruta_nome, imagem=imagem)

@app.route('/cores.html')
def cores():
    global cores_index
    # Verifica se chegou ao fim da lista
    if cores_index >= len(Cores):
        cores_index = 0  # Reinicia o índice

    cores_nome = list(Cores.keys())[cores_index]
    imagem_cor = Cores[cores_nome]
    cores_index += 1
    return render_template('cores.html', imagem_cor=imagem_cor, cores_nome=cores_nome)

if __name__ == '__main__' :
    app.run(debug=True)

