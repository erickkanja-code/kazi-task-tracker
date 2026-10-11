import quicktask

def setup_function():
    quicktask.tasks.clear()
    quicktask.next_task_id = 1
    
def test_add_task():
    # Arrange
    setup_function()
    
    # Act
    quicktask.add_task("Finish assignment")
    
    # Assert
    assert len(quicktask.tasks) == 1
    assert quicktask.tasks[0]["title"] == "Finish assignment"
    assert quicktask.tasks[0]["id"] == 1
    assert quicktask.tasks[0]["status"] == "pending"
    
def test_add_empty_task():
    setup_function()
    
    quicktask.add_task(" ")
    
    assert len(quicktask.tasks) == 0
    assert quicktask.next_task_id == 1

def test_delete_task():
    quicktask.add_task("Clean clothes")
    
    quicktask.delete_task(1)
    
    assert len(quicktask.tasks) == 0
    
    
