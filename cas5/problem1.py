

class User:
    def __init__(self, first_name, last_name, username, password):
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.password = password
            self.login_attempts = 0
    def greet_user(self):
          print(f"Hello {self.first_name}")
    
    def describe_user(self):
          print(self.first_name)
          print(self.last_name)
          print(self.username)
          print(self.password)
    
    def increment_login(self):
        if self.login_attempts < 3:
            self.login_attempts += 1
        else:
             print("User blocked")

    def reset_login_attempts(self):
         self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
        self.privileges = ["can add post", "can delete post", "can ban a user"]
    
    def show_privileges(self):
         print("admin privileges")
         for i in self.privileges:
              print(i)


# lista = list([1,2,3]) 
admin = Admin("Seid", "krsic", "seid", "123")
print(admin.show_privileges())