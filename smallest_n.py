# Importing two modules
import m_lists
from two_smallest import find_two_smallest

# Defining and Opening the file
file_1 = "result.txt"
file = open(file_1, "w")

# Writing the smallest two numbers in lists
file.write(str(find_two_smallest(m_lists.l_1))+"\n")
file.write(str(find_two_smallest(m_lists.l_2))+"\n")
file.write(str(find_two_smallest(m_lists.l_3))+"\n")
file.write(str(find_two_smallest(m_lists.l_4))+"\n")
file.close()