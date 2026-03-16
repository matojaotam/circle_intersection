def analyze_password(
        password,
        min_length=8,
        require_digit=True,
        require_upper=True,
        require_symbol=False,
        banned_words=None
):
    if banned_words is None:
        banned_words = ['heslo','1234']

    symbols = "!@#$%^&*()-_=+[]{};:,.?"

    total_rules = 0
    passed_rules = 0
    missing_rules = []

    total_rules += 1
    if len(password) >= min_length:
        passed_rules += 1
        if any(c.isdigit() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("digit")

    if require_upper:
        total_rules += 1
        if any(c.isupper() for c in password):
            passed_rules += 1
        else:
            missing_rules.append("upper")

    if require_symbol:
        total_rules += 1
        if any(c in symbols for c in password):
            passed_rules += 1
        else:
            missing_rules.append("symbol")

    total_rules += 1
    lower_pass = password.lower()
    if any(word.lower() in lower_pass for word in banned_words):
        missing_rules.append("banned_word")
    else:
        passed_rules += 1

    score_percent = int((passed_rules / total_rules) * 100)
    is_strong = len(missing_rules) == 0

    return is_strong, score_percent, missing_rules

print(analyze_password("Test1234",
                       8,
                       True,
                       True,
                       True,
                       ['admin', 'test']))

print(analyze_password("Test1234",
                       8,
                       require_symbol=True))

print(analyze_password("Test1234",
                       require_symbol=False))

print(analyze_password("Admin123A",
                       banned_words=["admin", "root", "user"]))



