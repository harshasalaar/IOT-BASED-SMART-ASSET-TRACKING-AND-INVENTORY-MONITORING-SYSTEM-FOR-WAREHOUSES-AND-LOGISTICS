"""
Generate professional visualizations for the Smart Asset Tracking System.
Creates 7 high-resolution charts suitable for the internship report.
"""

import json
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np
from collections import Counter, defaultdict


def load_data():
    """Load simulation data from files."""
    asset_readings = []
    inventory_readings = []
    alerts = []
    
    try:
        with open("asset_tracking_readings.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                asset_readings.append(row)
        
        with open("inventory_readings.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventory_readings.append(row)
        
        with open("system_alerts.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                alerts.append(row)
        
        with open("warehouse_analytics.json", "r") as f:
            analytics = json.load(f)
    except FileNotFoundError:
        print("Error: Data files not found. Please run smart_asset_tracking.py first.")
        return None, None, None, None
    
    return asset_readings, inventory_readings, alerts, analytics


def create_asset_tracking_chart(asset_readings):
    """Chart 1: Asset Tracking Status Distribution."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Chart 1: Asset Tracking Status and Location Distribution', fontsize=16, fontweight='bold')
    
    # Status distribution
    status_counts = Counter(r['status'] for r in asset_readings)
    colors1 = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12', '#95a5a6']
    ax1.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.1f%%', 
            colors=colors1, startangle=90)
    ax1.set_title('Asset Status Distribution', fontweight='bold', pad=20)
    
    # Location distribution
    location_counts = Counter(r['location'] for r in asset_readings)
    locations = list(location_counts.keys())
    counts = list(location_counts.values())
    colors2 = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    ax2.bar(locations, counts, color=colors2, edgecolor='black', linewidth=1.5)
    ax2.set_title('Asset Location Distribution', fontweight='bold', pad=20)
    ax2.set_ylabel('Number of Readings', fontweight='bold')
    ax2.set_xlabel('Location', fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('chart_01_asset_tracking.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 1: Asset Tracking Status - Created")
    plt.close()


def create_environmental_conditions_chart(asset_readings):
    """Chart 2: Temperature and Humidity Monitoring."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Chart 2: Environmental Conditions Monitoring', fontsize=16, fontweight='bold')
    
    # Extract every 100th reading for clarity
    sample_readings = asset_readings[::100]
    indices = range(len(sample_readings))
    temperatures = [float(r['temperature']) for r in sample_readings]
    humidities = [float(r['humidity']) for r in sample_readings]
    
    # Temperature chart
    ax1.plot(indices, temperatures, marker='o', linestyle='-', linewidth=2, markersize=6, color='#e74c3c')
    ax1.axhline(y=25, color='green', linestyle='--', linewidth=2, label='Optimal (25°C)')
    ax1.fill_between(indices, 18, 30, alpha=0.2, color='green', label='Safe Range')
    ax1.set_title('Temperature Trend', fontweight='bold', pad=20)
    ax1.set_ylabel('Temperature (°C)', fontweight='bold')
    ax1.set_xlabel('Reading Index', fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Humidity chart
    ax2.plot(indices, humidities, marker='s', linestyle='-', linewidth=2, markersize=6, color='#3498db')
    ax2.axhline(y=55, color='green', linestyle='--', linewidth=2, label='Optimal (55%)')
    ax2.fill_between(indices, 40, 70, alpha=0.2, color='green', label='Safe Range')
    ax2.set_title('Humidity Trend', fontweight='bold', pad=20)
    ax2.set_ylabel('Humidity (%)', fontweight='bold')
    ax2.set_xlabel('Reading Index', fontweight='bold')
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('chart_02_environmental_conditions.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 2: Environmental Conditions - Created")
    plt.close()


def create_inventory_status_chart(inventory_readings):
    """Chart 3: Inventory Level Status Distribution."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Chart 3: Inventory Level Status and Distribution', fontsize=16, fontweight='bold')
    
    # Inventory level distribution
    level_counts = Counter(r['inventory_level'] for r in inventory_readings)
    colors = {'Optimal': '#2ecc71', 'Low': '#f39c12', 'Critical': '#e74c3c', 'Overstocked': '#3498db'}
    level_colors = [colors.get(level, '#95a5a6') for level in level_counts.keys()]
    ax1.bar(level_counts.keys(), level_counts.values(), color=level_colors, edgecolor='black', linewidth=1.5)
    ax1.set_title('Inventory Level Distribution', fontweight='bold', pad=20)
    ax1.set_ylabel('Number of Readings', fontweight='bold')
    ax1.set_xlabel('Inventory Level', fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    
    # Quantity distribution
    sample_readings = inventory_readings[::100]
    quantities = [int(r['quantity']) for r in sample_readings]
    indices = range(len(sample_readings))
    ax2.plot(indices, quantities, marker='D', linestyle='-', linewidth=2, markersize=6, color='#9b59b6')
    ax2.fill_between(indices, 0, quantities, alpha=0.3, color='#9b59b6')
    ax2.set_title('Inventory Quantity Trend', fontweight='bold', pad=20)
    ax2.set_ylabel('Quantity (Units)', fontweight='bold')
    ax2.set_xlabel('Reading Index', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('chart_03_inventory_status.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 3: Inventory Status - Created")
    plt.close()


def create_alert_analysis_chart(alerts):
    """Chart 4: Alert Analysis and Distribution."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Chart 4: System Alert Analysis', fontsize=16, fontweight='bold')
    
    # Alert type distribution
    alert_type_counts = Counter(a['alert_type'] for a in alerts)
    ax1.barh(list(alert_type_counts.keys()), list(alert_type_counts.values()), 
             color='#e74c3c', edgecolor='black', linewidth=1.5)
    ax1.set_title('Alert Type Distribution', fontweight='bold', pad=20)
    ax1.set_xlabel('Number of Alerts', fontweight='bold')
    
    # Severity distribution
    severity_counts = Counter(a['severity'] for a in alerts)
    colors_severity = {'CRITICAL': '#e74c3c', 'WARNING': '#f39c12', 'INFO': '#3498db'}
    severity_colors = [colors_severity.get(sev, '#95a5a6') for sev in severity_counts.keys()]
    ax2.pie(severity_counts.values(), labels=severity_counts.keys(), autopct='%1.1f%%',
            colors=severity_colors, startangle=90)
    ax2.set_title('Alert Severity Distribution', fontweight='bold', pad=20)
    
    # Alerts over time (sample every 50 alerts)
    sample_alerts = alerts[::50]
    alert_indices = range(len(sample_alerts))
    ax3.plot(alert_indices, range(len(sample_alerts)), marker='o', linestyle='-', 
             linewidth=2, markersize=6, color='#e74c3c')
    ax3.fill_between(alert_indices, 0, range(len(sample_alerts)), alpha=0.3, color='#e74c3c')
    ax3.set_title('Alert Accumulation Over Time', fontweight='bold', pad=20)
    ax3.set_ylabel('Cumulative Alerts', fontweight='bold')
    ax3.set_xlabel('Alert Index (sampled)', fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # Alert count by asset (top 10)
    asset_alert_counts = Counter(a['asset_id'] for a in alerts)
    top_assets = dict(sorted(asset_alert_counts.items(), key=lambda x: x[1], reverse=True)[:10])
    ax4.barh(list(top_assets.keys()), list(top_assets.values()), 
             color='#f39c12', edgecolor='black', linewidth=1.5)
    ax4.set_title('Top 10 Assets by Alert Count', fontweight='bold', pad=20)
    ax4.set_xlabel('Number of Alerts', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('chart_04_alert_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 4: Alert Analysis - Created")
    plt.close()


def create_signal_and_battery_chart(asset_readings):
    """Chart 5: Signal Strength and Battery Level Monitoring."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Chart 5: Device Signal Strength and Battery Monitoring', fontsize=16, fontweight='bold')
    
    # Sample readings
    sample_readings = asset_readings[::100]
    indices = range(len(sample_readings))
    signal_strengths = [int(r['signal_strength']) for r in sample_readings]
    battery_levels = [int(r['battery_level']) for r in sample_readings]
    
    # Signal strength
    ax1.plot(indices, signal_strengths, marker='o', linestyle='-', linewidth=2, markersize=6, color='#3498db')
    ax1.axhline(y=70, color='green', linestyle='--', linewidth=2, label='Good Signal (70%)')
    ax1.axhline(y=30, color='red', linestyle='--', linewidth=2, label='Weak Signal (30%)')
    ax1.fill_between(indices, 70, 100, alpha=0.2, color='green', label='Excellent Range')
    ax1.set_title('Signal Strength Trend', fontweight='bold', pad=20)
    ax1.set_ylabel('Signal Strength (%)', fontweight='bold')
    ax1.set_xlabel('Reading Index', fontweight='bold')
    ax1.set_ylim(0, 105)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Battery level
    ax2.plot(indices, battery_levels, marker='s', linestyle='-', linewidth=2, markersize=6, color='#2ecc71')
    ax2.axhline(y=20, color='red', linestyle='--', linewidth=2, label='Critical (20%)')
    ax2.fill_between(indices, 0, battery_levels, alpha=0.3, color='#2ecc71')
    ax2.set_title('Battery Level Trend', fontweight='bold', pad=20)
    ax2.set_ylabel('Battery Level (%)', fontweight='bold')
    ax2.set_xlabel('Reading Index', fontweight='bold')
    ax2.set_ylim(0, 105)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('chart_05_signal_battery.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 5: Signal and Battery - Created")
    plt.close()


def create_warehouse_performance_chart(analytics):
    """Chart 6: Warehouse Performance Metrics."""
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 2, figure=fig)
    fig.suptitle('Chart 6: Warehouse Performance Metrics Dashboard', fontsize=16, fontweight='bold')
    
    asset_stats = analytics['asset_statistics']
    inventory_stats = analytics['inventory_statistics']
    alert_stats = analytics['alert_statistics']
    
    # Asset status breakdown
    ax1 = fig.add_subplot(gs[0, 0])
    asset_status = {
        'In Warehouse': asset_stats['assets_in_warehouse'],
        'In Transit': asset_stats['assets_in_transit'],
        'Delivered': asset_stats['assets_delivered']
    }
    colors = ['#2ecc71', '#3498db', '#e74c3c']
    ax1.pie(asset_status.values(), labels=asset_status.keys(), autopct='%1.1f%%',
            colors=colors, startangle=90)
    ax1.set_title('Asset Status Breakdown', fontweight='bold', pad=20)
    
    # Inventory status breakdown
    ax2 = fig.add_subplot(gs[0, 1])
    inventory_status = {
        'Optimal': inventory_stats['optimal_items'],
        'Low Stock': inventory_stats['low_stock_items'],
        'Critical': inventory_stats['critical_items'],
        'Overstocked': inventory_stats['overstocked_items']
    }
    colors_inv = ['#2ecc71', '#f39c12', '#e74c3c', '#3498db']
    ax2.pie(inventory_status.values(), labels=inventory_status.keys(), autopct='%1.1f%%',
            colors=colors_inv, startangle=90)
    ax2.set_title('Inventory Status Breakdown', fontweight='bold', pad=20)
    
    # Environmental metrics
    ax3 = fig.add_subplot(gs[1, 0])
    metrics = ['Avg Temp\n(°C)', 'Avg Humidity\n(%)', 'Avg Signal\n(%)', 'Avg Battery\n(%)']
    values = [
        asset_stats['avg_temperature'],
        asset_stats['avg_humidity'],
        asset_stats['avg_signal_strength'],
        asset_stats['avg_battery_level']
    ]
    colors_metrics = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
    bars = ax3.bar(metrics, values, color=colors_metrics, edgecolor='black', linewidth=1.5)
    ax3.set_title('Environmental Metrics', fontweight='bold', pad=20)
    ax3.set_ylabel('Value', fontweight='bold')
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f}', ha='center', va='bottom', fontweight='bold')
    
    # Alert metrics
    ax4 = fig.add_subplot(gs[1, 1])
    alert_types = ['Total\nAlerts', 'Critical\nAlerts', 'Warning\nAlerts']
    alert_values = [
        alert_stats['total_alerts'],
        alert_stats['critical_alerts'],
        alert_stats['warning_alerts']
    ]
    colors_alerts = ['#e74c3c', '#c0392b', '#f39c12']
    bars = ax4.bar(alert_types, alert_values, color=colors_alerts, edgecolor='black', linewidth=1.5)
    ax4.set_title('Alert Summary', fontweight='bold', pad=20)
    ax4.set_ylabel('Count', fontweight='bold')
    for bar, val in zip(bars, alert_values):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('chart_06_warehouse_performance.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 6: Warehouse Performance - Created")
    plt.close()


def create_comprehensive_dashboard(asset_readings, inventory_readings, alerts, analytics):
    """Chart 7: Comprehensive System Dashboard."""
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)
    fig.suptitle('Chart 7: Comprehensive Smart Asset Tracking System Dashboard', 
                 fontsize=18, fontweight='bold', y=0.995)
    
    # 1. Asset Status (top-left)
    ax1 = fig.add_subplot(gs[0, 0])
    status_counts = Counter(r['status'] for r in asset_readings)
    ax1.pie(status_counts.values(), labels=status_counts.keys(), autopct='%1.0f%%',
            colors=['#2ecc71', '#3498db', '#e74c3c', '#f39c12', '#95a5a6'], textprops={'fontsize': 8})
    ax1.set_title('Asset Status', fontweight='bold', fontsize=10)
    
    # 2. Location Distribution (top-middle)
    ax2 = fig.add_subplot(gs[0, 1])
    location_counts = Counter(r['location'] for r in asset_readings)
    ax2.barh(list(location_counts.keys()), list(location_counts.values()), 
             color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'], edgecolor='black', linewidth=1)
    ax2.set_title('Asset Locations', fontweight='bold', fontsize=10)
    ax2.set_xlabel('Count', fontsize=8)
    
    # 3. Temperature Distribution (top-right)
    ax3 = fig.add_subplot(gs[0, 2])
    temperatures = [float(r['temperature']) for r in asset_readings]
    ax3.hist(temperatures, bins=20, color='#e74c3c', edgecolor='black', alpha=0.7)
    ax3.axvline(np.mean(temperatures), color='green', linestyle='--', linewidth=2, label='Mean')
    ax3.set_title('Temperature Distribution', fontweight='bold', fontsize=10)
    ax3.set_xlabel('Temp (°C)', fontsize=8)
    ax3.set_ylabel('Frequency', fontsize=8)
    ax3.legend(fontsize=7)
    
    # 4. Humidity Distribution (middle-left)
    ax4 = fig.add_subplot(gs[1, 0])
    humidities = [float(r['humidity']) for r in asset_readings]
    ax4.hist(humidities, bins=20, color='#3498db', edgecolor='black', alpha=0.7)
    ax4.axvline(np.mean(humidities), color='green', linestyle='--', linewidth=2, label='Mean')
    ax4.set_title('Humidity Distribution', fontweight='bold', fontsize=10)
    ax4.set_xlabel('Humidity (%)', fontsize=8)
    ax4.set_ylabel('Frequency', fontsize=8)
    ax4.legend(fontsize=7)
    
    # 5. Inventory Status (middle-middle)
    ax5 = fig.add_subplot(gs[1, 1])
    level_counts = Counter(r['inventory_level'] for r in inventory_readings)
    colors_inv = {'Optimal': '#2ecc71', 'Low': '#f39c12', 'Critical': '#e74c3c', 'Overstocked': '#3498db'}
    inv_colors = [colors_inv.get(level, '#95a5a6') for level in level_counts.keys()]
    ax5.bar(range(len(level_counts)), list(level_counts.values()), color=inv_colors, edgecolor='black', linewidth=1)
    ax5.set_xticks(range(len(level_counts)))
    ax5.set_xticklabels(list(level_counts.keys()), fontsize=8, rotation=45)
    ax5.set_title('Inventory Levels', fontweight='bold', fontsize=10)
    ax5.set_ylabel('Count', fontsize=8)
    
    # 6. Alert Severity (middle-right)
    ax6 = fig.add_subplot(gs[1, 2])
    severity_counts = Counter(a['severity'] for a in alerts)
    colors_sev = {'CRITICAL': '#e74c3c', 'WARNING': '#f39c12', 'INFO': '#3498db'}
    sev_colors = [colors_sev.get(sev, '#95a5a6') for sev in severity_counts.keys()]
    ax6.pie(severity_counts.values(), labels=severity_counts.keys(), autopct='%1.0f%%',
            colors=sev_colors, textprops={'fontsize': 8})
    ax6.set_title('Alert Severity', fontweight='bold', fontsize=10)
    
    # 7. Signal Strength (bottom-left)
    ax7 = fig.add_subplot(gs[2, 0])
    signal_strengths = [int(r['signal_strength']) for r in asset_readings[::100]]
    ax7.plot(range(len(signal_strengths)), signal_strengths, marker='o', linestyle='-', 
             linewidth=1.5, markersize=4, color='#3498db')
    ax7.axhline(y=70, color='green', linestyle='--', linewidth=1, alpha=0.7)
    ax7.set_title('Signal Strength Trend', fontweight='bold', fontsize=10)
    ax7.set_ylabel('Signal (%)', fontsize=8)
    ax7.set_xlabel('Reading', fontsize=8)
    ax7.grid(True, alpha=0.3)
    
    # 8. Battery Level (bottom-middle)
    ax8 = fig.add_subplot(gs[2, 1])
    battery_levels = [int(r['battery_level']) for r in asset_readings[::100]]
    ax8.plot(range(len(battery_levels)), battery_levels, marker='s', linestyle='-', 
             linewidth=1.5, markersize=4, color='#2ecc71')
    ax8.axhline(y=20, color='red', linestyle='--', linewidth=1, alpha=0.7)
    ax8.set_title('Battery Level Trend', fontweight='bold', fontsize=10)
    ax8.set_ylabel('Battery (%)', fontsize=8)
    ax8.set_xlabel('Reading', fontsize=8)
    ax8.grid(True, alpha=0.3)
    
    # 9. Alert Types (bottom-right)
    ax9 = fig.add_subplot(gs[2, 2])
    alert_type_counts = Counter(a['alert_type'] for a in alerts)
    ax9.barh(list(alert_type_counts.keys()), list(alert_type_counts.values()), 
             color='#e74c3c', edgecolor='black', linewidth=1)
    ax9.set_title('Alert Types', fontweight='bold', fontsize=10)
    ax9.set_xlabel('Count', fontsize=8)
    
    plt.savefig('chart_07_comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
    print("✓ Chart 7: Comprehensive Dashboard - Created")
    plt.close()


def main():
    """Main entry point."""
    print("\n" + "="*80)
    print("GENERATING PROFESSIONAL VISUALIZATIONS")
    print("Smart Asset Tracking and Inventory Monitoring System")
    print("="*80)
    
    asset_readings, inventory_readings, alerts, analytics = load_data()
    
    if asset_readings is None:
        return
    
    create_asset_tracking_chart(asset_readings)
    create_environmental_conditions_chart(asset_readings)
    create_inventory_status_chart(inventory_readings)
    create_alert_analysis_chart(alerts)
    create_signal_and_battery_chart(asset_readings)
    create_warehouse_performance_chart(analytics)
    create_comprehensive_dashboard(asset_readings, inventory_readings, alerts, analytics)
    
    print("\n" + "="*80)
    print("✓ ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
    print("="*80)
    print("\nGenerated files:")
    print("  1. chart_01_asset_tracking.png")
    print("  2. chart_02_environmental_conditions.png")
    print("  3. chart_03_inventory_status.png")
    print("  4. chart_04_alert_analysis.png")
    print("  5. chart_05_signal_battery.png")
    print("  6. chart_06_warehouse_performance.png")
    print("  7. chart_07_comprehensive_dashboard.png")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
