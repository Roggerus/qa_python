import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('book_name', [
        'Властелин колец',
        'Гарри Поттер',
        'Левиафан',
        'Незнайка на луне',
        'А',
        'А' * 40
    ])
    def test_add_new_book_valid_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', [
        '',
        'A' * 41
    ])
    def test_add_new_book_empty_name_does_not_add_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', [
        'Фантастика',
        'Ужасы',
        'Детективы',
        'Мультфильмы',
        'Комедии'])
    def test_set_book_genre_valid_genre(self, collector, genre):
        book = 'Левиафан'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize("genre", [
        'Фэнтези',
        'Роман',
        'Детектив',
        ''
    ])
    def test_set_book_genre_invalid_genre(self, collector, genre):
        book = 'Букварь'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_positive(self, collector):
        book = 'Левиафан'
        genre = 'Фантастика'
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Левиафан', 'Фантастика'),
        ('Оно', 'Ужасы'),
    ])
    def test_get_books_genre_positive(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Левиафан', 'Фантастика'),
        ('Оно', 'Ужасы'),
    ])
    def test_get_books_with_specific_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert book_name in books_with_genre

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Незнайка на луне')
        collector.add_new_book('Оно')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert "Незнайка на луне" in children_books
        assert "Оно" not in children_books

    @pytest.mark.parametrize('book_name', [
        'Властелин колец',
        'Гарри Поттер',
        'Левиафан',
        'Незнайка на луне'])
    def test_add_book_in_favorites_books_added(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        book_name = 'Левиафан'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.favorites.count(book_name) == 1


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

