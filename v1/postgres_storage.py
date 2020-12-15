import dataset
import random
random.seed()

db = dataset.connect("postgresql://todouser1:todopassword1@drdelozier-1880.postgres.pythonanywhere-services.com:11880/tododb")
# db = dataset.connect("sqlite:///:memory:")

def get_items():
    items = list(db['todo'].all())
    results = [(item['id'],item['task'],item['status']) for item in items]
    return results

def get_item(id):
    items = list(db['todo'].find(id=id))
    if len(items) == 0:
        return None
    results = [(item['id'],item['task'],item['status']) for item in items]
    return results[0]

def create_item(task, status):
    id = db['todo'].insert(dict(task=task, status=status))
    return id

def update_status(id, value):
    db['todo'].update(dict(id=id, status=value), ['id'])

def update_item(id, updated_task):
    db['todo'].update(dict(id=id, task=updated_task), ['id'])

def delete_item(id):
    db['todo'].delete(id=id)

def _random_text():
    random_text = str(random.randint(10000,20000))
    return random_text

def test_get_items():
    print("testing get_items")
    results = get_items()
    assert type(results) is list
    assert len(results) > 0
    print(results)
    for item in results:
        assert type(item) is tuple
    id, task, status = results[0]
    assert type(id) is int
    assert type(task) is str
    assert type(status) is int
    assert status in [0,1]

def test_get_item():
    print("testing get_item(id)")
    results = get_items()
    assert len(results) > 0
    id, task, status = results[0]
    result = get_item(id)
    assert type(result) is tuple
    id2, task2, status2 = result
    assert id2 == id
    assert task2 == task
    assert status2 == status

def test_create_item():
    print("testing create_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    returned_id, task, status = get_item(id)
    assert returned_id == id
    assert task == example_task
    assert status == 0

def test_update_status():
    print("testing update_status()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    _, _, status = get_item(id)
    assert status == 0
    update_status(id, 1)
    _, _, status = get_item(id)
    assert status == 1
    update_status(id, 0)
    _, _, status = get_item(id)
    assert status == 0

def test_update_item():
    print("testing update_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    updated_task = example_task + " updated..."
    update_item(id, updated_task)
    _, task, status = get_item(id)
    assert task == updated_task

def test_delete_item():
    print("testing delete_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    returned_id, _, _ = get_item(id)
    assert returned_id == id
    delete_item(id)
    assert get_item(id) == None

if __name__ == "__main__":
    test_get_items()
    test_get_item()
    test_create_item()
    test_update_status()
    test_update_item()
    test_delete_item()
    print("done.")