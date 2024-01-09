class RepeatedElementError(ValueError):
    """Raised when a repeated element is found in the list
    Attributes:
        item -- the repeated element
        message -- explanation of the error
    """

    def __init__(self, item, message =  'Adding duplicated values is not allowed => '):
        self.item = item
        self.message = 'RepeatedElementError:' + message + '[' + item + ']' + '.'
        super().__init__(self.message)

def add_once(my_list, my_elem):
        '''
        Adds an element to a list, providing that it is not already in the list.
        
        my_list(list): a collection of elements
        my_elem: the element to be added to the list
        throws RepeatedElementError if the element is already in the list
        '''
        if my_elem in my_list:
            raise RepeatedElementError(my_elem)
        else:
            my_list.append(my_elem)

def request_number():
    '''
    Request a user input until the 0 value is provided. 
    When this happens, the elements provided by the user will be displayed in the same order right before the program end.
    
    '''
    user_input = input("Please enter a number: ")
    return user_input
user_input = request_number()
user_list = []
while user_input != '0':
    user_input = request_number()
    try:
            
        RepeatedElementError.add_once(user_list, user_input)
            
    except RepeatedElementError:
        print(RepeatedElementError.RepeatedElementError.message)

print("The numbers you entered are: " + str(user_list))