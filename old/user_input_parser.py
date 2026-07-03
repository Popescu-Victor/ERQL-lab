# There will be a entry widget in the gui where users will be able to write their custom scripts for doing creating these reports. For the time being, the variable "input" is a placeholder for entry.get().

input = "cv --> yuu"
clean = input.split(" --> ")



def code_deconstruct():
    if clean[0] == "hw":
        hw_code()
    if clean[0] == "cv":
        cv_code()
    else:
        print('Error')

def cv_code():
    print('Return CV fun')
    if clean[1]  not in ('graph', 'analyse', 'graph',):
        print('Error: "' + clean[1] + '" is not a valid input')
    if clean[1] == 'convert':
        cv_convert()
    if clean[1] == 'graph':
        cv_graph()
    if clean [1] == 'analyse':
        cv_analyse()

def cv_analyse(): 
    if len(clean) == 2:
     if clean[1] == 'analyse':
        print('RETURN cv analysis')
    else:
        print('Displaying analysis for ' + clean[2])
def cv_convert():
    if clean[1] == 'convert':
        print('RETURN converted text')


def cv_graph():
    if clean[1] == 'graph':
        print('RETURN cv plot')


def hw_code():
    print("Return HW fun")
    if clean[1]  not in ('graph', 'analyse', 'graph'):
        print('Error: "' + clean[1] + '" is not a valid input')
    else:
        print('init')

        
code_deconstruct()

