# Write the necessary code to display the total population count for the next 3 years

# In the country we want to investigate: 
# Population 380123456
# Birth every 6 seconds =======>   
# Dies every 12 seconds
# Immigrates every 40 seconds
# Seconds per year 31536000

pop = 380123456
spy = 31536000
bpy = spy / 6
dpy = spy / 12 #(-)
ipy = spy / 40
pby = bpy - dpy + ipy
year_1 = pop + pby
year_2 = pop + pby * 2
year_3 = pop + pby * 3

print("Population Year 1 = ", int(year_1))
print("Population Year 2 = ", int(year_2))
print("Population Year 3 = ", int(year_3))