"""
Smart Asset Tracking and Inventory Monitoring System
IoT-Based Solution for Warehouses and Logistics Management

This module implements a comprehensive simulation of an asset tracking and inventory
monitoring system using IoT technologies including RFID, GPS, and barcode scanning.
"""

import json
import csv
import random
import datetime
from enum import Enum
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import statistics


class AssetStatus(Enum):
    """Asset status enumeration."""
    IN_WAREHOUSE = "In Warehouse"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    LOST = "Lost"
    DAMAGED = "Damaged"


class InventoryLevel(Enum):
    """Inventory level status."""
    OPTIMAL = "Optimal"
    LOW = "Low"
    CRITICAL = "Critical"
    OVERSTOCKED = "Overstocked"


class AlertType(Enum):
    """Alert type enumeration."""
    LOW_STOCK = "Low Stock"
    ASSET_MISSING = "Asset Missing"
    UNAUTHORIZED_ACCESS = "Unauthorized Access"
    TEMPERATURE_ANOMALY = "Temperature Anomaly"
    LOCATION_ANOMALY = "Location Anomaly"
    DELIVERY_DELAYED = "Delivery Delayed"


@dataclass
class Asset:
    """Represents a tracked asset."""
    asset_id: str
    asset_name: str
    rfid_tag: str
    category: str
    location: str
    status: str
    last_scanned: str
    gps_latitude: float
    gps_longitude: float
    temperature: float
    humidity: float


@dataclass
class InventoryItem:
    """Represents an inventory item."""
    item_id: str
    item_name: str
    category: str
    quantity: int
    reorder_point: int
    warehouse_location: str
    last_updated: str
    supplier: str


@dataclass
class TrackingReading:
    """Represents a tracking reading."""
    timestamp: str
    asset_id: str
    asset_name: str
    location: str
    status: str
    gps_latitude: float
    gps_longitude: float
    temperature: float
    humidity: float
    signal_strength: int
    battery_level: int
    rfid_read_count: int


@dataclass
class InventoryReading:
    """Represents an inventory reading."""
    timestamp: str
    item_id: str
    item_name: str
    quantity: int
    inventory_level: str
    warehouse_location: str
    last_movement: str
    movement_type: str


@dataclass
class Alert:
    """Represents a system alert."""
    timestamp: str
    alert_type: str
    asset_id: str
    message: str
    severity: str


class AssetTracker:
    """Simulates RFID/GPS asset tracking."""
    
    def __init__(self, asset_id: str, asset_name: str):
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.rfid_tag = f"RFID_{asset_id}"
        self.status = AssetStatus.IN_WAREHOUSE.value
        self.location = random.choice(["Warehouse A", "Warehouse B", "Warehouse C", "Transit Hub"])
        self.gps_latitude = 28.6139 + random.uniform(-0.1, 0.1)
        self.gps_longitude = 77.2090 + random.uniform(-0.1, 0.1)
        self.temperature = 22.0 + random.uniform(-2, 2)
        self.humidity = 50.0 + random.uniform(-10, 10)
        self.signal_strength = random.randint(70, 100)
        self.battery_level = random.randint(60, 100)
        self.rfid_read_count = 0
        self.last_scanned = datetime.datetime.now().isoformat()
    
    def update_location(self) -> None:
        """Update asset location with GPS drift."""
        self.gps_latitude += random.uniform(-0.01, 0.01)
        self.gps_longitude += random.uniform(-0.01, 0.01)
        self.signal_strength = max(10, self.signal_strength + random.randint(-5, 5))
        self.battery_level = max(0, self.battery_level - random.randint(0, 2))
        self.last_scanned = datetime.datetime.now().isoformat()
    
    def update_environmental_conditions(self) -> None:
        """Update temperature and humidity readings."""
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-2, 2)
        self.temperature = max(15, min(35, self.temperature))
        self.humidity = max(20, min(80, self.humidity))
    
    def simulate_movement(self) -> None:
        """Simulate asset movement."""
        if random.random() < 0.3:
            self.status = AssetStatus.IN_TRANSIT.value
            self.location = "Transit Hub"
        elif random.random() < 0.2:
            self.status = AssetStatus.DELIVERED.value
        else:
            self.status = AssetStatus.IN_WAREHOUSE.value
            self.location = random.choice(["Warehouse A", "Warehouse B", "Warehouse C"])
    
    def get_reading(self) -> TrackingReading:
        """Get current asset reading."""
        self.update_location()
        self.update_environmental_conditions()
        self.rfid_read_count += 1
        
        return TrackingReading(
            timestamp=datetime.datetime.now().isoformat(),
            asset_id=self.asset_id,
            asset_name=self.asset_name,
            location=self.location,
            status=self.status,
            gps_latitude=round(self.gps_latitude, 6),
            gps_longitude=round(self.gps_longitude, 6),
            temperature=round(self.temperature, 2),
            humidity=round(self.humidity, 2),
            signal_strength=self.signal_strength,
            battery_level=self.battery_level,
            rfid_read_count=self.rfid_read_count
        )


class InventoryManager:
    """Manages inventory levels and stock."""
    
    def __init__(self, item_id: str, item_name: str, initial_quantity: int):
        self.item_id = item_id
        self.item_name = item_name
        self.category = random.choice(["Electronics", "Machinery", "Consumables", "Raw Materials"])
        self.quantity = initial_quantity
        self.reorder_point = initial_quantity * 0.2
        self.warehouse_location = random.choice(["Zone A1", "Zone A2", "Zone B1", "Zone B2", "Zone C1"])
        self.supplier = random.choice(["Supplier A", "Supplier B", "Supplier C", "Supplier D"])
        self.last_updated = datetime.datetime.now().isoformat()
        self.movement_history = []
    
    def consume_stock(self, quantity: int) -> None:
        """Consume inventory."""
        self.quantity = max(0, self.quantity - quantity)
        self.last_updated = datetime.datetime.now().isoformat()
        self.movement_history.append(("OUT", quantity, self.last_updated))
    
    def restock(self, quantity: int) -> None:
        """Add inventory."""
        self.quantity += quantity
        self.last_updated = datetime.datetime.now().isoformat()
        self.movement_history.append(("IN", quantity, self.last_updated))
    
    def get_inventory_level(self) -> str:
        """Determine inventory level status."""
        if self.quantity == 0:
            return InventoryLevel.CRITICAL.value
        elif self.quantity <= self.reorder_point:
            return InventoryLevel.LOW.value
        elif self.quantity > self.reorder_point * 5:
            return InventoryLevel.OVERSTOCKED.value
        else:
            return InventoryLevel.OPTIMAL.value
    
    def get_reading(self) -> InventoryReading:
        """Get current inventory reading."""
        last_movement = self.movement_history[-1] if self.movement_history else ("INITIAL", 0, self.last_updated)
        
        return InventoryReading(
            timestamp=datetime.datetime.now().isoformat(),
            item_id=self.item_id,
            item_name=self.item_name,
            quantity=self.quantity,
            inventory_level=self.get_inventory_level(),
            warehouse_location=self.warehouse_location,
            last_movement=last_movement[2],
            movement_type=last_movement[0]
        )


class AlertGenerator:
    """Generates alerts based on system conditions."""
    
    def __init__(self):
        self.alerts = []
    
    def check_asset_alerts(self, tracker: AssetTracker) -> List[Alert]:
        """Check for asset-related alerts."""
        alerts = []
        
        if tracker.battery_level < 20:
            alerts.append(Alert(
                timestamp=datetime.datetime.now().isoformat(),
                alert_type=AlertType.ASSET_MISSING.value,
                asset_id=tracker.asset_id,
                message=f"Asset {tracker.asset_name} has low battery ({tracker.battery_level}%)",
                severity="WARNING"
            ))
        
        if tracker.temperature > 30 or tracker.temperature < 18:
            alerts.append(Alert(
                timestamp=datetime.datetime.now().isoformat(),
                alert_type=AlertType.TEMPERATURE_ANOMALY.value,
                asset_id=tracker.asset_id,
                message=f"Temperature anomaly for {tracker.asset_name}: {tracker.temperature}°C",
                severity="CRITICAL"
            ))
        
        if tracker.signal_strength < 30:
            alerts.append(Alert(
                timestamp=datetime.datetime.now().isoformat(),
                alert_type=AlertType.LOCATION_ANOMALY.value,
                asset_id=tracker.asset_id,
                message=f"Weak signal for {tracker.asset_name}: {tracker.signal_strength}%",
                severity="WARNING"
            ))
        
        return alerts
    
    def check_inventory_alerts(self, inventory: InventoryManager) -> List[Alert]:
        """Check for inventory-related alerts."""
        alerts = []
        
        if inventory.get_inventory_level() == InventoryLevel.CRITICAL.value:
            alerts.append(Alert(
                timestamp=datetime.datetime.now().isoformat(),
                alert_type=AlertType.LOW_STOCK.value,
                asset_id=inventory.item_id,
                message=f"Critical stock level for {inventory.item_name}: {inventory.quantity} units",
                severity="CRITICAL"
            ))
        elif inventory.get_inventory_level() == InventoryLevel.LOW.value:
            alerts.append(Alert(
                timestamp=datetime.datetime.now().isoformat(),
                alert_type=AlertType.LOW_STOCK.value,
                asset_id=inventory.item_id,
                message=f"Low stock for {inventory.item_name}: {inventory.quantity} units",
                severity="WARNING"
            ))
        
        return alerts


class WarehouseAnalytics:
    """Analyzes warehouse and logistics data."""
    
    def __init__(self):
        self.asset_readings = []
        self.inventory_readings = []
        self.alerts = []
    
    def add_asset_reading(self, reading: TrackingReading) -> None:
        """Add asset tracking reading."""
        self.asset_readings.append(reading)
    
    def add_inventory_reading(self, reading: InventoryReading) -> None:
        """Add inventory reading."""
        self.inventory_readings.append(reading)
    
    def add_alert(self, alert: Alert) -> None:
        """Add alert."""
        self.alerts.append(alert)
    
    def get_asset_statistics(self) -> Dict:
        """Calculate asset tracking statistics."""
        if not self.asset_readings:
            return {}
        
        temperatures = [r.temperature for r in self.asset_readings]
        humidities = [r.humidity for r in self.asset_readings]
        signal_strengths = [r.signal_strength for r in self.asset_readings]
        battery_levels = [r.battery_level for r in self.asset_readings]
        
        return {
            "total_readings": len(self.asset_readings),
            "avg_temperature": round(statistics.mean(temperatures), 2),
            "avg_humidity": round(statistics.mean(humidities), 2),
            "avg_signal_strength": round(statistics.mean(signal_strengths), 2),
            "avg_battery_level": round(statistics.mean(battery_levels), 2),
            "min_temperature": round(min(temperatures), 2),
            "max_temperature": round(max(temperatures), 2),
            "min_humidity": round(min(humidities), 2),
            "max_humidity": round(max(humidities), 2),
            "assets_in_warehouse": len([r for r in self.asset_readings if r.status == AssetStatus.IN_WAREHOUSE.value]),
            "assets_in_transit": len([r for r in self.asset_readings if r.status == AssetStatus.IN_TRANSIT.value]),
            "assets_delivered": len([r for r in self.asset_readings if r.status == AssetStatus.DELIVERED.value])
        }
    
    def get_inventory_statistics(self) -> Dict:
        """Calculate inventory statistics."""
        if not self.inventory_readings:
            return {}
        
        quantities = [r.quantity for r in self.inventory_readings]
        
        return {
            "total_readings": len(self.inventory_readings),
            "total_items": len(set(r.item_id for r in self.inventory_readings)),
            "avg_quantity": round(statistics.mean(quantities), 2),
            "total_quantity": sum(quantities),
            "optimal_items": len([r for r in self.inventory_readings if r.inventory_level == InventoryLevel.OPTIMAL.value]),
            "low_stock_items": len([r for r in self.inventory_readings if r.inventory_level == InventoryLevel.LOW.value]),
            "critical_items": len([r for r in self.inventory_readings if r.inventory_level == InventoryLevel.CRITICAL.value]),
            "overstocked_items": len([r for r in self.inventory_readings if r.inventory_level == InventoryLevel.OVERSTOCKED.value])
        }
    
    def get_alert_statistics(self) -> Dict:
        """Calculate alert statistics."""
        if not self.alerts:
            return {"total_alerts": 0}
        
        return {
            "total_alerts": len(self.alerts),
            "critical_alerts": len([a for a in self.alerts if a.severity == "CRITICAL"]),
            "warning_alerts": len([a for a in self.alerts if a.severity == "WARNING"]),
            "low_stock_alerts": len([a for a in self.alerts if a.alert_type == AlertType.LOW_STOCK.value]),
            "temperature_alerts": len([a for a in self.alerts if a.alert_type == AlertType.TEMPERATURE_ANOMALY.value]),
            "location_alerts": len([a for a in self.alerts if a.alert_type == AlertType.LOCATION_ANOMALY.value])
        }


class SmartAssetTrackingSystem:
    """Main system controller."""
    
    def __init__(self, warehouse_id: str):
        self.warehouse_id = warehouse_id
        self.asset_trackers = []
        self.inventory_managers = []
        self.alert_generator = AlertGenerator()
        self.analytics = WarehouseAnalytics()
    
    def initialize_assets(self, num_assets: int = 20) -> None:
        """Initialize asset trackers."""
        categories = ["Pallet", "Container", "Equipment", "Vehicle", "Package"]
        for i in range(num_assets):
            asset_id = f"AST_{self.warehouse_id}_{i+1:03d}"
            asset_name = f"{random.choice(categories)} {i+1}"
            tracker = AssetTracker(asset_id, asset_name)
            self.asset_trackers.append(tracker)
    
    def initialize_inventory(self, num_items: int = 15) -> None:
        """Initialize inventory items."""
        item_names = [
            "Electronic Components", "Industrial Machinery", "Raw Materials",
            "Packaging Materials", "Tools and Equipment", "Spare Parts",
            "Consumer Goods", "Chemical Supplies", "Metal Stock", "Textiles",
            "Rubber Products", "Plastic Materials", "Glass Items", "Wood Products", "Ceramics"
        ]
        for i, name in enumerate(item_names[:num_items]):
            item_id = f"INV_{self.warehouse_id}_{i+1:03d}"
            initial_qty = random.randint(50, 500)
            manager = InventoryManager(item_id, name, initial_qty)
            self.inventory_managers.append(manager)
    
    def run_simulation(self, num_cycles: int = 1000) -> None:
        """Run the simulation for specified cycles."""
        print(f"\n{'='*80}")
        print(f"RUNNING SMART ASSET TRACKING SIMULATION")
        print(f"Warehouse: {self.warehouse_id}")
        print(f"Assets: {len(self.asset_trackers)}")
        print(f"Inventory Items: {len(self.inventory_managers)}")
        print(f"Simulation Cycles: {num_cycles}")
        print(f"{'='*80}\n")
        
        for cycle in range(num_cycles):
            if (cycle + 1) % 100 == 0:
                print(f"✓ Completed cycle {cycle + 1}/{num_cycles}")
            
            # Track assets
            for tracker in self.asset_trackers:
                tracker.simulate_movement()
                reading = tracker.get_reading()
                self.analytics.add_asset_reading(reading)
                
                # Check for alerts
                alerts = self.alert_generator.check_asset_alerts(tracker)
                for alert in alerts:
                    self.analytics.add_alert(alert)
            
            # Track inventory
            for inventory in self.inventory_managers:
                if random.random() < 0.3:
                    inventory.consume_stock(random.randint(1, 10))
                if random.random() < 0.2:
                    inventory.restock(random.randint(20, 100))
                
                reading = inventory.get_reading()
                self.analytics.add_inventory_reading(reading)
                
                # Check for alerts
                alerts = self.alert_generator.check_inventory_alerts(inventory)
                for alert in alerts:
                    self.analytics.add_alert(alert)
        
        print(f"\n{'='*80}")
        print(f"✓ SIMULATION COMPLETED SUCCESSFULLY")
        print(f"{'='*80}\n")
    
    def export_data(self) -> None:
        """Export all data to CSV and JSON."""
        # Export asset readings
        with open("asset_tracking_readings.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=TrackingReading.__dataclass_fields__.keys())
            writer.writeheader()
            for reading in self.analytics.asset_readings:
                writer.writerow(asdict(reading))
        
        # Export inventory readings
        with open("inventory_readings.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=InventoryReading.__dataclass_fields__.keys())
            writer.writeheader()
            for reading in self.analytics.inventory_readings:
                writer.writerow(asdict(reading))
        
        # Export alerts
        with open("system_alerts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=Alert.__dataclass_fields__.keys())
            writer.writeheader()
            for alert in self.analytics.alerts:
                writer.writerow(asdict(alert))
        
        # Export JSON with statistics
        data = {
            "warehouse_id": self.warehouse_id,
            "simulation_timestamp": datetime.datetime.now().isoformat(),
            "asset_statistics": self.analytics.get_asset_statistics(),
            "inventory_statistics": self.analytics.get_inventory_statistics(),
            "alert_statistics": self.analytics.get_alert_statistics(),
            "total_asset_readings": len(self.analytics.asset_readings),
            "total_inventory_readings": len(self.analytics.inventory_readings),
            "total_alerts": len(self.analytics.alerts)
        }
        
        with open("warehouse_analytics.json", "w") as f:
            json.dump(data, f, indent=2)
        
        print("✓ Data exported to CSV and JSON files")
    
    def print_statistics(self) -> None:
        """Print simulation statistics."""
        asset_stats = self.analytics.get_asset_statistics()
        inventory_stats = self.analytics.get_inventory_statistics()
        alert_stats = self.analytics.get_alert_statistics()
        
        print(f"\n{'='*80}")
        print(f"ASSET TRACKING STATISTICS")
        print(f"{'='*80}")
        for key, value in asset_stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print(f"\n{'='*80}")
        print(f"INVENTORY STATISTICS")
        print(f"{'='*80}")
        for key, value in inventory_stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print(f"\n{'='*80}")
        print(f"ALERT STATISTICS")
        print(f"{'='*80}")
        for key, value in alert_stats.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print(f"\n{'='*80}\n")


def main():
    """Main entry point."""
    system = SmartAssetTrackingSystem("WH_001")
    system.initialize_assets(20)
    system.initialize_inventory(15)
    system.run_simulation(1000)
    system.export_data()
    system.print_statistics()


if __name__ == "__main__":
    main()
