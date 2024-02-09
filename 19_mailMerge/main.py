from pathlib import Path

#Placeholder to be replaced in the letter
PLACEHOLDER = "[name]"

# File Paths
name_file_path = Path("./Input/Names/invited_names.txt")
letter_file_path = Path("./Input/Letters/starting_letter.txt")
output_folder_path = Path("./Output/ReadyToSend")

#read names from the file
with name_file_path.open() as names_file:
    #iterate through each name in the file
    for name in names_file:
        #remove leading/trailing whitespaces from the name
        stripped_name = name.strip()

        # read the content of the starting letter
        with letter_file_path.open as letter_file:
            letter_contents = letter_file.read()

            #replace the placeholder with the current name
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        #define the path for the output letter file
            output_file_path = output_folder / f"letter_for_{stripped_name}.txt"

        #wrute the modified letter content to the output file
            with output_file_path.open(mode="w") as completed_letter:
                completed_letter.write(new_letter)