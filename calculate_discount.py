def calculate_discount():    
    value = ""
    percentage = ""
    
    while not value:
        value_str = input("Ingresa el valor total: ")
        if not value_str:
            print("Por favor ingrese un valor.")
        else:
            try:
                value = int(value_str)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

    
    while not percentage:
        percentage_str = input("Ingresa el descuento: ")
        if not percentage_str:
            print("Por favor ingrese un valor.")
        else:
            try:
                percentage = int(percentage_str)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    

    percentage_value = (percentage * value) / 100
    total_value = value - percentage_value
    print("El resultado es " + str(total_value))


calculate_discount()