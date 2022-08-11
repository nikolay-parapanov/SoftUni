from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student('John', {
            'web programming': ['note1', 'note2'],
            'database basics': ['note3', 'note4']
        })

    def test_sudent_init(self):
        name = "test name"
        student = Student(name)
        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        name = "test name"
        courses = {
            'web programming': ['note1', 'note2'],
            'database basics': ['note3', 'note4']
        }
        student = Student(name, courses)
        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_add_notes_to_the_course(self):
        course = 'database basics'
        result = self.student.enroll(course, ['new note'])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(['note3', 'note4', 'new note'], self.student.courses[course])

    def test_enroll_with_new_course_add_notes_to_it(self):
        course = 'new course'
        notes = ['nc-1', 'nc-2']

        result = self.student.enroll(course, notes, "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_with_new_course_and_empty_string_add_notes_to_it(self):
        course = 'new course'
        notes = ['nc-1', 'nc-2']

        result = self.student.enroll(course, notes, "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_without_notes(self):
        course = 'new course'

        result = self.student.enroll(course, ['notes'], "N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_to_existing_course(self):
        course = 'database basics'
        result = self.student.add_notes(course, 'new_note 3')

        self.assertEqual('Notes have been updated', result)

        final_notes = ['note3', 'note4', 'new_note 3']
        self.assertEqual(final_notes, self.student.courses[course])

    def test_add_notes_raises_when_course_not_existing(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Invalid course", 'random note')
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course_remove_course_form_existing_courses(self):
        course = 'database basics'
        result = self.student.leave_course(course)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course not in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_invalid_existing_course(self):
        course = 'invalid course'
        with self.assertRaises(Exception) as context:
            self.student.leave_course(course)
        self.assertEqual('Cannot remove course. Course not found.', str(context.exception))


if __name__ == '__main__':
    main()
