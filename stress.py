from time import sleep
import os
print("Linux cpu stresser")
answer = input("Could i kill your cpu?(y : yes, n: no) :")
if answer == 'y' or answer == 'yes':
    print("byebye")
    while True:
        os.system("yes")
else:
    print("byebye")
