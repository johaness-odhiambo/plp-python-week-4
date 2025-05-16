def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_filename = input("Enter the name of the file to read: ")

        # Try opening the file
        with open(input_filename, 'r') as infile:
            contents = infile.read()

        # Modify the contents (e.g., convert to uppercase)
        modified_contents = contents.upper()

        # Ask for output file name
        output_filename = input("Enter the name of the new file to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_contents)

        print(f" Successfully read from '{input_filename}' and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f" Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f" Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
