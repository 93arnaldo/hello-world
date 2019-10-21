# Restaurant Menu Saver

daily_menu_file = open("daily_menu_file.txt", "w+")

menu_of_today = {} #hacemos que el diccionario exista. Nuestro Menu sera un diccionario que tendra, plato y precio

daily_menu_file.write("This is your daily menu: \n")
while True:

    daily_dish = str(raw_input("Por favor, introduce el nombre del plato: "))
    
    daily_dish_price = float(raw_input("Por favor, introduce el precio del plato:"))

    print "tu plato es " + daily_dish + " y cuesta " + daily_dish_price + "Euros"
    
    menu_of_today[daily_dish] = daily_dish_price
    
    more = str(raw_input("Queres introducir otro plato a tu menu?").lower())
    
    if more == "no":
        print "OK, this is your menu: " 
        for x in menu_of_today:
            menu_of_today.write((x+1) + "menu of today[x]" + "\n")
    break

menu_of_today.close()
