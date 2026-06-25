def main():
    print("Bem-vindo ao Echos of the Classics")
    try:
        while True:
            comando = input("Digite um comando (ou 'sair' para encerrar): ").strip().lower()
            if comando in {"sair", "exit", "quit"}:
                print("Encerrando...")
                break
            if not comando:
                continue
            print(f"Comando recebido: {comando}")
    except (KeyboardInterrupt, EOFError):
        print("\nEncerrando...")


if __name__ == "__main__":
    main()
