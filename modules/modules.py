# ways to import:

# [1] import module_name
# [2] import method_name from module_name
# [3] import method_name from module_name as name_specific_for_this_module_alone

# # importance of __main__:

# the current_file will always be __main__ and the  imported module will always be filename
# sometimes the functions of the imported module may work in the mainfile, so it is better to denote in the imported module, that execute that only if
# __name__ == "__main__" or else  the code in the current file should be executed.