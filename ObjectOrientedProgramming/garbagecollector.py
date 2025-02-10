# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

# #########################################################################################################
#
# import time    #Run the below programs with gc enabled...dont disable it
# class Test:
#     def __init__(self):
#         print("Object initialization")
#     def __del__(self):
#         print("Fulfilling requirements")
# t=Test()
# t=None  # Here only the object t will be deleted by gc since it is None
# time.sleep(10)
# print("End of program")

# #########################################################################################################
#
# import time
# class Test:
#     def __init__(self):
#         print("Object initialization")
#     def __del__(self):
#         print("Fulfilling requirements")
# t=Test()
# time.sleep(10)
# print("End of program") # after completing this line gc will delete the t since it was being used before End of program

#########################################################################################################

# import time
# class Test:
#     def __init__(self):
#         print("Object initialization")
#     def __del__(self):
#         print("Fulfilling requirements")
# t=Test()
# del t  # Here only the object t will be deleted by gc since it is None
# time.sleep(10)
# print("End of program")


#########################################################################################################

# import time
# class Test:
#     def __init__(self):
#         print("Object initialization")
#     def __del__(self):
#         print("Fulfilling requirements")
# t1=Test()
# t2 = t1
# t3 = t2
# t4 = t3
# del t1
# time.sleep(10)
# print("Object not deleted after deleting the t1")
# del t2
# del t3
# print("Still object not deleted")
# del t4
# time.sleep(10)
# print("End of program")


#########################################################################################################
import time
class Test:
    def __init__(self):
        print("Object initialization")
    def __del__(self):
        print("Fulfilling requirements")
list = [Test(), Test(), Test()]
time.sleep(10)
list = None
time.sleep(10)
print("End of application")


