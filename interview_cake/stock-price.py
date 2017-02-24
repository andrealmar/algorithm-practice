def stock_prices_everyday(price_list):
    maior_preco = 0
    menor_preco = price_list[0]
    for price in price_list:
        if price > maior_preco:
            maior_preco = price
        if price < menor_preco:
            menor_preco = price
    print maior_preco, menor_preco
    return maior_preco - menor_preco

# run your function through some test cases here
# remember: debugging is half the battle!


price_list = [100, 51, 88, 92, 103, 62]

print stock_prices_everyday(price_list)
