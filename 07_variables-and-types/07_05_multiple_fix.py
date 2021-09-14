# Fix the variable assignment shown below.
# Can you see why using the multiple variable assignment can be tricky?
# Declared like this, it's easy to mix which is which.

dreams, profession = "flying", "programming"
# Besides that they're conceptually distinct? Like the last lab exercise?
# I don't see why they're easy to mix up, 
# unless one's 'dream' is 'programming
# or one's profession is 'flying'
#but here goes:

dreams = "flying"
profession = "programming"

print(dreams + profession)