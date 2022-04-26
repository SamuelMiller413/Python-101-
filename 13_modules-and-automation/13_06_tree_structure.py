import pathlib

# Write a script that walks through a nested folder structure
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

user = pathlib.Path("/Users")
admin = pathlib.Path("/Users/admin")
desktop = pathlib.Path("/Users/admin/Desktop")
screenshots = pathlib.Path("/Users/admin/Desktop/screenshots")
user_print = 'Users contents: '
admin_print = 'admin contents: '
desktop_print = 'Desktop contents'
screenshots_print = 'screenshot contents: '

for filepath in user.iterdir():
    user_print += filepath.name + ", "
for filepath in admin.iterdir():
    admin_print += filepath.name + ", "
for filepath in desktop.iterdir():
    desktop_print += filepath.name + ", "
for filepath in screenshots.iterdir():
    screenshots_print += filepath.name + ", "
    
print(user_print)
print('')
print(admin_print)
print('')
print(desktop_print)
print('')
print(screenshots_print)








