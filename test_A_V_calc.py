'''
TPRG 2131 Fall 2023 Assignment 1
Sept, 2023
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''


import A_V_calc  # Import the module containing the functions to be tested

def test_calculate_area_circle():
    # Test cases for calculate_area_circle function
    assert A_V_calc.calculate_area_circle(1) == 3.141592653589793 
    assert A_V_calc.calculate_area_circle(2) == 12.566370614359172
    assert A_V_calc.calculate_area_circle(3) == 28.274333882308138
    
def test_calculate_volume_sphere():
    # Test cases for calculate_area_circle function
    assert A_V_calc.calculate_volume_sphere(1) == 4.1887902047863905  # Using math.pi
    assert A_V_calc.calculate_volume_sphere(2) == 33.510321638291124
    assert A_V_calc.calculate_volume_sphere(3) == 113.09733552923254
    
def test_calculate_area_rectangle():
    # Test cases for calculate_area_circle function
    assert A_V_calc.calculate_area_rectangle(1,2) == 2.0  
    assert A_V_calc.calculate_area_rectangle(3,4) == 12.0
    assert A_V_calc.calculate_area_rectangle(5, 6) == 30.0
    
def test_calculate_area_square():
    # Test cases for calculate_area_circle function
    assert A_V_calc.calculate_area_square(1) == 1.0 
    assert A_V_calc.calculate_area_square(2) == 4.0
    assert A_V_calc.calculate_area_square(3) == 9.0
    
def test_calculate_volume_cylinder():
    # Test cases for calculate_area_circle function
    assert A_V_calc.calculate_volume_cylinder(1,2) == 6.283185307179586  # Using math.pi
    assert A_V_calc.calculate_volume_cylinder(3,4) == 113.09733552923255
    assert A_V_calc.calculate_volume_cylinder(5, 6) == 471.23889803846896

    
