import subprocess

def set_power_plan(plan_name):
    """
    Set the active power plan using its name.
    
    Parameters:
    - plan_name: Name of the power plan to set.
    """
    # Mapping of power plan names to their GUIDs
    plan_guids = {
        "ultimate Performance": "b3273f8f-c754-4ff5-811f-41529314c78c",
        "High performance": "7faa33e4-c660-4592-88f1-9642fec04d1a",
        "Power Saver": "03e8eacc-2d62-472d-bd20-879cb0139581",
        "Balanced": "9c7bdafd-41b0-4210-a2f5-4e64af06fe7c"
    }

    try:
        plan_guid = plan_guids[plan_name]
        subprocess.run(['powercfg', '/setactive', plan_guid], check=True, capture_output=True)
        print(f"Successfully set power plan to {plan_name}")
        
        # Adjust fan speed for Silent mode
        
    except KeyError:
        print(f"Unknown power plan: {plan_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting power plan: {e}")
        print("Make sure to run the script as administrator.")

if __name__ == "__main__":
    # List of power plans
    power_plans = ["ultimate Performance", "High performance", "Power Saver", "Balanced"]
    
    while True:
        # Display menu
        print("\nSelect a power plan:")
        for i, plan in enumerate(power_plans, 1):
            print(f"{i}. {plan}")
        
        try:
            choice = int(input("Enter choice (1-4): "))
            if 1 <= choice <= 4:
                selected_plan = power_plans[choice - 1]
                
                # Set selected power plan
                set_power_plan(selected_plan)
                break  # Exit the loop if a valid choice is made
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

