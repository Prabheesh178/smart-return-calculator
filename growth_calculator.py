import json
import os

def load_history():
    filename = "calc_history.json"
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except:
            return []
    else:
        return []

def save_history(record):
    history = load_history()
    history.append(record)
    with open("calc_history.json", "w") as file:
        json.dump(history, file, indent=4)
    print("Saved to History")

def view_history():
    history = load_history()
    print("\n------Past Calculations")
    if not history:
        print("no history Found yet ")
    else:
        for i, item in enumerate(history, 1):
            print(f"{i}. {item['type']} | Invested: ₹{item['invested']:,.2f} | Profit: ₹{item['profit']:,.2f}")

def calculate_sip(monthly_amount, rate, years):
    total = 0
    months = int(years * 12)
    monthly_rate = float(rate / 100) / 12
    for i in range(months):
        total = total + monthly_amount
        interest = total * monthly_rate
        total = total + interest
    return total

def calculate_lumpsum(initial_amount, rate, years):
    final_amount = initial_amount * ((1 + rate / 100) ** years)
    return final_amount

def main():
    while True:
        print("\n___ SMART RETURN CALCULATOR____")
        print("1. Monthly SIP (Recurring)")
        print("2. One-Time Lumpsum (FD/Bond)")
        print("3. View History")
        print("4. Exit")

        choice = input("select option(1-4): ").strip()

        if choice == '4':
            print("exiting----")
            break

        if choice == "3":
            view_history()
            continue
        
        if choice in ['1', '2']:
            try:
                rate = float(input("Expected Annual Return (%): "))
                years = float(input("Time Period (Years): "))
                scheme_type = ""
                invested = 0
                final_val = 0

                if choice == "1":
                    scheme_type = "SIP"
                    amount = float(input("Monthly Investment Amount: ₹"))
                    final_val = calculate_sip(amount, rate, years)
                    invested = amount * 12 * years
                
                elif choice == "2":
                    scheme_type = "Lumpsum"
                    amount = float(input("One-Time Investment Amount: ₹"))
                    final_val = calculate_lumpsum(amount, rate, years)
                    invested = amount
                
                profit = float(final_val - invested)
                print(f"\n>> RESULT:")
                print(f"   Invested: ₹{invested:,.2f}")
                print(f"   Returns:  ₹{final_val:,.2f}")
                print(f"   Profit:   ₹{profit:,.2f}")
                
                data_packet = {
                    "type": scheme_type,
                    "invested": invested,
                    "returns": final_val,
                    "profit": profit,
                    "years": years
                }
                save_history(data_packet)
            except ValueError:
                print("!! Error: Please enter valid numbers.")
        else:
             print("Invalid selection.")

if __name__ == "__main__":
    main()

           
            
       
            
        
            
   
               
               









