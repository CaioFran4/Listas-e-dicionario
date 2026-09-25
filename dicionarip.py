
aluno = {"nome":"Ana","nota": 8, "cel":"1198989891"}

clientes = [
    {"nome":"Ana","cel":"11878", "empresa":"FIAT"},
    {"nome":"Pedro","cel":"153232", "empresa":"INTEL"},
    {"nome":"Maria","cel":"44444", "empresa":"SEBRAE"},
    {"nome":"Felipe","cel":"55555", "empresa":"INTEL"}
]


empresa_cliente = str(input("Qual a empresa que você quer ver?: ")).upper()

for cliente in clientes:
    if cliente["empresa"] == empresa_cliente:
        print(clientes)


print("--> Cadastrando Novo Cliente <--")
nome = input("Qual o nome do Cliente?: ")
celular = input("Qual o numero de celular do Cliente?: ")
empresa = input("Qual a empresa do Cliente?: ")

novo_cliente = {
    "Nome": nome,
    "cel": celular,
    "empresa": empresa
}
clientes.append(novo_cliente)
print(clientes)

# Remover um Cliente

print("--> Removendo Um Cliente <--")
nome_cliente = input("Digite o nome do CLiente para remover: ")
for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove (cliente)
        break
print (clientes)