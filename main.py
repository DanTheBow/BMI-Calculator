print("Sie möchten sich Ihren BMI berechnen lassen?")
print("Nichts leichter als das! Tragen Sie Ihre Körpergröße und Ihr Gewicht ein.")
print("Dann können Sie Ihren BMI berechnen lassen.")
print()


def your_bmi(height, weight):
    bmi = round(weight / height ** 2, 1)
    print("Ihr BMI beträgt: " + str(bmi))

    if bmi <= 17.5:
        print("Kritisches Untergewicht")
    elif bmi <= 20:
        print("Untergewicht")
    elif bmi <= 26:
        print("Normalgewicht")
    elif bmi <= 31:
        print("Leichtes Übergewicht")
    else:
        print("Übergewicht")


your_height = float(input("Geben Sie Ihre Größe in m ein: "))
your_weight = float(input("Geben Sie Ihr Gewicht in Kg ein: "))

your_bmi(your_height, your_height)
