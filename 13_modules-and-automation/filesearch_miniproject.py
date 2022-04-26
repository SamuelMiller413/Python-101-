# Write a script that searches a folder you specify 
# (as well as its subfolders, up to two levels deep) and 
# compiles a list of all .jpg files contained in there. 
# The list should include the complete path of each .jpg file.

# You should train:

# Using for loops
# Using conditional statements
# Working with pathlib
# Thinking about nested loops

import pathlib

path_pictures = pathlib.Path("/Users/admin/")

# pathlib.Path("/Users/admin/Documents/documents_practice")
# path_documents_practice = pathlib.Path("/Users/admin/Documents/documents_practice")
# str(path_documents_practice)

# new_path = pathlib.Path('/Users/admin/Documents/documents_practice')
# new_path.mkdir(exist_ok=True)

# Most Recent:
# for filepath in path_documents_practice.iterdir():
#     new_zoo_name = filepath.name
#     new_zoo_name += f"change_{num}"

    # filepath.with_name()
    # if filepath.suffix == '.docx':
    #     new_filepath = new_path.joinpath(filepath.name)
    #     filepath.replace(new_filepath)

# for filepath in path_pictures.iterdir():
#     if filepath.suffix == '.JPG':
#         new_filepath= new_path.joinpath(filepath.name)
#         filepath.replace(new_filepath)



# for filepath in path.iterdir():
#     print(filepath.name)

