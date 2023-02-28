from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):

    def test_can_get_todo_list(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_additem_page(self):
        

    def test_get_edit_item_page(self): 


    def test_can_add_item(self):


    def test_can_delete_item(self):


    def test_can_toggle_item(self):
        

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test ToDo Item')
        response=self.client.post(f'/edit/{item.id}', {'name' : 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=items.id)
        self.assertEqual(updated_item.name, 'Updated Name')