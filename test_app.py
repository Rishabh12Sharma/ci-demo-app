from app import Calculator, TaskManager

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 3) == 12

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_task_manager_add():
    manager = TaskManager("test_tasks.json")
    task = manager.add_task("Test", "Testing CI")
    assert task["title"] == "Test"
