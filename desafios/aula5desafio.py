class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email

    def mostrar_email(self):
        return self._email
    
    def apresentar_usuario(self):
        print(f"Usuário: {self.nome} / Email: {self.mostrar_email()}")


class Aluno(Usuario):
    def apresentar_usuario(self):
        print(f"Aluno: {self.nome} / Email: {self.mostrar_email()}")
    

class Professor(Usuario):
    def apresentar_usuario(self):
        print(f"Professor: {self.nome} / Email: {self.mostrar_email()}")


usuarios = [
    Aluno("Eduardo", "eduardoguimaraes@gmail.com"),
    Professor("Filipe", "filipescmelo@gmail.com"),
    Usuario("Bruno", "Bruno@gmail.com")
]


for p in usuarios:
    p.apresentar_usuario()