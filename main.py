import pyjokes

def main():
    print("Hello World! Let me tell you a joke.")
    print(pyjokes.get_joke(language="en", category="neutral"))

if __name__ == "__main__":
    main()
