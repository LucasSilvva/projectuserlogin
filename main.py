from functions import menu
import mysql.connector

conexao = mysql.connector.connect(

host = "Localhost",
username = "root",
password = "root",
database ="sistema"
)

cursor = conexao.cursor()


class User:
    def __init__(self,name: str,email : str,password: str) -> None:
        self.name = name
        self.email = email
        self.password = password

    def Register(self) ->None:
        db = ("INSERT INTO user (name,password,email) values (%s,%s,%s)")
        data = (self.name,self.password,self.email)
        cursor.execute('SELECT * from  user where email = %s',(self.email))
        if cursor.fetchone():
            print('Ja existe esse email')
            return
        cursor.execute(
            (db,data)
        )
        conexao.commit()

user1 =User("Layla", "lalaprincess@gmail.com", "12345678")
user2 = User("Kushi","kushi123@gmail.com","123456")
user2.Register()
print(user2.nome, user2.email)