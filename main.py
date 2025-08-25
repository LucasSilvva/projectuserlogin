
import mysql.connector

conexao = mysql.connector.connect(

host = "Localhost",
username = "root",
password = "root",
database ="sistema"
)

cursor = conexao.cursor()


class User:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def Register(self):
        bd = ("INSERT INTO user (nome,senha,email) values (%s,%s,%s)")
        data = (self.nome,self.senha,self.email)
        cursor.execute(bd,data)
        conexao.commit()

user1 =User("Layla", "lalaprincess@gmail.com", "12345678")
user2 = User("Kushi","kushi123@gmail.com","123456")
user2.Register()
print(user2.nome, user2.email)