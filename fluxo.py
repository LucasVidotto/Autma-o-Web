from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass

# --- DATACLASSES ---
@dataclass
class Titular:
    cnpj: str
    razao_social: str
    telefone: str
    email: str
    cep: str
    lagradouro: str
    n_lagradouro: str
    complemento: str
    bairro: str
    cidade: str
    estado: str

@dataclass
class Complementar:
    capital_social: str
    faturamento_anual: str
    data_fundacao: str
    tipo_empresa: str
    cnae: str

@dataclass
class Controlador:
    cpf_cnpj: str
    raao_social: str
    telefne: str
    email: str
    cep: str
    lagradouro: str
    n_lagradouro: str
    complemento: str
    bairro: str
    cidade: str
    estado: str

@dataclass
class Socios:
    cpf: str
    nome_completo: str
    rg: str
    data_emissao: str
    orgao_exped: str
    data_nascimento: str
    nome_mae: str
    nome_pai: str
    estado_civil: str
    nomeConjuge: str
    cpfConjuge : str
    renda: str
    profissao: str
    nacionalidade: str
    genero: str
    telefone: str
    email:str
    cep: str
    lagradouro: str
    n_lagradouro: str
    complemento: str
    bairro: str
    cidade: str
    estado: str

@dataclass
class Credor:
    cpf_cnpj: str
    nome_completo_razao: str
    tipo_operacao: str
    valor_operacao: str
    prazo_operacao: str

# --- FUNÇÕES AUXILIARES ---
def abrir_navegador(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def get_valor(driver, indice):
    try:
        inputs = driver.find_elements(By.TAG_NAME, "input")
        return inputs[indice].get_attribute("value")
    except IndexError:
       return f"INPUT {indice} NÃO ENCONTRADO"
    except NoSuchElementException:
       return "NÃO ENCONTRADO"

def get_valor_multiplos(driver, ids):
    for id in ids:
        try:
            elemento = driver.find_element(By.ID, id)
            return elemento.get_attribute("value")
        except NoSuchElementException:
            continue
    return "NÃO ENCONTRADO"

# --- FUNÇÃO PARA TENTAR VÁRIOS IDS NUMÉRICOS ---
def get_valor_por_ids(driver, ids):
    for id in ids:
        try:
            elemento = driver.find_element(By.ID, str(id))
            return elemento.get_attribute("value")
        except NoSuchElementException:
            continue
    return "NÃO ENCONTRADO"

# --- FUNÇÃO PARA TENTAR VÁRIOS data-cy ---
def get_valor_por_data_cy(driver, data_cy_values):
    for val in data_cy_values:
        try:
            elemento = driver.find_element(By.CSS_SELECTOR, f"[data-cy='{val}']")
            return elemento.get_attribute("value")
        except NoSuchElementException:
            continue
    return "NÃO ENCONTRADO"

# Exemplo de uso para o campo cnpj:
# cnpj = get_valor_por_data_cy(driver, ["cnpj", "cnpj_input", "cnpj_field"])

# --- CAPTURA DE DADOS ---

def capturar_dadostitular(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    return Titular(
        cnpj=get_valor_por_data_cy(driver, ["CNPJ", "cnpj", "cnpj_field"]),
        razao_social=get_valor_por_data_cy(driver, ["Razão social", "razao social", "razao_field"]),
        telefone=get_valor_por_data_cy(driver, ["Telefone celular", "telefone celular", "telefone_field"]),
        email=get_valor_por_data_cy(driver, ["E-mail", "email", "e-mail"]),
        cep=get_valor_por_data_cy(driver, ["CEP", "cep", "Cep"]),
        lagradouro=get_valor_por_data_cy(driver, ["Endereço", "ENDEREÇO", "endereço"]),
        n_lagradouro=get_valor_por_data_cy(driver, ["Número", "número", "Numero"]),
        complemento=get_valor_por_data_cy(driver, ["Complemento", "complemento", "complemento_field"]),
        bairro=get_valor_por_data_cy(driver, ["Bairro", "bairro", "bairro-input"]),
        cidade=get_valor_por_data_cy(driver, ["Cidade", "cidade", "cidade-input"]),
        estado=get_valor_por_data_cy(driver, ["Estado", "estado", "estado-input"])
    )

def capturar_dadoscomplementar(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    return Complementar(
        capital_social=get_valor(driver, 0),
        faturamento_anual=get_valor(driver, 1),
        data_fundacao=get_valor(driver, 2),
        tipo_empresa=get_valor(driver, 3),
        cnae=get_valor(driver, 4)
    )

def capturar_dadoscontrolador(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    return Controlador(
        cpf_cnpj=get_valor(driver, 0),
        raao_social=get_valor(driver, 1),
        telefne=get_valor(driver, 2),
        email=get_valor(driver, 3),
        cep=get_valor(driver, 4),
        lagradouro=get_valor(driver, 5),
        n_lagradouro=get_valor(driver, 6),
        complemento=get_valor(driver, 7),
        bairro=get_valor(driver, 8),
        cidade=get_valor(driver, 9),
        estado=get_valor(driver, 10)
    )

def capturar_dadoscredor(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    return Credor(
        cpf_cnpj=get_valor(driver, 0),
        nome_completo_razao=get_valor(driver, 1),
        tipo_operacao=get_valor(driver, 2),
        valor_operacao=get_valor(driver, 3),
        prazo_operacao=get_valor(driver, 4)
    )

def capturar_dadossocios(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    return Socios(
        cpf=get_valor(driver, 0),
        nome_completo=get_valor(driver, 1),
        rg=get_valor(driver, 2),
        data_emissao=get_valor(driver, 3),
        orgao_exped=get_valor(driver, 4),
        data_nascimento=get_valor(driver, 5),
        nome_mae=get_valor(driver, 6),
        nome_pai=get_valor(driver, 7),
        estado_civil=get_valor(driver, 8),
        nomeConjuge=get_valor(driver, 9),
        cpfConjuge=get_valor(driver, 10),
        renda=get_valor(driver, 11),
        profissao=get_valor(driver, 12),
        nacionalidade=get_valor(driver, 13),
        genero=get_valor(driver, 14),
        telefone=get_valor(driver, 15),
        email=get_valor(driver, 16),
        cep=get_valor(driver, 17),
        lagradouro=get_valor(driver, 18),
        n_lagradouro=get_valor(driver, 19),
        complemento=get_valor(driver, 20),
        bairro=get_valor(driver, 21),
        cidade=get_valor(driver, 22),
        estado=get_valor(driver, 23)
    )

# --- JANELAS DE INSTRUÇÃO ---
def mostrar_instrucoes(driver, ao_salvar):
    def fechar():
        ao_salvar()
        root.destroy()
    root = tk.Tk()
    root.title("Instruções para Titular")
    root.geometry("520x320")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=260)
    label_titulo = tk.Label(frame, text="Atenção!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    instrucoes = (
        "1 - Faça login normalmente no sistema e avance pelas abas até chegar na tela de preenchimento dos dados do Titular.\n\n"
        "2 - Preencha todos os campos do Titular.\n\n"
        "3 - Antes de clicar em 'Avançar' no site, clique em 'Salvar' nesta janela para capturar os dados corretamente."
    )
    label_mensagem = tk.Label(frame, text=instrucoes, font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=440, justify="left")
    label_mensagem.pack(pady=(0, 12))
    btn_frame = tk.Frame(frame, bg="#ffffff")
    btn_frame.pack()
    btn_salvar = tk.Button(
        btn_frame, text="Salvar", command=fechar,
        font=("Arial", 13, "bold"), bg="#27ae60", fg="white",
        activebackground="#219150", activeforeground="white",
        width=14, height=1, bd=0, relief="ridge"
    )
    btn_salvar.pack(side="left", padx=10)
    root.mainloop()

def mostrar_segunda_instrucao(driver, ao_salvar):
    def fechar():
        ao_salvar()
        root.destroy()
    root = tk.Tk()
    root.title("Instruções para Controlador")
    root.geometry("480x300")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=240)
    label_titulo = tk.Label(frame, text="Atenção!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    instrucoes = (
        "1 - Avance para a aba Controlador e preencha os dados.\n"
        "2 - Após preencher, clique em 'Salvar' para capturar os dados."
    )
    label_mensagem = tk.Label(frame, text=instrucoes, font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=400, justify="left")
    label_mensagem.pack(pady=(0, 12))
    btn_frame = tk.Frame(frame, bg="#ffffff")
    btn_frame.pack()
    btn_salvar = tk.Button(
        btn_frame, text="Salvar", command=fechar,
        font=("Arial", 13, "bold"), bg="#27ae60", fg="white",
        activebackground="#219150", activeforeground="white",
        width=12, height=1, bd=0, relief="ridge"
    )
    btn_salvar.pack(side="left", padx=10)
    root.mainloop()

def mostrar_terceira_instrucao(driver, ao_salvar):
    def fechar():
        ao_salvar()
        root.destroy()
    root = tk.Tk()
    root.title("Instruções para Credor")
    root.geometry("480x300")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=240)
    label_titulo = tk.Label(frame, text="Atenção!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    instrucoes = (
        "1 - Avance para a aba Credor e preencha os dados.\n"
        "2 - Após preencher, clique em 'Salvar' para capturar os dados."
    )
    label_mensagem = tk.Label(frame, text=instrucoes, font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=400, justify="left")
    label_mensagem.pack(pady=(0, 12))
    btn_frame = tk.Frame(frame, bg="#ffffff")
    btn_frame.pack()
    btn_salvar = tk.Button(
        btn_frame, text="Salvar", command=fechar,
        font=("Arial", 13, "bold"), bg="#27ae60", fg="white",
        activebackground="#219150", activeforeground="white",
        width=12, height=1, bd=0, relief="ridge"    
    )
    btn_salvar.pack(side="left", padx=10)
    root.mainloop()

def mostrar_instrucao_complementar(driver, ao_salvar):
    def fechar():
        ao_salvar()
        root.destroy()
    root = tk.Tk()
    root.title("Instruções para Dados Complementares")
    root.geometry("480x300")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=240)
    label_titulo = tk.Label(frame, text="Atenção!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    instrucoes = (
        "1 - Avance para a aba de Dados Complementares e preencha os dados.\n"
        "2 - Após preencher, clique em 'Salvar' para capturar os dados."
    )
    label_mensagem = tk.Label(frame, text=instrucoes, font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=400, justify="left")
    label_mensagem.pack(pady=(0, 12))
    btn_frame = tk.Frame(frame, bg="#ffffff")
    btn_frame.pack()
    btn_salvar = tk.Button(
        btn_frame, text="Salvar", command=fechar,
        font=("Arial", 13, "bold"), bg="#27ae60", fg="white",
        activebackground="#219150", activeforeground="white",
        width=12, height=1, bd=0, relief="ridge"
    )
    btn_salvar.pack(side="left", padx=10)
    root.mainloop()


def mostrar_instrucao_socios(driver, ao_salvar):
    def fechar():
        ao_salvar()
        root.destroy()
    root = tk.Tk()
    root.title("Instruções para Sócios")
    root.geometry("480x300")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=240)
    label_titulo = tk.Label(frame, text="Atenção!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    instrucoes = (
        "1 - Avance para a aba Sócios e preencha os dados.\n"
        "2 - Após preencher, clique em 'Salvar' para capturar os dados."
    )
    label_mensagem = tk.Label(frame, text=instrucoes, font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=400, justify="left")
    label_mensagem.pack(pady=(0, 12))
    btn_frame = tk.Frame(frame, bg="#ffffff")
    btn_frame.pack()
    btn_salvar = tk.Button(
        btn_frame, text="Salvar", command=fechar,
        font=("Arial", 13, "bold"), bg="#27ae60", fg="white",
        activebackground="#219150", activeforeground="white",
        width=12, height=1, bd=0, relief="ridge"
    )
    btn_salvar.pack(side="left", padx=10)
    root.mainloop()

# --- SALVAR NO TXT ---
def salvar_dados(titular, complementar, socios, controlador, credor):
    with open("dadospj.txt", "w", encoding="utf-8") as f:
        f.write("=== Dados do Titular ===\n")
        f.write(f"{titular.cnpj}\n")
        f.write(f"{titular.razao_social}\n")
        f.write(f"{titular.telefone}\n")
        f.write(f"{titular.email}\n")
        f.write(f"{titular.cep}\n")
        f.write(f"{titular.lagradouro}\n")
        f.write(f"{titular.n_lagradouro}\n")
        f.write(f"{titular.complemento}\n")
        f.write(f"{titular.bairro}\n")
        f.write(f"{titular.cidade}\n")
        f.write(f"{titular.estado}\n\n")

        f.write("=== Dados Complementares ===\n")
        f.write(f"{complementar.capital_social}\n")
        f.write(f"{complementar.faturamento_anual}\n")
        f.write(f"{complementar.data_fundacao}\n")
        f.write(f"{complementar.tipo_empresa}\n")
        f.write(f"{complementar.cnae}\n\n")

        f.write("=== Dados do Controlador ===\n")
        f.write(f"{controlador.cpf_cnpj}\n")
        f.write(f"{controlador.raao_social}\n")
        f.write(f"{controlador.telefne}\n")
        f.write(f"{controlador.email}\n")
        f.write(f"{controlador.cep}\n")
        f.write(f"{controlador.lagradouro}\n")
        f.write(f"{controlador.n_lagradouro}\n")
        f.write(f"{controlador.complemento}\n")
        f.write(f"{controlador.bairro}\n")
        f.write(f"{controlador.cidade}\n")
        f.write(f"{controlador.estado}\n\n")

        f.write("=== Dados dos Sócios ===\n")
        f.write(f"{socios.cpf}\n")
        f.write(f"{socios.nome_completo}\n")
        f.write(f"{socios.rg}\n")
        f.write(f"{socios.data_emissao}\n")
        f.write(f"{socios.orgao_exped}\n")
        f.write(f"{socios.data_nascimento}\n")
        f.write(f"{socios.nome_mae}\n")
        f.write(f"{socios.nome_pai}\n")
        f.write(f"{socios.estado_civil}\n")
        f.write(f"{socios.nomeConjuge}\n")
        f.write(f"{socios.cpfConjuge}\n")
        f.write(f"{socios.renda}\n")
        f.write(f"{socios.profissao}\n")
        f.write(f"{socios.nacionalidade}\n")
        f.write(f"{socios.genero}\n")
        f.write(f"{socios.telefone}\n")
        f.write(f"{socios.email}\n")
        f.write(f"{socios.cep}\n")
        f.write(f"{socios.lagradouro}\n")
        f.write(f"{socios.n_lagradouro}\n")
        f.write(f"{socios.complemento}\n")
        f.write(f"{socios.bairro}\n")
        f.write(f"{socios.cidade}\n")
        f.write(f"{socios.estado}\n\n")

        f.write("=== Dados do Credor ===\n")
        f.write(f"{credor.cpf_cnpj}\n")
        f.write(f"{credor.nome_completo_razao}\n")
        f.write(f"{credor.tipo_operacao}\n")
        f.write(f"{credor.valor_operacao}\n")
        f.write(f"{credor.prazo_operacao}\n")
    print("Todos os dados capturados e salvos em dados.txt!")

def mostrar_finalizacao(ao_finalizar):
    def fechar():
        ao_finalizar()
        root.destroy()
    root = tk.Tk()
    root.title("Finalização")
    root.geometry("480x280")
    root.configure(bg="#e9ecef")
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=200)
    label_titulo = tk.Label(frame, text="Processo Finalizado!", font=("Arial", 16, "bold"), bg="#ffffff", fg="#2c3e50")
    label_titulo.pack(pady=(18, 8))
    label_mensagem = tk.Label(
        frame,
        text="Todos os dados foram salvos.\n\nFinalize o processo no site (clique em 'Concluir' na plataforma).\n\nDepois disso, clique em 'Finalizar' aqui para encerrar o sistema.",
        font=("Arial", 11), bg="#ffffff", fg="#495057", wraplength=400, justify="center"
    )
    label_mensagem.pack(pady=(0, 12))
    btn_finalizar = tk.Button(
        frame, text="Finalizar", command=fechar,
        font=("Arial", 13, "bold"), bg="#2980b9", fg="white",
        activebackground="#1c5a85", activeforeground="white",
        width=16, height=1, bd=0, relief="ridge"
    )
    btn_finalizar.pack(pady=(0, 10))
    root.mainloop()

def main():
    url = "https://webapp.exmpartners.com.br/users/login"
    driver = abrir_navegador(url)
    resultado = {}

    def salvar_titular():
        resultado['titular'] = capturar_dadostitular(driver)

    def salvar_complementar():
        resultado['complementar'] = capturar_dadoscomplementar(driver)

    def salvar_socios():
        resultado['socios'] = capturar_dadossocios(driver)

    def salvar_controlador():
        resultado['controlador'] = capturar_dadoscontrolador(driver)

    def salvar_credor():
        resultado['credor'] = capturar_dadoscredor(driver)
        salvar_dados(
            resultado['titular'],
            resultado['complementar'],
            resultado['socios'],
            resultado['controlador'],
            resultado['credor']
        )

    def finalizar():
        driver.quit()

    mostrar_instrucoes(driver, salvar_titular)
    mostrar_instrucao_complementar(driver, salvar_complementar)
    mostrar_instrucao_socios(driver, salvar_socios)
    mostrar_segunda_instrucao(driver, salvar_controlador)
    mostrar_terceira_instrucao(driver, salvar_credor)
    mostrar_finalizacao(finalizar)

if __name__ == "__main__":
    main()