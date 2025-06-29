import os

# Define the new directory and file name
new_directory = "my_new_folder"
new_file = "my_first_file.txt"

# Create the new directory
os.makedirs(new_directory, exist_ok=True)
print(f"Directory '{new_directory}' created successfully.")

# Define the content of the file
file_content = "Hello, DevOps world! This is my first Python script."

# Create and write to the new file
with open(os.path.join(new_directory, new_file), "w") as f:
    f.write(file_content)

print(f"File '{new_file}' created in '{new_directory}'.")

