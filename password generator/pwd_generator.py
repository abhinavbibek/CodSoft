import string
import random

def generate_pwd(n):
    all_characters= (
        list(string.ascii_lowercase) +
        list(string.ascii_uppercase) +
        list(string.digits) +
        list(string.punctuation))
    random.shuffle(all_characters)
    password=random.sample(all_characters,n)
    password=''.join(password)
    return password

def main():
    n=int(input("enter no of characters for pwd:"))
    if(n<8):
        print("pwd should be longer than 8")
    else:
        pwd= generate_pwd(n)
    print("strong password:",pwd)
    
if __name__ == "__main__":
    main()
