def create_file():
    try:
        # Create a new file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", 'w') as file:
            # Write at least three lines of text to the file
            file.write("Hello, find here system data.\n")
            file.write("Netstat logs\n")
            file.write("Routing logs. IP: 189.114.10.10\n")
        print("File created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        file.close()

def read_and_display_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", 'r') as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to open the file.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        file.close()

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", 'a') as file:
            # Append three additional lines of text to the existing content
            file.write("This is line 4 appended to the file.\n")
            file.write("67890\n")
            file.write("Appending line 6.\n")
        print("Content appended to the file successfully.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        file.close()

if __name__ == "__main__":
    create_file()
    read_and_display_file()
    append_to_file()
