import math

# Coordenadas das capitais brasileiras (latitude, longitude)
capitais = {
    "Aracaju": (-10.91758, -37.06499),
    "Belém": (-1.45749, -48.50539),
    "Belo Horizonte": (-19.85213, -43.99275),
    "Boa Vista": (2.82031, -60.67194),
    "Brasília": (-15.79392, -47.88294),
    "Campo Grande": (-19.32132, -54.58787),
    "Cuiabá": (-15.60906, -56.08447),
    "Curitiba": (-25.42941, -49.27127),
    "Florianópolis": (-27.70552, -48.50597),
    "Fortaleza": (-3.69373, -38.58625),
    "Goiânia": (-16.6804, -49.25637),
    "João Pessoa": (-7.11550, -34.88452),
    "Macapá": (0.00075, -51.07821), 
    "Maceió": (-9.66537, -35.73586),
    "Manaus": (-3.13645, -60.02525),
    "Natal": (-5.15629, -35.49962),
    "Palmas": (-10.18193, -48.33361),
    "Porto Alegre": (-30.02815, -51.22855),
    "Porto Velho": (-8.76280, -63.90861),
    "Recife": (-8.06296, -34.87117),
    "Rio Branco": (-9.97320, -67.80653),
    "Rio de Janeiro": (-22.91923, -43.21495),
    "Salvador": (-13.00189, -38.53293),
    "São Luís": (-2.52764, -44.30779),
    "São Paulo": (-23.55028, -46.63394),
    "Teresina": (-5.09026, -42.81666),
    "Vitória": (-20.32190, -40.33973)
}

def haversine(coord1, coord2):
    # Coordenadas são dadas em graus, vamos convertê-las para radianos
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Fórmula haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Raio da Terra em quilômetros
    return c * r

def main():
    print("Bem-vindo ao calculador de distâncias entre capitais brasileiras!")
    print("Capitais disponíveis:")
    for capital in capitais:
        print(capital)
    
    cidade1 = input("\nDigite o nome da primeira capital: ")
    cidade2 = input("Digite o nome da segunda capital: ")

    if cidade1 in capitais and cidade2 in capitais:
        distancia = haversine(capitais[cidade1], capitais[cidade2])
        print(f"A distância entre {cidade1} e {cidade2} é de aproximadamente {distancia:.2f} km.")
    else:
        print("Uma ou ambas as capitais inseridas não são válidas. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

