"""
Magic Methods Exercises

This file contains exercises to practice implementing Python's magic methods.
Complete each exercise by implementing the required magic methods.

Run this file to test your implementations:
    python 04_magic_methods.py
"""


# Exercise 1: String Representation
class Book:
    """
    A class representing a book.
    
    TODO: Implement the following magic methods:
    - __init__(self, title, author, pages)
    - __str__(self) - should return "Title by Author"
    - __repr__(self) - should return "Book('Title', 'Author', pages)"
    """
    
    def __init__(self, title, author, pages):
        # TODO: Initialize the book with title, author, and pages
        pass
    
    def __str__(self):
        # TODO: Return a user-friendly string representation
        pass
    
    def __repr__(self):
        # TODO: Return a developer-friendly string representation
        pass


# Exercise 2: Comparison Operators
class Temperature:
    """
    A class representing temperature in Celsius.
    
    TODO: Implement the following magic methods:
    - __init__(self, celsius)
    - __eq__(self, other) - equality comparison
    - __lt__(self, other) - less than comparison
    - __le__(self, other) - less than or equal comparison
    - __gt__(self, other) - greater than comparison
    - __ge__(self, other) - greater than or equal comparison
    - __str__(self) - return "X°C"
    """
    
    def __init__(self, celsius):
        # TODO: Initialize with temperature in celsius
        pass
    
    def __str__(self):
        # TODO: Return string representation like "25°C"
        pass
    
    def __eq__(self, other):
        # TODO: Check if temperatures are equal
        pass
    
    def __lt__(self, other):
        # TODO: Check if this temperature is less than other
        pass
    
    def __le__(self, other):
        # TODO: Check if this temperature is less than or equal to other
        pass
    
    def __gt__(self, other):
        # TODO: Check if this temperature is greater than other
        pass
    
    def __ge__(self, other):
        # TODO: Check if this temperature is greater than or equal to other
        pass


# Exercise 3: Arithmetic Operators
class Money:
    """
    A class representing money with currency.
    
    TODO: Implement the following magic methods:
    - __init__(self, amount, currency="USD")
    - __add__(self, other) - add two Money objects (same currency only)
    - __sub__(self, other) - subtract two Money objects (same currency only)
    - __mul__(self, number) - multiply money by a number
    - __truediv__(self, number) - divide money by a number
    - __str__(self) - return "$X.XX USD" format
    - __eq__(self, other) - check equality
    """
    
    def __init__(self, amount, currency="USD"):
        # TODO: Initialize with amount and currency
        pass
    
    def __str__(self):
        # TODO: Return formatted string like "$10.50 USD"
        pass
    
    def __add__(self, other):
        # TODO: Add two Money objects (check currency compatibility)
        pass
    
    def __sub__(self, other):
        # TODO: Subtract two Money objects (check currency compatibility)
        pass
    
    def __mul__(self, number):
        # TODO: Multiply money by a number
        pass
    
    def __truediv__(self, number):
        # TODO: Divide money by a number
        pass
    
    def __eq__(self, other):
        # TODO: Check if two Money objects are equal
        pass


# Exercise 4: Container Methods
class Playlist:
    """
    A class representing a music playlist.
    
    TODO: Implement the following magic methods:
    - __init__(self, name)
    - __len__(self) - return number of songs
    - __getitem__(self, index) - get song by index
    - __setitem__(self, index, song) - set song at index
    - __contains__(self, song) - check if song is in playlist
    - __iter__(self) - make playlist iterable
    - __str__(self) - return playlist info
    """
    
    def __init__(self, name):
        # TODO: Initialize playlist with name and empty song list
        pass
    
    def add_song(self, song):
        """Add a song to the playlist."""
        # TODO: Add song to the internal list
        pass
    
    def __len__(self):
        # TODO: Return number of songs in playlist
        pass
    
    def __getitem__(self, index):
        # TODO: Return song at given index
        pass
    
    def __setitem__(self, index, song):
        # TODO: Set song at given index
        pass
    
    def __contains__(self, song):
        # TODO: Check if song is in playlist
        pass
    
    def __iter__(self):
        # TODO: Return iterator for songs
        pass
    
    def __str__(self):
        # TODO: Return playlist information
        pass


# Exercise 5: Context Manager
class Timer:
    """
    A context manager that measures execution time.
    
    TODO: Implement the following magic methods:
    - __init__(self, name="Timer")
    - __enter__(self) - start timing
    - __exit__(self, exc_type, exc_val, exc_tb) - stop timing and print result
    """
    
    def __init__(self, name="Timer"):
        # TODO: Initialize timer with name
        pass
    
    def __enter__(self):
        # TODO: Start timing (hint: use time.time())
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Stop timing and print elapsed time
        pass


# Exercise 6: Callable Objects
class Multiplier:
    """
    A callable class that multiplies numbers by a fixed factor.
    
    TODO: Implement the following magic methods:
    - __init__(self, factor)
    - __call__(self, number) - multiply number by factor
    - __str__(self) - return description of multiplier
    """
    
    def __init__(self, factor):
        # TODO: Initialize with multiplication factor
        pass
    
    def __call__(self, number):
        # TODO: Multiply number by factor and return result
        pass
    
    def __str__(self):
        # TODO: Return description like "Multiplier(x3)"
        pass


# Test functions
def test_book():
    """Test the Book class."""
    print("Testing Book class...")
    
    book = Book("1984", "George Orwell", 328)
    
    # Test string representations
    print(f"str(book): {str(book)}")
    print(f"repr(book): {repr(book)}")
    
    expected_str = "1984 by George Orwell"
    expected_repr = "Book('1984', 'George Orwell', 328)"
    
    assert str(book) == expected_str, f"Expected '{expected_str}', got '{str(book)}'"
    assert repr(book) == expected_repr, f"Expected '{expected_repr}', got '{repr(book)}'"
    
    print("✓ Book class tests passed!")


def test_temperature():
    """Test the Temperature class."""
    print("\nTesting Temperature class...")
    
    temp1 = Temperature(25)
    temp2 = Temperature(30)
    temp3 = Temperature(25)
    
    # Test string representation
    assert str(temp1) == "25°C", f"Expected '25°C', got '{str(temp1)}'"
    
    # Test comparisons
    assert temp1 == temp3, "Equal temperatures should be equal"
    assert temp1 != temp2, "Different temperatures should not be equal"
    assert temp1 < temp2, "25°C should be less than 30°C"
    assert temp1 <= temp2, "25°C should be less than or equal to 30°C"
    assert temp1 <= temp3, "25°C should be less than or equal to 25°C"
    assert temp2 > temp1, "30°C should be greater than 25°C"
    assert temp2 >= temp1, "30°C should be greater than or equal to 25°C"
    assert temp3 >= temp1, "25°C should be greater than or equal to 25°C"
    
    print("✓ Temperature class tests passed!")


def test_money():
    """Test the Money class."""
    print("\nTesting Money class...")
    
    money1 = Money(10.50)
    money2 = Money(5.25)
    money3 = Money(10.50)
    
    # Test string representation
    assert str(money1) == "$10.50 USD", f"Expected '$10.50 USD', got '{str(money1)}'"
    
    # Test equality
    assert money1 == money3, "Equal money amounts should be equal"
    assert money1 != money2, "Different money amounts should not be equal"
    
    # Test arithmetic
    result_add = money1 + money2
    assert str(result_add) == "$15.75 USD", f"Expected '$15.75 USD', got '{str(result_add)}'"
    
    result_sub = money1 - money2
    assert str(result_sub) == "$5.25 USD", f"Expected '$5.25 USD', got '{str(result_sub)}'"
    
    result_mul = money1 * 2
    assert str(result_mul) == "$21.00 USD", f"Expected '$21.00 USD', got '{str(result_mul)}'"
    
    result_div = money1 / 2
    assert str(result_div) == "$5.25 USD", f"Expected '$5.25 USD', got '{str(result_div)}'"
    
    print("✓ Money class tests passed!")


def test_playlist():
    """Test the Playlist class."""
    print("\nTesting Playlist class...")
    
    playlist = Playlist("My Favorites")
    
    # Add some songs
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")
    
    # Test length
    assert len(playlist) == 3, f"Expected length 3, got {len(playlist)}"
    
    # Test item access
    assert playlist[0] == "Song 1", f"Expected 'Song 1', got '{playlist[0]}'"
    assert playlist[1] == "Song 2", f"Expected 'Song 2', got '{playlist[1]}'"
    
    # Test item assignment
    playlist[1] = "New Song 2"
    assert playlist[1] == "New Song 2", f"Expected 'New Song 2', got '{playlist[1]}'"
    
    # Test contains
    assert "Song 1" in playlist, "Song 1 should be in playlist"
    assert "Song 4" not in playlist, "Song 4 should not be in playlist"
    
    # Test iteration
    songs = list(playlist)
    expected_songs = ["Song 1", "New Song 2", "Song 3"]
    assert songs == expected_songs, f"Expected {expected_songs}, got {songs}"
    
    print("✓ Playlist class tests passed!")


def test_timer():
    """Test the Timer context manager."""
    print("\nTesting Timer context manager...")
    
    import time
    
    # Test basic timing
    with Timer("Test Timer") as timer:
        time.sleep(0.1)  # Sleep for 100ms
    
    print("✓ Timer context manager test completed!")


def test_multiplier():
    """Test the Multiplier callable class."""
    print("\nTesting Multiplier callable class...")
    
    double = Multiplier(2)
    triple = Multiplier(3)
    
    # Test string representation
    assert str(double) == "Multiplier(x2)", f"Expected 'Multiplier(x2)', got '{str(double)}'"
    assert str(triple) == "Multiplier(x3)", f"Expected 'Multiplier(x3)', got '{str(triple)}'"
    
    # Test calling
    assert double(5) == 10, f"Expected 10, got {double(5)}"
    assert triple(4) == 12, f"Expected 12, got {triple(4)}"
    
    print("✓ Multiplier class tests passed!")


def main():
    """Run all tests."""
    print("Running Magic Methods Exercises Tests")
    print("=" * 40)
    
    try:
        test_book()
        test_temperature()
        test_money()
        test_playlist()
        test_timer()
        test_multiplier()
        
        print("\n" + "=" * 40)
        print("🎉 All tests passed! Great job implementing magic methods!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("Please check your implementation and try again.")


if __name__ == "__main__":
    main()