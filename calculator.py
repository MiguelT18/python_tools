import inquirer

choices = {
    "Si": "👍 Si",
    "No": "👎 No"
}

calculate = {
    "operations": "🧮 Operaciones aritméticas",
    "discount": "💲 Calcular descuento"
}


def main():
    question = [
        inquirer.List("size", message="¿Qué cálculo necesitas?",
                      choices=[calculate["operations"], calculate["discount"], "❌ Ninguno"])
    ]
    answer = inquirer.prompt(question)

    if answer["size"] == "Ninguno":
        print("Un gusto poder ayudarte jefe 😁")
        exit
    elif answer["size"] == calculate["discount"]:
        calculate_discount()
    elif answer["size"] == calculate["operations"]:
        basic_calculator()


def calculate_discount():
    value = ""
    percentage = ""

    while not value:
        value_str = input("Ingresa el valor total: ")
        if not value_str:
            print("Por favor ingrese un valor.")
        else:
            try:
                value = float(value_str)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

    while not percentage:
        percentage_str = input("Ingresa el descuento: ")
        if not percentage_str:
            print("Por favor ingrese un valor.")
        else:
            try:
                percentage = float(percentage_str)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

    percentage_value = (percentage * value) / 100
    total_value = value - percentage_value
    total_value_rounded = round(total_value, 2)
    print("\n" + "El resultado es 💲" + str(total_value_rounded))
    print()

    question = [
        inquirer.List(
            "size", message="¿Necesitas algún otro cálculo?", choices=[choices["Si"], choices["No"]])
    ]
    answer = inquirer.prompt(question)

    if answer["size"] == choices["No"]:
        print("Un gusto poder ayudarte jefe 😁")
        exit
    elif answer["size"] == choices["Si"]:
        main()
        exit


def basic_calculator():
    operations = {
        "Sumar": "➕ Sumar",
        "Restar": "➖ Restar",
        "Multiplicar": "✖️ Multiplicar",
        "Dividir": "➗ Dividir"
    }

    def sum():
        num1_str = input("Ingrese el primer valor: ")
        num2_str = input("Ingrese el segundo valor: ")
        result = ""

        if not num1_str and not num2_str:
            print("Por favor, ingrese un valor.")
        else:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                result = num1 + num2
                rounded_result = round(result, 2)
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

        print("\n" + str(num1) + " ➕ " + str(num2) +
              " = " + str(rounded_result) + "\n")
        final_question = [
            inquirer.List(
                "size", message="¿Necesitas realizar alguna otra operación?", choices=[choices["Si"], choices["No"]])
        ]
        final_answer = inquirer.prompt(final_question)
        if final_answer["size"] == choices["Si"]:
            basic_calculator()
        elif final_answer["size"] == choices["No"]:
            question = [
                inquirer.List(
                    "size", message="¿Necesitas algún otro cálculo?", choices=[choices["Si"], choices["No"]])
            ]
            answer = inquirer.prompt(question)
            if answer["size"] == choices["Si"]:
                main()
            elif answer["size"] == choices["No"]:
                print("Un gusto poder ayudarte jefe 😁")
                exit

    def sustract():
        num1_str = input("Ingrese el primer valor: ")
        num2_str = input("Ingrese el segundo valor: ")
        result = ""

        if not num1_str and not num2_str:
            print("Por favor, ingrese un valor.")
        else:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                result = num1 - num2
                rounded_result = round(result, 2)
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

        print("\n" + str(num1) + " ➖ " + str(num2) +
              " = " + str(rounded_result) + "\n")
        final_question = [
            inquirer.List(
                "size", message="¿Necesitas realizar alguna otra operación?", choices=[choices["Si"], choices["No"]])
        ]
        final_answer = inquirer.prompt(final_question)
        if final_answer["size"] == choices["Si"]:
            basic_calculator()
        elif final_answer["size"] == choices["No"]:
            question = [
                inquirer.List(
                    "size", message="¿Necesitas algún otro cálculo?", choices=[choices["Si"], choices["No"]])
            ]
            answer = inquirer.prompt(question)
            if answer["size"] == choices["Si"]:
                main()
            elif answer["size"] == choices["No"]:
                print("Un gusto poder ayudarte jefe 😁")
                exit

    def multiply():
        num1_str = input("Ingrese el primer valor: ")
        num2_str = input("Ingrese el segundo valor: ")
        result = ""

        if not num1_str and not num2_str:
            print("Por favor, ingrese un valor.")
        else:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                result = num1 * num2
                rounded_result = round(result, 2)
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

        print("\n" + str(num1) + " ✖️ " + str(num2) +
              " = " + str(rounded_result) + "\n")
        final_question = [
            inquirer.List(
                "size", message="¿Necesitas realizar alguna otra operación?", choices=[choices["Si"], choices["No"]])
        ]
        final_answer = inquirer.prompt(final_question)
        if final_answer["size"] == choices["Si"]:
            basic_calculator()
        elif final_answer["size"] == choices["No"]:
            question = [
                inquirer.List(
                    "size", message="¿Necesitas algún otro cálculo?", choices=[choices["Si"], choices["No"]])
            ]
            answer = inquirer.prompt(question)
            if answer["size"] == choices["Si"]:
                main()
            elif answer["size"] == choices["No"]:
                print("Un gusto poder ayudarte jefe 😁")
                exit

    def divide():
        num1_str = input("Ingrese el primer valor: ")
        num2_str = input("Ingrese el segundo valor: ")
        result = ""

        if not num1_str and not num2_str:
            print("Por favor, ingrese un valor.")
        else:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                result = num1 / num2
                rounded_result = round(result, 2)
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

        print("\n" + str(num1) + " ➗ " + str(num2) +
              " = " + str(rounded_result) + "\n")
        final_question = [
            inquirer.List(
                "size", message="¿Necesitas realizar alguna otra operación?", choices=[choices["Si"], choices["No"]])
        ]
        final_answer = inquirer.prompt(final_question)
        if final_answer["size"] == choices["Si"]:
            basic_calculator()
        elif final_answer["size"] == choices["No"]:
            question = [
                inquirer.List(
                    "size", message="¿Necesitas algún otro cálculo?", choices=[choices["Si"], choices["No"]])
            ]
            answer = inquirer.prompt(question)
            if answer["size"] == choices["Si"]:
                main()
            elif answer["size"] == choices["No"]:
                print("Un gusto poder ayudarte jefe 😁")
                exit

    init_question = [
        inquirer.List("size", message="¿Qué operación necesitas realizar?", choices=[
                      operations["Sumar"], operations["Restar"], operations["Multiplicar"], operations["Dividir"]])
    ]
    init_answer = inquirer.prompt(init_question)

    if init_answer["size"] == operations["Sumar"]:
        sum()
    elif init_answer["size"] == operations["Restar"]:
        sustract()
    elif init_answer["size"] == operations["Multiplicar"]:
        multiply()
    elif init_answer["size"] == operations["Dividir"]:
        divide()


main()
