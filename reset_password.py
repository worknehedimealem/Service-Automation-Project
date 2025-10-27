# reset_password.py
import os
import sys

def reset_bi_password(user_id):
    """
    Simulates the process of resetting a BI user's password.
    In a real scenario, this would use an API or a secure connection
    to the EDW/BI system's administration interface to perform the reset.
    """
    print(f"Starting password reset for user: {user_id}...")

    # --- Step 1: Check System Status (The Condition from the Excel) ---
    # The condition from the Excel is: "If the EDW Report system is up and running"
    edw_system_status = os.environ.get('EDW_SYSTEM_STATUS', 'up').lower()

    if edw_system_status != 'up':
        print("ERROR: The EDW Report system is NOT up and running. Aborting.")
        # Exit with a non-zero code to fail the GitHub Action
        sys.exit(1)

    print("Condition satisfied: EDW Report system is up and running.")

    # --- Step 2: Perform the Password Reset ---
    # Placeholder code. Replace with your secure, bank-approved logic.
    try:
        # Securely execute the password reset command/API call
        print(f"Successfully connected to the BI server.")
        print(f"Executing password reset command for {user_id}...")
        
        # Simulating the work done within the '10 minutes' TAT
        # In a real system, the connection and reset operation would take this time.
        
        print(f"Password for {user_id} has been reset successfully and temporary password sent.")
        
        # --- Step 3: Log the Completion ---
        print(f"Service completed successfully for TCODE EDWU-2.")
        
        # The script is successful, so we exit with code 0 (success)
        sys.exit(0)

    except Exception as e:
        print(f"CRITICAL ERROR during password reset: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # The script expects the User ID to be passed as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python reset_password.py <user_id>")
        sys.exit(1)
    
    target_user_id = sys.argv[1]
    reset_bi_password(target_user_id)
