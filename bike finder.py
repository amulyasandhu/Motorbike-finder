try:
    from ai import call_gpt
except ImportError:
    def call_gpt(prompt):
        return "AI feature not configured. Please connect an API."

def main():
    bike = input("Tell the name of the motorbike: ")
    print("Revving up the details of your motorbike... ")
    print(call_gpt(f"Give details of the {bike} - Include its model history, engine specs, top speed, mileage, design, features, price range, and ideal user"))

if __name__ == "__main__":
    main()