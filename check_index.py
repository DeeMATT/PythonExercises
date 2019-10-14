def limit_number(num, range_low, range_high):

	for i in range(range_low, range_high+1):
            if num == i:
                return num
            if num < range_low:
                return range_low
            elif num > range_high:
                return range_high

print(limit_number(5, 1, 10))
print(limit_number(-3, 1, 10))
print(limit_number(14, 1, 10))
print(limit_number(4.6, 1, 10))
print(limit_number(-100, -73, -70))
print(limit_number(2, -73, -70))

"""
Test.assert_equals(limit_number(-71.5, -73, -70), -71.5)
Test.assert_equals(limit_number(7, 8, 8.1), 8)
Test.assert_equals(limit_number(9, 8, 8.1), 8.1)
Test.assert_equals(limit_number(8.05, 8, 8.1), 8.05)
Test.assert_equals(limit_number(16, 16, 16), 16)
Test.assert_equals(limit_number(-1, 16, 16), 16)
Test.assert_equals(limit_number(800, 16, 16), 16)
"""