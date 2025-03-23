def get_user_role(token: dict):
    return token.get('role', 'employee')