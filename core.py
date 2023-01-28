def is_interactive():
	usr = input('Please input your name: ')
	print(f"Welcome player {usr}!")

_itc = input("Go with interactive mode? Y/n : ")

if _itc == 'Y':
	is_interactive()
elif _itc == 'n':
	print("We fly without interaction.")
else:
	print("Aborting.")
#added comment
