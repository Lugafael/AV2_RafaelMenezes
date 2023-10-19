cadastrar_usuario = lambda usuarios, novo_login=input("Digite o novo login: "), nova_senha=input("Digite a nova senha: "): usuarios.append((novo_login, nova_senha))
login_usuario = lambda usuarios, login=input("Digite seu login: "), senha=input("Digite sua senha: "): any(map(lambda x: x[0] == login and x[1] == senha, usuarios))

salvar_usuarios = lambda usuarios: open("usuarios.txt", "w").writelines([f"{usuario[0]} {usuario[1]}\n" for usuario in usuarios])
carregar_usuarios = lambda: [tuple(line.strip().split()) for line in open("usuarios.txt")]

login_sucesso = lambda: print("SUCESSO")
login_falhou = lambda: print("FRACASSO")

usuarios = carregar_usuarios()
cadastrar_usuario(usuarios)
resultado_login = login_usuario(usuarios)

(lambda: login_sucesso() if resultado_login else login_falhou())()
salvar_usuarios(usuarios)
