"""Unit tests for tasks.py.

These tests only use small lists created inside the tests themselves.
They never touch your real tasks.json file.
"""

import unittest

import tasks


class TestGenerateId(unittest.TestCase):

    def test_empty_list_gives_id_1(self):
        # With no tasks, the first ID should be 1.
        self.assertEqual(tasks.generate_id([]), 1)

    def test_next_id_is_biggest_plus_one(self):
        # IDs 1 and 2 exist, so the next one should be 3.
        existing = [
            {"id": 1, "title": "A", "done": False},
            {"id": 2, "title": "B", "done": False},
        ]
        self.assertEqual(tasks.generate_id(existing), 3)

    def test_id_is_not_reused_after_gap(self):
        # IDs 1 and 5 exist (2-4 were deleted). Next must be 6, not 2.
        existing = [
            {"id": 1, "title": "A", "done": False},
            {"id": 5, "title": "B", "done": False},
        ]
        self.assertEqual(tasks.generate_id(existing), 6)


class TestAddTask(unittest.TestCase):

    def test_add_task_returns_new_task(self):
        # The returned task should have the right title, id and done=False.
        task_list = []
        new_task = tasks.add_task(task_list, "Buy milk")
        self.assertEqual(new_task["title"], "Buy milk")
        self.assertEqual(new_task["id"], 1)
        self.assertFalse(new_task["done"])

    def test_add_task_adds_to_list(self):
        # The list itself should grow by one.
        task_list = []
        tasks.add_task(task_list, "Buy milk")
        self.assertEqual(len(task_list), 1)

    def test_add_task_gives_increasing_ids(self):
        # Adding two tasks should give IDs 1 and 2.
        task_list = []
        first = tasks.add_task(task_list, "One")
        second = tasks.add_task(task_list, "Two")
        self.assertEqual(first["id"], 1)
        self.assertEqual(second["id"], 2)

    def test_add_task_strips_spaces(self):
        # Extra spaces around the title should be removed.
        task_list = []
        new_task = tasks.add_task(task_list, "   Buy milk   ")
        self.assertEqual(new_task["title"], "Buy milk")

    def test_add_empty_title_raises_error(self):
        # An empty title is not allowed: expect a ValueError.
        with self.assertRaises(ValueError):
            tasks.add_task([], "")

    def test_add_spaces_only_title_raises_error(self):
        # A title of only spaces counts as empty too.
        with self.assertRaises(ValueError):
            tasks.add_task([], "     ")

    def test_failed_add_does_not_change_list(self):
        # If adding fails, the list must stay empty.
        task_list = []
        with self.assertRaises(ValueError):
            tasks.add_task(task_list, "")
        self.assertEqual(task_list, [])


class TestFindTask(unittest.TestCase):

    def setUp(self):
        # Runs before every test in this class: fresh sample data.
        self.task_list = [
            {"id": 1, "title": "A", "done": False},
            {"id": 2, "title": "B", "done": False},
        ]

    def test_find_existing_task(self):
        found = tasks.find_task(self.task_list, 2)
        self.assertEqual(found["title"], "B")

    def test_find_missing_task_returns_none(self):
        self.assertIsNone(tasks.find_task(self.task_list, 99))

    def test_find_in_empty_list_returns_none(self):
        self.assertIsNone(tasks.find_task([], 1))


class TestCompleteTask(unittest.TestCase):

    def setUp(self):
        self.task_list = [
            {"id": 1, "title": "A", "done": False},
            {"id": 2, "title": "B", "done": False},
        ]

    def test_complete_existing_task(self):
        # Should return True and mark the task as done.
        result = tasks.complete_task(self.task_list, 1)
        self.assertTrue(result)
        self.assertTrue(self.task_list[0]["done"])

    def test_complete_only_changes_that_task(self):
        # Task 2 must stay not done.
        tasks.complete_task(self.task_list, 1)
        self.assertFalse(self.task_list[1]["done"])

    def test_complete_missing_task_returns_false(self):
        # Should return False and change nothing.
        result = tasks.complete_task(self.task_list, 99)
        self.assertFalse(result)
        self.assertFalse(self.task_list[0]["done"])
        self.assertFalse(self.task_list[1]["done"])


class TestDeleteTask(unittest.TestCase):

    def setUp(self):
        self.task_list = [
            {"id": 1, "title": "A", "done": False},
            {"id": 2, "title": "B", "done": False},
        ]

    def test_delete_existing_task(self):
        # Should return True and remove it from the list.
        result = tasks.delete_task(self.task_list, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.task_list), 1)
        self.assertIsNone(tasks.find_task(self.task_list, 1))

    def test_delete_keeps_other_tasks(self):
        tasks.delete_task(self.task_list, 1)
        self.assertEqual(self.task_list[0]["id"], 2)

    def test_delete_missing_task_returns_false(self):
        # Should return False and leave the list unchanged.
        result = tasks.delete_task(self.task_list, 99)
        self.assertFalse(result)
        self.assertEqual(len(self.task_list), 2)

    def test_delete_from_empty_list_returns_false(self):
        self.assertFalse(tasks.delete_task([], 1))


class TestGetAllTasks(unittest.TestCase):

    def test_get_all_returns_same_tasks(self):
        task_list = [{"id": 1, "title": "A", "done": False}]
        self.assertEqual(tasks.get_all_tasks(task_list), task_list)

    def test_get_all_on_empty_list(self):
        self.assertEqual(tasks.get_all_tasks([]), [])

    def test_get_all_returns_a_copy(self):
        # Changing the returned list must not change the original list.
        task_list = [{"id": 1, "title": "A", "done": False}]
        copy = tasks.get_all_tasks(task_list)
        copy.append({"id": 2, "title": "B", "done": False})
        self.assertEqual(len(task_list), 1)


if __name__ == "__main__":
    unittest.main()
