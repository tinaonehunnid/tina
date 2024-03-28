import random
import string


def generate_random_id(length=5):
    """Generate a random string of uppercase letters with the given length."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Define the number of files to generate
num_files = 10

# Loop to create each file
for _ in range(num_files):
    # Generate two random IDs
    random_id1 = generate_random_id()
    random_id2 = generate_random_id()
    
    # Construct the file name
    file_name = f"{random_id1}_HAYSTACK_{random_id2}.txt"
    
    # Create and open the file for writing
    with open(file_name, 'w') as file:
        # If you want to write specific content to the file, you can do it here
        # For example: file.write("Some content")
        pass  # Currently just creating an empty file

print(f"Generated {num_files} files.")
