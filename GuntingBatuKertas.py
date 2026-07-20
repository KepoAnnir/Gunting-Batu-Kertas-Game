import random

pilihan = ["Gunting", "Batu", "Kertas"]

nyawa = 3

while nyawa > 0:
    pilih = ' '.join(pilihan) 
    print(f"\n{pilih}") 
    print("By: Pian") 
    pemain = input("Pilihan Anda: \n") 
    bot = random.choice(pilihan) 

    if pemain.lower() == "gunting" and bot.lower() == "kertas":
        print(f"\nKamu: {pemain}") 
        print(f"Bot: {bot}") 
        print("Kamu Menang!") 
        nyawa += 1
        print(f"Nyawa: {nyawa}") 
        lanjut = input("\nLanjut? (Y/N): ") 
        if lanjut.lower() == "n":
            break 
        elif lanjut.lower() == "y":
            continue
        else:
            break
    elif pemain.lower() == "gunting" and bot.lower() == "gunting":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Seri!") 
       nyawa = nyawa
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "gunting" and bot.lower() == "batu":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Kamu Kalah!") 
       nyawa -= 1
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "kertas" and bot.lower() == "gunting":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}") 
       print("Kamu Kalah!") 
       nyawa -= 1
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "kertas" and bot.lower() == "kertas":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Seri!") 
       nyawa = nyawa
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "kertas" and bot.lower() == "batu":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Kamu Menang") 
       nyawa += 1
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "batu" and bot.lower() == "gunting":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Kamu Menang!") 
       nyawa += 1
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "batu" and bot.lower() == "kertas":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Kamu Kalah!")
       nyawa -= 1
       print(f"Nyawa: {nyawa}")  
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() == "batu" and bot.lower() == "batu":
       print(f"\nKamu: {pemain}") 
       print(f"Bot: {bot}")
       print("Seri!") 
       nyawa = nyawa
       print(f"Nyawa: {nyawa}") 
       lanjut = input("\nLanjut? (Y/N): ") 
       if lanjut.lower() == "n":
           break 
       elif lanjut.lower() == "y":
           continue
       else:
           break 
    elif pemain.lower() not in pilihan:
        print("\nSalah Ketik!\n") 
        continue
    if nyawa < 1:
        print("Nyawa Habis!") 