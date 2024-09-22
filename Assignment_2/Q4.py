# How memory is managed in python?

# Ans. Python manages memory using a private heap and automatic garbage collection. It uses reference counting 
# to track object usage, and when an object is no longer referenced, it is deallocated. For objects in circular 
# references, Python's garbage collector cleans them up to free memory. This allows Python to handle most memory
# management tasks automatically.