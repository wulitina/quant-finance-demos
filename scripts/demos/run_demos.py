import os

def list_demos():
    demos_path = os.path.join(os.getcwd(), "demos")
    demos = [d for d in os.listdir(demos_path) if os.path.isdir(os.path.join(demos_path, d))]
    print("Available Demos:")
    for i, demo in enumerate(demos, start=1):
        print(f"{i}. {demo}")

def main():
    print("Welcome to Quant Finance Demos!")
    list_demos()

if __name__ == "__main__":
    main()
