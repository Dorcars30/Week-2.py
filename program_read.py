def program_read():

    filename = input("program_read: ")
print(program_read)

        with open(filename, 'r') as file:
            content = file.read()
            print("program_read")
        modified_content = content.upper()
print(program_read)
        new_filename = f"modified_{filename}"

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f" Modified  '{new_filename}'.")

    
        


program_read()
