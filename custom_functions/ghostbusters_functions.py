#!/usr/bin/env python3
"""Ghostbusters Lab | Step 4"""

def report_ghost_sighting(ghost_name, location="New York City"):
    """Prints details about the ghost sighting with a default location."""
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")  # Valid call
report_ghost_sighting("Stay Puft")  # Valid call, 'location' defaults to "New York City"

#!/usr/bin/env python3
"""Ghostbusters Lab | Step 5"""

def calculate_catch_rate(ghost_name):
    """Returns a catch rate based on the ghost's name."""
    return len(ghost_name) * 10
    # len() is a built-in function that counts the number of 'pieces' to an object

# Call the function and store the result
rate = calculate_catch_rate("Slimer")

# Print the result
print("The catch rate for this ghost is:", rate)

 #!/usr/bin/env python3
 """Fixed Function"""

 # Define the function first
 def report_ghost_sighting(ghost_name): # must define the argument
     print(f"{ghost_name} has been sighted! Who you gonna call?")  # Fixed placement issue

 # Then call the function
 report_ghost_sighting("Slimer")  # Function call now works

