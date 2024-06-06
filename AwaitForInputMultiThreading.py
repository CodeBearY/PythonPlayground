import threading
import time

# SpecificClass is defined with a run method that prints a message when it is executed.
# The input_thread function waits for user input and stores it in the global variable user_input.
# The main function creates and starts a thread to handle user input. Meanwhile, it continues to run and checks for user input in a loop.
# Once the user enters the text, the SpecificClass instance is created and its run method is called.
# The program waits for the input thread to finish using thread.join().

# Define the class that will be run after input is received
class SpecificClass:
    def run(self):
        print("SpecificClass is now running.")

# Function to handle user input
def input_thread():
    global user_input
    user_input = input("Please enter some text to continue: ")

# Main function
def main():
    global user_input
    user_input = None
    
    # Create and start the input thread
    thread = threading.Thread(target=input_thread)
    thread.start()

    # Continue running the program while waiting for user input
    print("Program is running, waiting for user input...")
    while user_input is None:
        # Simulate doing some work
        time.sleep(1)
    
    # Once input is received, run the specific class
    print(f"You entered: {user_input}")
    specific_instance = SpecificClass()
    specific_instance.run()

    # Wait for the input thread to finish
    thread.join()

# Entry point of the program
if __name__ == "__main__":
    main()
