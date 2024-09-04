import customtkinter

# Definindo o tema de estilos da aplicação
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Definindo as configs da tela
main_window = customtkinter.CTk()
main_window.geometry("600x400")

# Definindo os botões, textos e outros elementos
main_window_label = customtkinter.CTkLabel(main_window, text="Conversor de moedas", font=("", 20))

label_origin_coin = customtkinter.CTkLabel(main_window, text="Selecione a moeda de origem")
label_destiny_coin = customtkinter.CTkLabel(main_window, text="Selecione a moeda de destino")

allTagsCoins = ["USD", "BRL", "EUR", "BTC"]

input_origin_coin = customtkinter.CTkOptionMenu(main_window, values=allTagsCoins)
input_destiny_coin = customtkinter.CTkOptionMenu(main_window, values=allTagsCoins)


def convert_coin():
    print("Convertendo moeda...")

button_convert_coin = customtkinter.CTkButton(main_window, text="Converter", command=convert_coin)


scroll_area_list_coins = customtkinter.CTkScrollableFrame(main_window)
allTextCoin = ["USD: Dólar Americano", "BRL: Real", "EUR: Euro", "BTC: Botcoin"]
for coin in allTextCoin:
    textCoin = customtkinter.CTkLabel(scroll_area_list_coins, text=coin)
    textCoin.pack()


# Definindo os elementos na tela
main_window_label.pack(padx=10, pady=10)

label_origin_coin.pack(padx=10, pady=3)
input_origin_coin.pack(padx=10, pady=10)

label_destiny_coin.pack(padx=10, pady=3)
input_destiny_coin.pack(padx=10, pady=10)

button_convert_coin.pack(padx=10, pady=10)

scroll_area_list_coins.pack(padx=10, pady=10)


# Exibindo a tela
main_window.mainloop()