while True:
    choice = input("Sten, sax, påse? ").lower()

    if choice == "sten":
        print("Datorn valde påse, du förlorade.")

    elif choice == "sax":
        print("Datorn valde sten, du förlorade.")

    elif choice == "påse":
        print("Datorn valde sax, du förlorade.")

    else:
        break