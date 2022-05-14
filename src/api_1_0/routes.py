from src.api_1_0 import api_v1
from src.api_1_0.resources.course import CoursesList, CourseName
from src.api_1_0.resources.group import GroupName, GroupsList
from src.api_1_0.resources.student import StudentName, StudentsList

api_v1.add_resource(GroupsList, '/groups/')
api_v1.add_resource(GroupName, '/groups/<group_id>')
api_v1.add_resource(CoursesList, '/courses/')
api_v1.add_resource(CourseName, '/courses/<course_id>')
api_v1.add_resource(StudentsList, '/students/')
api_v1.add_resource(StudentName, '/students/<student_id>')
