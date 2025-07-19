"""
Inventory Management System - Solution

This solution demonstrates complex data management using basic Python concepts,
preparing students for intermediate topics like object-oriented design and data analysis.
"""

import json
import csv
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int = 0, 
                 category: str = "General", min_stock: int = 5):
        """Initialize a product."""
        if not product_id or not name:
            raise ValueError("Product ID and name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if min_stock < 0:
            raise ValueError("Minimum stock cannot be negative")
            
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.min_stock = min_stock
    
    def update_quantity(self, change: int) -> bool:
        """Update product quantity."""
        new_quantity = self.quantity + change
        if new_quantity < 0:
            return False
        self.quantity = new_quantity
        return True
    
    def is_low_stock(self) -> bool:
        """Check if product is below minimum stock level."""
        return self.quantity <= self.min_stock
    
    def get_value(self) -> float:
        """Calculate total value of this product in inventory."""
        return self.price * self.quantity
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category,
            "min_stock": self.min_stock
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            category=data.get("category", "General"),
            min_stock=data.get("min_stock", 5)
        )


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
        """Add a new product to inventory."""
        if product_id in self.products:
            return False
        
        try:
            product = Product(product_id, name, price, quantity, category, min_stock)
            self.products[product_id] = product
            self.log_transaction("ADD_PRODUCT", product_id, {
                "name": name,
                "price": price,
                "quantity": quantity,
                "category": category
            })
            return True
        except ValueError:
            return False
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from inventory."""
        if product_id not in self.products:
            return False
        
        product = self.products[product_id]
        del self.products[product_id]
        self.log_transaction("REMOVE_PRODUCT", product_id, {
            "name": product.name,
            "final_quantity": product.quantity
        })
        return True
    
    def update_stock(self, product_id: str, quantity_change: int, 
                    reason: str = "Manual adjustment") -> bool:
        """Update stock quantity for a product."""
        if product_id not in self.products:
            return False
        
        product = self.products[product_id]
        old_quantity = product.quantity
        
        if product.update_quantity(quantity_change):
            self.log_transaction("UPDATE_STOCK", product_id, {
                "old_quantity": old_quantity,
                "new_quantity": product.quantity,
                "change": quantity_change,
                "reason": reason
            })
            return True
        return False
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        return self.products.get(product_id)
    
    def search_products(self, query: str) -> List[Product]:
        """Search products by name or category."""
        query_lower = query.lower()
        matching_products = []
        
        for product in self.products.values():
            if (query_lower in product.name.lower() or 
                query_lower in product.category.lower()):
                matching_products.append(product)
        
        return matching_products
    
    def get_low_stock_products(self) -> List[Product]:
        """Get products that are below minimum stock level."""
        return [product for product in self.products.values() if product.is_low_stock()]
    
    def get_products_by_category(self, category: str) -> List[Product]:
        """Get all products in a specific category."""
        return [product for product in self.products.values() 
                if product.category.lower() == category.lower()]
    
    def calculate_total_inventory_value(self) -> float:
        """Calculate total value of all inventory."""
        return sum(product.get_value() for product in self.products.values())
    
    def get_inventory_summary(self) -> Dict:
        """Get summary statistics of inventory."""
        if not self.products:
            return {
                "total_products": 0,
                "total_value": 0,
                "categories": {},
                "low_stock_count": 0,
                "average_product_value": 0
            }
        
        categories = {}
        low_stock_count = 0
        total_value = 0
        
        for product in self.products.values():
            # Count by category
            if product.category not in categories:
                categories[product.category] = 0
            categories[product.category] += 1
            
            # Count low stock
            if product.is_low_stock():
                low_stock_count += 1
            
            # Add to total value
            total_value += product.get_value()
        
        return {
            "total_products": len(self.products),
            "total_value": total_value,
            "categories": categories,
            "low_stock_count": low_stock_count,
            "average_product_value": total_value / len(self.products)
        }
    
    def generate_inventory_report(self) -> str:
        """Generate a formatted inventory report."""
        if not self.products:
            return "No products in inventory."
        
        summary = self.get_inventory_summary()
        report_lines = [
            "Inventory Report",
            "=" * 50,
            f"Total Products: {summary['total_products']}",
            f"Total Value: ${summary['total_value']:.2f}",
            f"Average Product Value: ${summary['average_product_value']:.2f}",
            f"Low Stock Items: {summary['low_stock_count']}",
            "",
            "Products by Category:",
        ]
        
        for category, count in summary['categories'].items():
            report_lines.append(f"  {category}: {count} products")
        
        report_lines.extend([
            "",
            "Product Details:",
            "-" * 80,
            f"{'ID':<10} {'Name':<20} {'Category':<15} {'Price':<8} {'Qty':<5} {'Value':<10} {'Status'}"
        ])
        
        for product in sorted(self.products.values(), key=lambda p: p.name):
            status = "LOW STOCK" if product.is_low_stock() else "OK"
            report_lines.append(
                f"{product.product_id:<10} {product.name:<20} {product.category:<15} "
                f"${product.price:<7.2f} {product.quantity:<5} ${product.get_value():<9.2f} {status}"
            )
        
        return "\n".join(report_lines)
    
    def generate_low_stock_alert(self) -> str:
        """Generate low stock alert report."""
        low_stock_products = self.get_low_stock_products()
        
        if not low_stock_products:
            return "No products are currently low in stock."
        
        alert_lines = [
            "LOW STOCK ALERT",
            "=" * 30,
            f"Found {len(low_stock_products)} products below minimum stock level:",
            ""
        ]
        
        for product in sorted(low_stock_products, key=lambda p: p.quantity):
            reorder_qty = max(product.min_stock * 2, 10)  # Simple reorder calculation
            alert_lines.append(
                f"• {product.name} (ID: {product.product_id}): "
                f"{product.quantity} left (min: {product.min_stock}) "
                f"- Suggest reordering {reorder_qty} units"
            )
        
        return "\n".join(alert_lines)
    
    def save_inventory(self) -> bool:
        """Save inventory to file."""
        try:
            data = {
                "products": [product.to_dict() for product in self.products.values()],
                "transaction_history": self.transaction_history[-100:]  # Keep last 100 transactions
            }
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error saving inventory: {e}")
            return False
    
    def load_inventory(self) -> bool:
        """Load inventory from file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Load products
            for product_data in data.get("products", []):
                product = Product.from_dict(product_data)
                self.products[product.product_id] = product
            
            # Load transaction history
            self.transaction_history = data.get("transaction_history", [])
            
            return True
        except FileNotFoundError:
            return False  # File doesn't exist yet, that's okay
        except Exception as e:
            print(f"Error loading inventory: {e}")
            return False
    
    def export_to_csv(self, filename: str) -> bool:
        """Export inventory to CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    "Product ID", "Name", "Category", "Price", 
                    "Quantity", "Min Stock", "Total Value", "Status"
                ])
                
                # Write product data
                for product in sorted(self.products.values(), key=lambda p: p.name):
                    status = "LOW STOCK" if product.is_low_stock() else "OK"
                    writer.writerow([
                        product.product_id,
                        product.name,
                        product.category,
                        product.price,
                        product.quantity,
                        product.min_stock,
                        product.get_value(),
                        status
                    ])
            
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def log_transaction(self, transaction_type: str, product_id: str, 
                       details: Dict) -> None:
        """Log a transaction to history."""
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "type": transaction_type,
            "product_id": product_id,
            "details": details
        }
        self.transaction_history.append(transaction)
    
    def get_transaction_history(self, product_id: str = None, 
                              limit: int = 10) -> List[Dict]:
        """Get transaction history."""
        transactions = self.transaction_history
        
        # Filter by product ID if specified
        if product_id:
            transactions = [t for t in transactions if t["product_id"] == product_id]
        
        # Return most recent transactions
        return transactions[-limit:] if transactions else []


def main():
    """Simplified main function for demonstration."""
    inventory = InventoryManager()
    
    # Add some sample products
    inventory.add_product("P001", "Laptop", 999.99, 10, "Electronics", 3)
    inventory.add_product("P002", "Mouse", 29.99, 50, "Electronics", 10)
    inventory.add_product("P003", "Notebook", 2.99, 2, "Office", 20)  # Low stock
    
    print("Sample Inventory Management System")
    print("=" * 40)
    
    # Show inventory report
    print(inventory.generate_inventory_report())
    
    # Show low stock alert
    print("\n" + inventory.generate_low_stock_alert())
    
    # Demonstrate search
    print(f"\nSearching for 'electronics':")
    results = inventory.search_products("electronics")
    for product in results:
        print(f"  {product.name} - ${product.price}")
    
    # Save inventory
    if inventory.save_inventory():
        print("\nInventory saved successfully!")


if __name__ == "__main__":
    main()