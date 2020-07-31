from python_algo.palindrome import check

def test_false_case():
    assert check('race a car') == False

def test_true_case():
    assert check('A man, a plan, a canal: Panama') == True

def test_long_palindrome():
    assert check('Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man—a prisoner up to new era.') == True