from personajes import Guerrero, Mago, Arquero, Combate

def main():
    print("Guardians of the Ancient Kingdom")
    g1 = Guerrero("Aragorn", 100, 25, 10)
    g2 = Mago("Gandalf", 80, 30, 5)
    g3 = Arquero("Legolas", 90, 22, 8)

    print(g1.mostrar_estado())
    print(g2.mostrar_estado())
    print(g3.mostrar_estado())

    combate = Combate(g1, g2)
    combate.iniciar()

if __name__ == "__main__":
    main()
