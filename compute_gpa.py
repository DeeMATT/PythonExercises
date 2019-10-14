"""A function that computes a student’s GPA with a point value
system that can be customized as an optional parameter
"""
points_def = {'A+': 5.0, 'A': 4.5, 'B+': 4.0, 'B': 3.5,
              'C+': 3.0, 'C': 2.5, 'D+': 2.0, 'D': 1.5,
              'E': 1.0, 'F+': 0.5, 'F': 0.0}


def compute_gpa(grades, points=points_def):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses

dele = ['A+', 'B', 'B+', 'F']
print(compute_gpa(dele))