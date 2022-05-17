from unittest import TestCase, main
from itertools import islice
from tests import *


class TestCollection(TestCase):
    """Test queries courses"""

    def test_get_course_info(self):
        """Test get_course_info"""
        courses = get_course_info('Chemistry')
        for course in islice(courses, 1, 2):
            self.assertEqual(course, (39, 'Gavrilyuk Artem', 'YY-54'))


    def test_get_courses(self):
        """Test get_courses"""
        courses = get_courses()
        for course in islice(courses, 1, 2):
            self.assertEqual(course, ('English', 'description English'))

    def test_get_course_id_by_name(self):
        """Test get_course_id_by_name"""
        self.assertEqual(get_course_id_by_name('English'), 4)


if __name__ == '__main__':
    main()
