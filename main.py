import random
import array
import json

##############################################
def read_parameters_file():
    # Opening JSON file
    parameters_file = open('config.json')
    # json object as a dictionary
    metadata = json.load(parameters_file)
    # Closing file
    parameters_file.close()
    return metadata

##############################################
def generator():
    """
    password generated with at least one character from each category
    """
    # read parameters file and receive all params as dictionary
    params = read_parameters_file()

    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = params['max_length']

    # declare arrays of the character that we need in out password

    DIGITS = params['digits']
    LOWERCASE_CHARACTERS = params['lowercase_chars']
    UPPERCASE_CHARACTERS = params['uppercase_chars']
    SYMBOLS = params['available_symbols']
    
    # combines all the character arrays above to form one array
    COMBINED_LIST = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS + DIGITS
    
    # randomly select at least one character from each character set above
    rand_upper = random.choice(UPPERCASE_CHARACTERS)
    rand_lower = random.choice(LOWERCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    rand_digit = random.choice(DIGITS)
    
    # combine the character randomly selected above
    # at this step, the password contains only 4 characters but
    # define a n-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
    # now we have at least one character from each characters list, we generate the rest of
    # the password length by selecting randomly from the combined list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass += random.choice(COMBINED_LIST)
    
        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    
    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for item in temp_pass_list:
            password += item
            
    # return password
    return password

##############################################
if __name__ == "__main__":
    random_password = generator()
    print(random_password)
