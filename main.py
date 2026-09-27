alunos = []

def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    idade= int(input('Digite a idade do aluno: '))
    while True:
      nota= float(input('Digite a nota do aluno: '))
      if 0 <= nota <= 10:
          break
      else:
          print('Nota inválida. A nota deve ser de 0 a 10.')
    dados = {
        'nome':nome,
        'idade':idade,
        'nota':nota
    }
    alunos.append(dados)

def listar_alunos():
    if len(alunos) == 0:
        print('Sem alunos cadastrados')
        return
    for aluno in alunos:
        print(f"{'='*30}\nNome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n{'='*30}")

def procura_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('Sem alunos cadastrados')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
            print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}\n")
            break
    else:
        print('Esse aluno não foi encontrado')

def deletar_aluno(nome_do_aluno):
    if len(alunos) == 0:
        print('Sem alunos cadastrados')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_do_aluno.lower():
               alunos.remove(aluno)
               print(f'{nome_do_aluno} deletado com sucesso!')
               break
    else:
        print('Esse aluno não foi encontrado')

def media_de_notas():
    if len(alunos) == 0:
        print('Sem alunos cadastrados')
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f"A média das notas dos alunos é {media:.2f}")

def salvar_registro():
    if len(alunos) == 0:
        print('Sem alunos cadastrados para salvar')
        return
    
    with open("registro_alunos.txt", "a") as arquivo:
        arquivo.write("\n" + "="*40 + "\n")
        
        soma = 0
        
        for aluno in alunos:
            linha = f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}\n"
            arquivo.write(linha)
            soma += aluno['nota']
        
        media = soma / len(alunos)
        arquivo.write(f"\nMédia da turma: {media:.2f}\n")
        arquivo.write("="*40 + "\n")
    
    print("Registro salvo com sucesso!")

while True:
    opcao = int(input('\nO que deseja fazer?\n1.Adicionar aluno\n2.Listar todos os alunos\n3.Buscar aluno pelo nome\n4.Remover aluno\n5.Mostrar média geral das notas\n6.Salvar registro de alunos\n7. Sair\n'))
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input('Qual aluno deseja buscar?: ')
            procura_aluno(nome_aluno)
        case 4:
            nome_aluno = input('Qual aluno deseja remover?: ')
            deletar_aluno(nome_aluno)
        case 5:
            media_de_notas()
        case 6:
            salvar_registro()
        case 7:
            break