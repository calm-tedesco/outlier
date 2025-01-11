import pandas as pd



class User:

    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):

        self.user_id = user_id

        self.username = username

        self.password = password

        self.failed_attempts = failed_attempts

        self.is_locked = is_locked



    def reset_failed_attempts(self):

        self.failed_attempts = 0

        print(f"Failed attempts reset for user {self.username}.")



    def increment_failed_attempts(self):

        self.failed_attempts += 1

        print(f"Failed attempts for {self.username}: {self.failed_attempts}")

        #BEFORE: if self.failed_attempts >= 3:
        if self.failed_attempts >= 2:

            self.lock_account()



    def lock_account(self):

        self.is_locked = True

        print(f"Account for {self.username} has been locked due to too many failed login attempts.")



class AuthenticationSystem:

    def __init__(self):

        self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts_left", "is_locked"])


    def register_user(self, user_id, username, password):

        new_user = User(user_id, username, password)

        self.users = pd.concat([self.users, pd.DataFrame({

            "user_id": [user_id], 

            "username": [username], 

            "password": [password], 

            #BEFORE: "failed_attempts_left": [3], 
            "failed_attempts_left": [0],

            "is_locked": [False]

        })], ignore_index=True) # Add new user to DataFrame.

        print(f"User {username} registered successfully.")



    # Never alter this login function

    def login(self, username, password):

        user_row = self.users[self.users['username'].str.lower() == username.lower()]

        if user_row.empty:

            print(f"User {username} not found.")

            return



        user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0], 

                    user_row['failed_attempts_left'].values[0], user_row['is_locked'].values[0])
        

        if user.is_locked:

            print(f"Account for {username} is locked. Please contact support.")

            return



        #BEFORE: if password == password:
        if password == user.password:

            #BEFORE: user.increment_failed_attempts()

            user.reset_failed_attempts()

            self.update_user(user)

            print(f"User {username} logged in successfully.")

        else:

            #BEFORE: user.reset_failed_attempts()
            user.increment_failed_attempts()

            self.update_user(user)



    def update_user(self, user):

        self.users.loc[self.users['username'] == user.username, 'failed_attempts_left'] = user.failed_attempts

        self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked

        print(f"User {user.username}'s data updated.")



auth_system = AuthenticationSystem()

print("register neena")
auth_system.register_user(1, "neena", "password123") 

print("register helios")
auth_system.register_user(2, "helios", "mysecurepassword") 

print(f"{auth_system.users}\n")

print("login 1st neena")
auth_system.login("neena", "password321")  
print(f"{auth_system.users}\n")

print("login 2nd neena")
auth_system.login("Neena", "password123")  
print(f"{auth_system.users}\n")


print("login 3rd neena")
auth_system.login("neena", "password321")  
print(f"{auth_system.users}\n")

print("login 4th neena")
auth_system.login("neena", "password123")   
print(f"{auth_system.users}\n")


print("login helios")
auth_system.login("helios", "mysecurepassword")
print(f"{auth_system.users}\n")

