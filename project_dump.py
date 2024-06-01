import os
import fnmatch

def parse_gitignore(file_path):
    """Parse .gitignore file and return patterns to ignore."""
    ignore_patterns = []
    negated_patterns = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.startswith('!'):
                        negated_patterns.append(line[1:])
                    else:
                        ignore_patterns.append(line)
    return ignore_patterns, negated_patterns

def should_ignore(path, ignore_patterns, negated_patterns, project_root):
    """Check if a given path should be ignored based on the patterns."""
    rel_path = os.path.relpath(path, start=project_root).replace("\\", "/")
    rel_path_lower = rel_path.lower()
    # Add a trailing slash to directories for matching
    if os.path.isdir(path):
        rel_path_lower += '/'
    # Debug: Print the relative path being checked
    print(f"Checking: {rel_path}")
    # Check negated patterns first
    for pattern in negated_patterns:
        if fnmatch.fnmatch(rel_path_lower, pattern.lower()) or fnmatch.fnmatch(os.path.basename(path).lower(), pattern.lower()):
            print(f"Not ignoring due to negated pattern: {rel_path} matches {pattern}")
            return False
    # Check ignore patterns
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(rel_path_lower, pattern.lower()) or fnmatch.fnmatch(os.path.basename(path).lower(), pattern.lower()):
            print(f"Ignoring: {rel_path} matches {pattern}")
            return True
        # Check if the pattern starts with a slash (absolute path from project root)
        if pattern.startswith('/') and fnmatch.fnmatch('/' + rel_path_lower, pattern.lower()):
            print(f"Ignoring: {rel_path} matches absolute pattern {pattern}")
            return True
    return False

def generate_folder_structure(directory, output_file, ignore_patterns, negated_patterns, indent_level=0):
    """Generate a visual representation of the folder structure, excluding ignored patterns."""
    indent = ' ' * 4 * indent_level
    with open(output_file, 'a', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(directory):
            # Check if current root directory should be ignored
            if should_ignore(root, ignore_patterns, negated_patterns, directory):
                print(f"Excluding directory: {root}")
                dirs[:] = []
                files[:] = []
                continue
            
            level = root.replace(directory, '').count(os.sep)
            if level == indent_level:
                out_file.write(f"{indent}{os.path.basename(root)}/\n")
                sub_indent = ' ' * 4 * (level + 1)

                # Apply ignore patterns to directories and files
                dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns, negated_patterns, directory)]
                files = [f for f in files if not should_ignore(os.path.join(root, f), ignore_patterns, negated_patterns, directory)]

                dirs.sort()
                files.sort()
                for d in dirs:
                    print(f"Found directory: {d}")
                    out_file.write(f"{sub_indent}{d}/\n")
                for f in files:
                    print(f"Found file: {f}")
                    out_file.write(f"{sub_indent}{f}\n")
                break

# Get the current working directory
current_directory = os.getcwd()

# Output file name
output_file = 'root_structure_filtered.txt'

# Clear the output file if it exists
if os.path.exists(output_file):
    os.remove(output_file)

# Read and parse .gitignore file
gitignore_file = os.path.join(current_directory, '.gitignore')
ignore_patterns, negated_patterns = parse_gitignore(gitignore_file)

# Debug: print the parsed patterns
print("Ignore patterns:", ignore_patterns)
print("Negated patterns:", negated_patterns)

# Generate folder structure starting from the current directory
generate_folder_structure(current_directory, output_file, ignore_patterns, negated_patterns)

print(f"Folder structure saved to {output_file}")
