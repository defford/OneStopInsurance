import datetime

def sumPrevClaims(prevClaims):
    sum = 0
    
    for claim in prevClaims:
        sum += claim
    
    return sum


def PPrint(screenWidth, *args):
    """
    Stands for 'Positional Print'
    Positions multiple text elements along a line.

    *args allows functions to take arguments as they're given: 
        Earch arg is a tuple of variable length. Each tuple contains:
            - content (str): The string to print.
            - position (int or str): The position along the line if an int, or one of 'left', 'right', 'center'.
            - align (str, optional): If position is an int, align can be 'left' or 'right'. Defaults to 'left'.

    Returns the elements along a line specifically positioned.
    """

    line = [' '] * screenWidth  # Creates a list of spaces to build the line

    for content, position, *optional in args:
        if content: 
            align = optional[0] if optional else 'left'
            if isinstance(position, int): 
                start = position if align == 'left' else position - len(content)
            elif position == 'left':
                start = 0
            elif position == 'right':
                start = screenWidth - len(content)
            elif position == 'center':
                start = (screenWidth - len(content)) // 2

            # Insert the content into the line list
            for i, char in enumerate(content):
                if 0 <= start + i < screenWidth:
                    line[start + i] = char
        else:
            print() 


    # Convert list back to string and print
    print(''.join(line))



def AddMonths(date, interval):
    day = date.day
    month = date.month
    year = date.year

    # Calculate the new month and year
    month += interval

    if month > 12:
        year += 1

    newDate = datetime.datetime(year, month, day)
    
    return newDate