from brute_force import brute_force
from datetime import datetime

etc_shadow = "/etc/shadow"
# etc_shadow = "./test/shadow"

with open(etc_shadow, "r") as f:
    lines = f.readlines()

user_list = []
for line in lines:
    username, cyphertext = line.split(":")[0], line.split(":")[1]
    if cyphertext in ["*", "!", "!!"," ","!*"]:
        continue
    else:
        user_list.append([username,cyphertext])


def user_info():
    """
    Get the user information
    :return:
    user_list: [username, cyphertext]
    min_length: [int] minimum password length
    max_length: [int] maximum password length
    required_chars: [str] required characters
    """
    print("User List")
    print("=========")
    for index,user in enumerate(user_list):
        print(f"{index+1}. {user[0]}")
    user_num = int(input("Who do I hack? >> "))-1
    min_length = int(input("Minimum password length >> "))
    max_length = int(input("Maximum password length >> "))
    print("Required characters (s: special, u: upper, l: lower, n: number)")
    required_chars = input(">> ")
    return user_list[user_num],min_length,max_length,required_chars

def main():
    """
    Main function
    """
    user_list,min_length,max_length,required_chars = user_info()
    username = user_list[0]
    cyphertext = user_list[1]
    cypher_object = cyphertext.split("$")
    cypher_type = cypher_object[1]
    if cypher_type == "y":
        cypher_salt = cypher_object[3]
    else:
        cypher_salt = cypher_object[2]

    print(f"Cracking Started to {username} ")
    print(f"Cracking Started at {datetime.now()}")

    password = brute_force(min_length,max_length,required_chars,cyphertext,cypher_type,cypher_salt)

    print(f"Cracking Finished to {username} password: {password}")
    print(f"Cracking Finished at {datetime.now()}")

if __name__ == "__main__":
    main()
