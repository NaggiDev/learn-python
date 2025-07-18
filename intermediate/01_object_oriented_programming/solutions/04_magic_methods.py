"""
Magic Methods Solutions

This file contains the complete solutions for the magic methods exercises.
"""

import time


# Exercise 1: String Representation
class Book:
    """A class representing a book."""
    
    def __init__(self, title, author, pages):
        """Initialize the book with title, author, and pages."""
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f"Book('{self.title}', '{self.author}', {self.pages})"


# Exercise 2: Comparison Operators
class Temperature:
    """A class representing temperature in Celsius."""
    
    def __init__(self, celsius):
        """Initialize with temperature in celsius."""
        self.celsius = celsius
    
    def __str__(self):
        """Return string representation like '25°C'."""
        return f"{self.celsius}°C"
    
    def __eq__(self, other):
        """Check if temperatures are equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius == other.celsius
    
    def __lt__(self, other):
        """Check if this temperature is less than other."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius < other.celsius
    
    def __le__(self, other):
        """Check if this temperature is less than or equal to other."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius <= other.celsius
    
    def __gt__(self, other):
        """Check if this temperature is greater than other."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius > other.celsius
    
    def __ge__(self, other):
        """Check if this temperature is greater than or equal to other."""
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.celsius >= other.celsius


# Exercise 3: Arithmetic Operators
class Money:
    """A class representing money with currency."""
    
    def __init__(self, amount, currency="USD"):
        """Initialize with amount and currency."""
        self.amount = round(float(amount), 2)  # Round to 2 decimal places
        self.currency = currency
    
    def __str__(self):
        """Return formatted string like '$10.50 USD'."""
        return f"${self.amount:.2f} {self.currency}"
    
    def __add__(self, other):
        """Add two Money objects (check currency compatibility)."""
        if not isinstance(other, Money):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        """Subtract two Money objects (check currency compatibility)."""
        if not isinstance(other, Money):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError(f"Cannot subtract {other.currency} from {self.currency}")
        
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, number):
        """Multiply money by a number."""
        if not isinstance(number, (int, float)):
            return NotImplemented
        
        return Money(self.amount * number, self.currency)
    
    def __truediv__(self, number):
        """Divide money by a number."""
        if not isinstance(number, (int, float)):
            return NotImplemented
        
        if number == 0:
            raise ValueError("Cannot divide by zero")
        
        return Money(self.amount / number, self.currency)
    
    def __eq__(self, other):
        """Check if two Money objects are equal."""
        if not isinstance(other, Money):
            return NotImplemented
        
        return self.amount == other.amount and self.currency == other.currency


# Exercise 4: Container Methods
class Playlist:
    """A class representing a music playlist."""
    
    def __init__(self, name):
        """Initialize playlist with name and empty song list."""
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        """Add a song to the playlist."""
        self.songs.append(song)
    
    def __len__(self):
        """Return number of songs in playlist."""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Return song at given index."""
        return self.songs[index]
    
    def __setitem__(self, index, song):
        """Set song at given index."""
        self.songs[index] = song
    
    def __contains__(self, song):
        """Check if song is in playlist."""
        return song in self.songs
    
    def __iter__(self):
        """Return iterator for songs."""
        return iter(self.songs)
    
    def __str__(self):
        """Return playlist information."""
        return f"Playlist '{self.name}' with {len(self.songs)} songs"


# Exercise 5: Context Manager
class Timer:
    """A context manager that measures execution time."""
    
    def __init__(self, name="Timer"):
        """Initialize timer with name."""
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """Start timing."""
        self.start_time = time.time()
        print(f"{self.name} started...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop timing and print elapsed time."""
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"{self.name} finished in {elapsed:.4f} seconds")
        
        # Return False to propagate any exceptions
        return False


# Exercise 6: Callable Objects
class Multiplier:
    """A callable class that multiplies numbers by a fixed factor."""
    
    def __init__(self, factor):
        """Initialize with multiplication factor."""
        self.factor = factor
    
    def __call__(self, number):
        """Multiply number by factor and return result."""
        return number * self.factor
    
    def __str__(self):
        """Return description like 'Multiplier(x3)'."""
        return f"Multiplier(x{self.factor})"


# Test functions (same as in exercises file)
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
    
    # Test currency mismatch
    eur_money = Money(10, "EUR")
    try:
        money1 + eur_money
        assert False, "Should have raised ValueError for currency mismatch"
    except ValueError:
        pass  # Expected
    
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
    
    # Test string representation
    print(f"Playlist info: {playlist}")
    
    print("✓ Playlist class tests passed!")


def test_timer():
    """Test the Timer context manager."""
    print("\nTesting Timer context manager...")
    
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
    
    # Demonstrate usage
    print(f"Using {double}: 5 * 2 = {double(5)}")
    print(f"Using {triple}: 4 * 3 = {triple(4)}")
    
    print("✓ Multiplier class tests passed!")


def main():
    """Run all tests."""
    print("Running Magic Methods Solutions Tests")
    print("=" * 40)
    
    try:
        test_book()
        test_temperature()
        test_money()
        test_playlist()
        test_timer()
        test_multiplier()
        
        print("\n" + "=" * 40)
        print("🎉 All tests passed! Magic methods implementation complete!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()