from name_function import get_formatted_name 

def test_first_last_name():
    """Do names like 'Janis Joplin work'"""
    formatted_name = get_formatted_name('Janis','Joplin','Jane')
    assert formatted_name == 'Janis Joplin Jane'

#To Test - python -m pytest -q