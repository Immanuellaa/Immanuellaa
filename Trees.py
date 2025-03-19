# Define the directory structure using a dictionary
directory_tree = {
    "Pictures": {
        "Saved Pictures": ["Web Images", "Chrome", "Opera", "Firefox"],
        "Screenshots": [],
        "Camera Roll": ["2025", "2024", "2023"]
    }
}

# Function to display the directory structure
def display_tree(directory, level=0):
    """Recursively prints the directory structure in a tree format."""
    for key, value in directory.items():
        print("  " * level + "|-- " + key)
        if isinstance(value, dict):  # If it's a dictionary, recurse
            display_tree(value, level + 1)
        elif isinstance(value, list):  # If it's a list, print the items
            for item in value:
                print("  " * (level + 1) + "|-- " + item)

# Function to add a new directory
def add_directory(parent, new_directory):
    """Adds a new directory under a specified parent directory."""
    if parent in directory_tree:
        directory_tree[parent][new_directory] = []
    else:
        for key, value in directory_tree.items():
            if isinstance(value, dict) and parent in value:
                directory_tree[key][parent][new_directory] = []
                return
    print(f"Parent directory '{parent}' not found.")

# Function to delete a directory
def delete_directory(directory):
    """Deletes a directory and its subdirectories."""
    for key, value in directory_tree.items():
        if directory in value:
            del directory_tree[key][directory]
            return
    print(f"Directory '{directory}' not found.")

# Display the initial structure
print("Initial Directory Structure:")
display_tree(directory_tree)

# Example usage:
print("\nAdding 'Downloads' under 'Pictures':")
add_directory("Pictures", "Downloads")
display_tree(directory_tree)

print("\nDeleting 'Saved Pictures':")
delete_directory("Saved Pictures")
display_tree(directory_tree)
