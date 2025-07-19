"""
Inventory Management System - Review Exercise

This exercise combines multiple basic concepts:
- Dictionaries and nested data structures
- Lists and list operations
- Functions and parameter validation
- File operations (JSON/CSV)
- Error handling and data validation
- Mathematical operations and calculations

Requirements:
1. Create an InventoryManager class that can:
   - Add, update, and remove products
   - Track stock levels and prices
   - Calculate inventory values
   - Generate low stock alerts
   - Save/load inventory data
   - Generate sales and inventory reports

2. Implement proper data validation
3. Handle edge cases (negative quantities, invalid prices)
4. Provide search and filtering capabilities

This bridges to intermediate concepts by introducing:
- Complex data structures and relationships
- Business logic implementation
- Data persistence patterns
- Reporting and analytics basics
"""

import json
import csv
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int = 0, 
                 category: str = "General", min_stock: int = 5):
        """
        Initialize a product.
        
        Args:
            product_id: Unique identifier for the product
            name: Product name
            price: Product price
            quantity: Current stock quantity
            category: Product category
            min_stock: Minimum stock level for alerts
        """
        # TODO: Implement product initialization
        # - Validate input parameters
        # - Set instance variables
        # - Handle edge cases (negative values, empty strings)
        pass
    
    def update_quantity(self, change: int) -> bool:
        """
        Update product quantity.
        
        Args:
            change: Change in quantity (positive for add, negative for remove)
            
        Returns:
            True if successful, False if would result in negative quantity
        """
        # TODO: Implement quantity update
        # - Check if change would result in negative quantity
        # - Update quantity if valid
        # - Return success status
        pass
    
    def is_low_stock(self) -> bool:
        """Check if product is below minimum stock level."""
        # TODO: Implement low stock check
        pass
    
    def get_value(self) -> float:
        """Calculate total value of this product in inventory."""
        # TODO: Implement value calculation
        pass
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        # TODO: Implement dictionary conversion
        pass
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        # TODO: Implement product creation from dictionary
        pass


class InventoryManager:
    """Manages inventory of products."""
    
    def __init__(self, data_file: str = "inventory.json"):
        """Initialize inventory manager."""
        self.data_file = data_file
        self.products = {}  # Dict[str, Product]
        self.transaction_history = []  # List of transaction records
        self.load_inventory()
    
    def add_product(self, product_id: str, name: str, price: float, 
                   quantity: int = 0, category: str = "General", 
                   min_stock: int = 5) -> bool:
        """
        Add a new product to inventory.
        
        Args:
            product_id: Unique identifier
            name: Product name
            price: Product price
            quantity: Initial quantity
            category: Product category
            min_stock: Minimum stock level
            
        Returns:
            True if added successfully, False if product already exists
        """
        # TODO: Implement product addition
        # - Check if product already exists
        # - Create new Product instance
        # - Add to products dictionary
        # - Log transaction
        # - Return success status
        pass
    
    def remove_product(self, product_id: str) -> bool:
        """
        Remove a product from inventory.
        
        Args:
            product_id: Product identifier
            
        Returns:
            True if removed, False if product doesn't exist
        """
        # TODO: Implement product removal
        # - Check if product exists
        # - Remove from products dictionary
        # - Log transaction
        # - Return success status
        pass
    
    def update_stock(self, product_id: str, quantity_change: int, 
                    reason: str = "Manual adjustment") -> bool:
        """
        Update stock quantity for a product.
        
        Args:
            product_id: Product identifier
            quantity_change: Change in quantity
            reason: Reason for the change
            
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement stock update
        # - Check if product exists
        # - Update product quantity
        # - Log transaction
        # - Return success status
        pass
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        # TODO: Implement product retrieval
        pass
    
    def search_products(self, query: str) -> List[Product]:
        """
        Search products by name or category.
        
        Args:
            query: Search query
            
        Returns:
            List of matching products
        """
        # TODO: Implement product search
        # - Search by product name (case-insensitive)
        # - Search by category
        # - Return list of matching products
        pass
    
    def get_low_stock_products(self) -> List[Product]:
        """Get products that are below minimum stock level."""
        # TODO: Implement low stock detection
        pass
    
    def get_products_by_category(self, category: str) -> List[Product]:
        """Get all products in a specific category."""
        # TODO: Implement category filtering
        pass
    
    def calculate_total_inventory_value(self) -> float:
        """Calculate total value of all inventory."""
        # TODO: Implement total value calculation
        pass
    
    def get_inventory_summary(self) -> Dict:
        """Get summary statistics of inventory."""
        # TODO: Implement inventory summary
        # - Total products
        # - Total value
        # - Products by category
        # - Low stock count
        # - Average product value
        pass
    
    def generate_inventory_report(self) -> str:
        """Generate a formatted inventory report."""
        # TODO: Implement report generation
        # - Include summary statistics
        # - List all products with details
        # - Highlight low stock items
        # - Format nicely with proper alignment
        pass
    
    def generate_low_stock_alert(self) -> str:
        """Generate low stock alert report."""
        # TODO: Implement low stock alert
        # - Get low stock products
        # - Format alert message
        # - Include reorder suggestions
        pass
    
    def save_inventory(self) -> bool:
        """Save inventory to file."""
        # TODO: Implement inventory saving
        # - Convert products to serializable format
        # - Save to JSON file
        # - Handle file writing errors
        # - Return success status
        pass
    
    def load_inventory(self) -> bool:
        """Load inventory from file."""
        # TODO: Implement inventory loading
        # - Read from JSON file
        # - Create Product instances
        # - Handle file reading errors
        # - Return success status
        pass
    
    def export_to_csv(self, filename: str) -> bool:
        """Export inventory to CSV file."""
        # TODO: Implement CSV export
        # - Create CSV with product details
        # - Include headers
        # - Handle file writing errors
        # - Return success status
        pass
    
    def log_transaction(self, transaction_type: str, product_id: str, 
                       details: Dict) -> None:
        """Log a transaction to history."""
        # TODO: Implement transaction logging
        # - Create transaction record with timestamp
        # - Add to transaction history
        # - Include transaction type, product ID, and details
        pass
    
    def get_transaction_history(self, product_id: str = None, 
                              limit: int = 10) -> List[Dict]:
        """
        Get transaction history.
        
        Args:
            product_id: Filter by product ID (optional)
            limit: Maximum number of transactions to return
            
        Returns:
            List of transaction records
        """
        # TODO: Implement transaction history retrieval
        # - Filter by product ID if specified
        # - Return most recent transactions
        # - Limit results as requested
        pass


def display_menu():
    """Display the main menu options."""
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Update Stock")
    print("4. View Product")
    print("5. Search Products")
    print("6. View Low Stock Alert")
    print("7. Generate Inventory Report")
    print("8. View Inventory Summary")
    print("9. Export to CSV")
    print("10. View Transaction History")
    print("11. Save Inventory")
    print("12. Exit")
    print("=" * 36)


def get_float_input(prompt: str, min_val: float = None) -> Optional[float]:
    """Helper function to get validated float input."""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            return None


def get_int_input(prompt: str, min_val: int = None) -> Optional[int]:
    """Helper function to get validated integer input."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            return None


def main():
    """Main program loop with menu-driven interface."""
    inventory = InventoryManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ").strip()
        
        if choice == "1":
            # TODO: Implement add product functionality
            pass
            
        elif choice == "2":
            # TODO: Implement remove product functionality
            pass
            
        elif choice == "3":
            # TODO: Implement update stock functionality
            pass
            
        elif choice == "4":
            # TODO: Implement view product functionality
            pass
            
        elif choice == "5":
            # TODO: Implement search products functionality
            pass
            
        elif choice == "6":
            # TODO: Implement low stock alert functionality
            pass
            
        elif choice == "7":
            # TODO: Implement inventory report functionality
            pass
            
        elif choice == "8":
            # TODO: Implement inventory summary functionality
            pass
            
        elif choice == "9":
            # TODO: Implement CSV export functionality
            pass
            
        elif choice == "10":
            # TODO: Implement transaction history functionality
            pass
            
        elif choice == "11":
            # TODO: Implement save inventory functionality
            pass
            
        elif choice == "12":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()