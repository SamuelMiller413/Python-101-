# Import pathlib                    √
import pathlib

# Find the path to my Desktop       √
path_desktop = pathlib.Path("/Users/admin/Desktop")
str(path_desktop)

#  List all the files on there      √   <--no longer relevant but kept in this code for the purpose of documenting the process
# for filepath in path_desktop.iterdir():
#     print(filepath.name)

# Create a new folder               √
new_path = pathlib.Path('/Users/admin/Desktop/screenshots')
new_path.mkdir(exist_ok=True)

# Filter for screenshots only       √
for filepath in path_desktop.iterdir():
    if filepath.suffix == '.png':  # filter for screenshots only    √
        new_filepath = new_path.joinpath(filepath.name)     # Create a new path for each file   √
        filepath.replace(new_filepath)      # Move the screenshots there    √   


# oldpath.replace(newpath)










# pathlib.Path().cwd()
# path = pathlib.Path().cwd()
# str(path)

# for filepath in path.iterdir():
#     print(filepath.name)

# pathlib.Path().cwd().name

# pathlib.Path("/Users/admin/Documents/CodingNomads/REsources/Python 101")






