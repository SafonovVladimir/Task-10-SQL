from unittest import TestCase, main
from itertools import islice
from tests import *


class TestCollection(TestCase):
    """Test queries groups"""

    def test_get_groups_name(self):
        """Test get_groups_name"""
        groups = get_groups_name()
        for group in islice(groups, 1, 2):
            self.assertEqual(group[0], 'CA-76')

    def test_get_group_inf(self):
        """Test get_group_inf"""
        groups = get_group_inf('CA-76')
        for group in islice(groups, 1, 2):
            self.assertEqual(group, (2, 'Ishchenko Dmytro', 'CA-76'))

    def test_get_groups_with_student_count(self):
        """Test get_groups_with_student_count"""
        groups = get_groups_with_student_count(20)
        for group in islice(groups, 1, 2):
            self.assertEqual(group[0], 'YY-54')

    def test_get_group_id_by_name(self):
        """Test get_group_id_by_name"""
        self.assertEqual(get_group_id_by_name('CA-76'), 1)


if __name__ == '__main__':
    main()
