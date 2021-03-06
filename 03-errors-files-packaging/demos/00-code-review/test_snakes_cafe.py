import snakes_cafe as cafe
# import pytest


# def example_raised_error():
#     """Doc String"""
#     with pytest.raises(TypeError):
#         example_expects_int('invalid string')


def test_valid_add_to_cart():
    """
    Tests that items not in the menu can't be added
    """
    cafe.cart = {}
    assert cafe.add_to_cart('thing') is False


def test_add_to_cart():
    """
    Tests that items that are in the menu but not in the cart are added to the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts')
    assert 'pop-tarts' in cafe.cart


def test_multi_add_to_cart():
    """
    Tests that items that are in the menu and in the cart are incremented in the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts')
    cafe.add_to_cart('pop-tarts')
    assert cafe.cart['pop-tarts'] == 2


def test_valid_remove_cart():
    """
    Tests that if item is not in cart, it is not removed
    """
    cafe.cart = {}
    assert cafe.remove_cart('pop-tarts') is False


def test_multi_remove_cart():
    """
    Tests that if more than one of an item is in the cart, it is decremented by one in the cart
    """
    cafe.cart = {'pop-tarts': 2}
    cafe.remove_cart('pop-tarts')
    assert cafe.cart['pop-tarts'] == 1


def test_remove_cart():
    """
    Tests that if one of an item is in the cart, it is completely removed
    """
    cafe.cart = {'pop-tarts': 1}
    cafe.remove_cart('pop-tarts')
    assert 'pop-tarts' not in cafe.cart


def test_print_menu():
    """
    validates that menu is a dictionary
    validates that expected menu is printed
    """
    assert (isinstance(cafe.menu_categories, dict) is True) and\
           (isinstance(cafe.print_menu(cafe.menu_categories), str))


def test_print_cart():
    """
    validates that cart is a dictionary
    validates that expected cart is printed
    """
    assert (isinstance(cafe.cart, dict) is True) and\
           (isinstance(cafe.print_cart(cafe.cart), str))
