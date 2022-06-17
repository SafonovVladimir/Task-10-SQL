from unittest import TestCase, main
from itertools import islice
from tests import *


class TestCollection(TestCase):
    """Test queries student"""

    def test_get_student(self):
        """Test get_student"""
        self.assertEqual(get_student('200'), [(200, 'Shvets Yurii', 'JJ-36')])

    def test_get_student_id_list(self):
        """Test get_student_id_list"""
        id_list = get_student_id_list()
        for id in islice(id_list, 1, 2):
            self.assertEqual(id, 2)

    def test_get_student_courses(self):
        """Test get_student_courses"""
        self.assertEqual(get_student_courses('200'), [('Marketing', 'description Marketing')])

    def test_get_students_subjects_list(self):
        """Test get_students_subjects_list"""
        students = get_students_subjects_list()
        for student in islice(students, 1, 2):
            self.assertEqual(student, ('Pavlo', 'Shevchenko', 'Literature'))

    def test_get_all_students_with_group_name(self):
        """Test get_all_students_with_group_name"""
        students = get_all_students_with_group_name()
        for student in islice(students, 1, 2):
            self.assertEqual(student, (182, 'Bondarenko Dmytro', 'KE-38'))


if __name__ == '__main__':
    main()
