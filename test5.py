def is_valid_password(password):
    # Check length of password
    if len(password) < 8:
        return False
    
    # Check first character is alphabetical
    if not password[0].isalpha():
        return False
    
    # Count alphabetical and numerical characters
    alpha_count = 0
    num_count = 0
    for char in password:
        if char.isalpha():
            alpha_count += 1
        elif char.isnumeric():
            num_count += 1
    
    # Check for minimum alphabetical and numerical characters
    if alpha_count < 4 or num_count < 3:
        return False
    
    # Password meets all criteria
    return True