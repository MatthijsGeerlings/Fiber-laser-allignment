''''This is some code that is implemented into the fiber_window file to ensure the multiply array 
is only imported once'''
try:
    value_to_check_whether_the_multiply_array_exists +\
        value_to_check_whether_the_multiply_array_exists 
except NameError:
    print('''Multiply array is created and a vlue is assigned to 
          value_to_check_whether_the_multiply_array_exists ''')
    # create multiply array
    #multiply_array = self.experiment.import_or_create_and_save_multiply_array\
     #   ('width camere (pixels)','height camera (pixels)')
    value_to_check_whether_the_multiply_array_exists = 1
else:
    pass
finally:
    pass
