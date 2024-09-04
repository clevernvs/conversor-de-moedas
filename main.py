import customtkinter
from get_currency import get_full_text, get_all_available_currency_code_converters

# Definindo o tema de estilos da aplicação
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Configurações da tela
main_window = customtkinter.CTk()
main_window.geometry("600x400")

# Configurações os elementos
header_label = customtkinter.CTkLabel(main_window, text="Conversor de moedas", font=("", 20))

label_origin_currency = customtkinter.CTkLabel(main_window, text="Selecione a moeda de origem")
label_destiny_currency = customtkinter.CTkLabel(main_window, text="Selecione a moeda de destino")

dic_available_converters = get_all_available_currency_code_converters()

def get_destiny_currency(currency_code):
    list_destiny_currency = dic_available_converters[currency_code]
    input_destiny_currency.configure(values=list_destiny_currency)
    input_destiny_currency.set(list_destiny_currency[0])



input_origin_currency = customtkinter.CTkOptionMenu(main_window, values=list(dic_available_converters.keys()), command=get_destiny_currency)
input_destiny_currency = customtkinter.CTkOptionMenu(main_window, values="Selecione uma moeda de origem.")


def convert_currency():
    print("Convertendo moeda...")

button_convert_currency = customtkinter.CTkButton(main_window, text="Converter", command=convert_currency)


scroll_area_list_currencys = customtkinter.CTkScrollableFrame(main_window)
all_currency_full_text = get_full_text()
for currency_code in all_currency_full_text:
    currency_name = all_currency_full_text[currency_code]
    textcurrency = customtkinter.CTkLabel(scroll_area_list_currencys, text=f"{currency_code}: {currency_name}" )
    textcurrency.pack()


# Definindo os elementos na tela
header_label.pack(padx=10, pady=10)

label_origin_currency.pack(padx=10, pady=3)
input_origin_currency.pack(padx=10, pady=10)

label_destiny_currency.pack(padx=10, pady=3)
input_destiny_currency.pack(padx=10, pady=10)

button_convert_currency.pack(padx=10, pady=10)

scroll_area_list_currencys.pack(padx=10, pady=10)


# Exibindo a tela
main_window.mainloop()