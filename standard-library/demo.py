import os

# --- Working with Paths ---
print("Current Working Directory:", os.getcwd())  # Prints the current working directory
print("Absolute Path of Current Directory:", os.path.abspath("."))  # Prints the absolute path of the current directory

# Example path for demonstration
example_path = os.path.join(os.getcwd(), "example", "file.txt")
print("Example Path:", example_path)

print("Base Name of Path:", os.path.basename(example_path))  # Extracts the file name
print("Directory Name of Path:", os.path.dirname(example_path))  # Extracts the directory path
print("Does Path Exist?", os.path.exists(example_path))  # Checks if the path exists

# Joining and splitting paths
joined_path = os.path.join("folder", "subfolder", "file.txt")
print("Joined Path:", joined_path)
print("Split Path:", os.path.split(joined_path))  # Splits into directory and file name
print("Split Extension:", os.path.splitext(joined_path))  # Splits file name and extension

# Normalizing paths
messy_path = "/folder//subfolder/../file.txt"
print("Normalized Path:", os.path.normpath(messy_path))  # Cleans up the path

# --- Working with Directories ---
print("\n--- Directory Operations ---")
print("Listing Current Directory:", os.listdir("."))  # Lists files in the current directory

# Create and remove directories (commented to avoid accidental changes)
# os.mkdir("new_directory")  # Creates a new directory
# os.makedirs("new_directory/sub_directory")  # Creates a directory and its parents
# os.rmdir("new_directory")  # Removes a directory (must be empty)

# --- Environment Variables ---
print("\n--- Environment Variables ---")
print("Environment Keys:", list(os.environ.keys()))  # Prints the keys of environment variables
print("Environment Values:", list(os.environ.values())[:5])  # Prints the first 5 values
print("HOME Environment Variable:", os.getenv("HOME", "Not Set"))  # Gets the HOME variable or default

# --- System Information ---
print("\n--- System Information ---")
print("OS Name:", os.name)  # Prints the name of the operating system
print("Path Separator:", os.pathsep)  # Path separator for the OS
print("Line Separator:", repr(os.linesep))  # Line separator for the OS
print("File Path Separator:", os.sep)  # File path separator for the OS

# --- System Commands ---
print("\n--- System Commands ---")
os.system("echo Hello, World!")  # Executes a system command (prints "Hello, World!")

# --- Walking Through Directory Tree ---
print("\n--- Directory Tree Walk ---")
for root, dirs, files in os.walk("."):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
    break  # Only show the first level to keep output short
