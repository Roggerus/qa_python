import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

class TestBooksCollector:

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('Властелин колец')
        assert 'Властелин колец' in collector.get_books_genre()

    def test_add_new_book_empty_name_does_not_add_book(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_long_name_does_not_add_book(self, collector):
        collector.add_new_book('A' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_genre(self, collector):
        collector.add_new_book('Левиафан')
        collector.set_book_genre('Левиафан', 'Фантастика')
        assert collector.get_book_genre('Левиафан') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Букварь')
        collector.set_book_genre('Букварь', 'Фэнтези')
        assert collector.get_book_genre('Букварь') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Левиафан')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Левиафан', 'Фантастика')
        books = collector.get_books_with_specific_genre("Фантастика")
        assert 'Властелин колец' in books
        assert 'Левиафан' in books
        assert len(books) == 2

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Незнайка на луне')
        collector.add_new_book('Оно')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert "Незнайка на луне" in children_books
        assert "Оно" not in children_books

    def test_add_book_in_favorites_books_added(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.favorites

    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        collector.add_new_book('Левиафан')
        collector.add_book_in_favorites('Левиафан')
        collector.add_book_in_favorites('Левиафан')
        assert collector.favorites.count('Левиафан') == 1

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.favorites

    def test_delete_non_existent_book_from_favorites_the_list_not_change(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Оно')
        assert 'Гарри Поттер' in collector.favorites
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_return_correct_list(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Гарри Поттер')
        favorites = collector.favorites
        assert 'Властелин колец' in favorites
        assert 'Гарри Поттер' in favorites
        assert len(favorites) == 2

