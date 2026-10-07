# Smart Asset Tracking and Inventory Monitoring System

## Project Overview

This project implements a comprehensive **IoT-Based Smart Asset Tracking and Inventory Monitoring System** for warehouses and logistics management. The system provides real-time monitoring of asset locations, inventory levels, and environmental conditions using IoT technologies. It enables organizations to optimize warehouse operations, reduce losses, and improve logistics efficiency.

## Project Objectives

- Design and implement a smart asset tracking system using IoT concepts and Python
- Integrate multiple tracking sensors for continuous monitoring of warehouse conditions
- Develop automated inventory level assessment and anomaly detection algorithms
- Create comprehensive data logging and analysis mechanisms
- Implement scalable system architecture for multi-warehouse deployments
- Support early detection of asset loss and inventory anomalies

## System Features

### Core Monitoring Capabilities
- **Asset Location Tracking**: Continuous GPS and RFID-based location monitoring
- **Asset Status Monitoring**: Real-time status tracking (In Warehouse, In Transit, Delivered)
- **Environmental Monitoring**: Temperature and humidity tracking
- **Signal Strength Monitoring**: RFID/GPS signal quality assessment
- **Battery Level Monitoring**: Tracker battery status and alerts
- **Inventory Level Tracking**: Real-time stock quantity monitoring
- **Anomaly Detection**: Automated detection of temperature, signal, and battery anomalies

### Inventory Status Classification
- **OPTIMAL**: Inventory at ideal levels for operational efficiency
- **LOW**: Stock approaching reorder point, action recommended
- **CRITICAL**: Stock at or below critical threshold, immediate action required
- **OVERSTOCKED**: Excess inventory, potential storage optimization needed

### Alert System
- **Low Stock Alerts**: When inventory falls below reorder point
- **Temperature Anomalies**: When temperature deviates from safe range
- **Signal Strength Alerts**: When RFID/GPS signal becomes weak
- **Battery Alerts**: When device battery reaches critical levels
- **Location Anomalies**: When assets are in unexpected locations

### System Components
- **AssetTracker**: Simulates asset tracking with location, status, and environmental data
- **InventoryManager**: Manages inventory levels and stock movements
- **AlertGenerator**: Generates alerts based on system conditions
- **WarehouseAnalytics**: Analyzes warehouse and logistics data
- **SmartAssetTrackingSystem**: Central controller orchestrating all components

### Performance Metrics
- **Total Asset Readings**: 20,000 tracking data points
- **Total Inventory Readings**: 15,000 inventory status updates
- **Total Alerts Generated**: 28,274 system alerts
- **Critical Alerts**: 6,546 (23.2%)
- **Warning Alerts**: 21,728 (76.8%)

## Simulation Results

### Asset Tracking Statistics (1000 Cycles)
- **Average Temperature**: 21.93°C (Range: 15-35°C)
- **Average Humidity**: 54.57% (Range: 20-80%)
- **Average Signal Strength**: 81.86% (Range: 10-100%)
- **Average Battery Level**: 2.94% (declining due to simulation duration)
- **Assets In Warehouse**: 11,214 readings (56.1%)
- **Assets In Transit**: 6,016 readings (30.1%)
- **Assets Delivered**: 2,770 readings (13.9%)

### Inventory Statistics
- **Total Inventory Items**: 15 distinct items
- **Total Quantity Tracked**: 79,507,268 units (across all readings)
- **Average Quantity per Item**: 5,300.48 units
- **Optimal Stock Items**: 61 readings
- **Overstocked Items**: 14,939 readings

### Alert Statistics
- **Temperature Anomaly Alerts**: 6,546 (23.2%)
- **Location/Signal Alerts**: 2,858 (10.1%)
- **Low Stock Alerts**: 0 (0.0%)
- **Critical Severity**: 6,546 alerts
- **Warning Severity**: 21,728 alerts

## File Structure

```
smart_asset_tracking_report/
├── smart_asset_tracking.py              # Main simulation engine (600+ lines)
├── generate_visualizations.py           # Chart generation script (500+ lines)
├── generate_report.py                   # Word document generator (400+ lines)
├── asset_tracking_readings.csv          # Asset tracking data (CSV format)
├── inventory_readings.csv               # Inventory data (CSV format)
├── system_alerts.csv                    # Alert event log
├── warehouse_analytics.json             # Simulation data (JSON format)
├── chart_01_asset_tracking.png          # Visualization
├── chart_02_environmental_conditions.png # Visualization
├── chart_03_inventory_status.png        # Visualization
├── chart_04_alert_analysis.png          # Visualization
├── chart_05_signal_battery.png          # Visualization
├── chart_06_warehouse_performance.png   # Visualization
├── chart_07_comprehensive_dashboard.png # Visualization
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
└── IoT_Smart_Asset_Tracking_Internship_Report.docx # Final report (30+ pages)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Extract the project files**:
   ```bash
   unzip iot_smart_asset_tracking_code.zip
   cd smart_asset_tracking_report
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install python-docx matplotlib numpy
   ```

## Usage

### Run the Complete Simulation

Execute the main simulation to generate asset tracking data:
```bash
python3 smart_asset_tracking.py
```

This will:
- Run 1000 monitoring cycles
- Generate 20,000 asset tracking readings
- Generate 15,000 inventory readings
- Create 28,274 system alerts
- Export data to CSV and JSON formats
- Display comprehensive statistics

### Generate Visualizations

Create professional charts from the simulation data:
```bash
python3 generate_visualizations.py
```

This will generate 7 high-resolution visualization files:
1. Asset Tracking Status (Status and Location Distribution)
2. Environmental Conditions (Temperature and Humidity Trends)
3. Inventory Status (Level Distribution and Quantity Trends)
4. Alert Analysis (Type, Severity, and Accumulation)
5. Signal and Battery (Device Health Monitoring)
6. Warehouse Performance Dashboard (Key Metrics Summary)
7. Comprehensive System Dashboard (9-panel overview)

### Generate the Report

Create the final Word document report:
```bash
python3 generate_report.py
```

This will generate `IoT_Smart_Asset_Tracking_Internship_Report.docx` containing:
- Executive Summary with learning objectives and outcomes
- Organization Overview
- Introduction to IoT and Asset Tracking
- Problem Assessment and Requirements Analysis
- Solution Design and System Architecture
- Solution Development, Python Implementation, and Testing
- Results and Performance Evaluation with 7 embedded visualizations
- Conclusion and Future Scope
- References

## System Architecture

### Monitoring Cycle Flow
```
Track Assets → Monitor Inventory → Analyze Conditions → Generate Alerts → Log Data → Export Results
```

### Data Processing Pipeline
```
Trackers → AlertGenerator → WarehouseAnalytics → Data Logger → CSV/JSON Export
```

### Decision Logic
```
Asset Location + Status + Environment → Anomaly Detection
Inventory Quantity + Reorder Point → Stock Level Classification
Temperature + Signal + Battery → Alert Generation
```

## Environmental Thresholds

### Temperature (°C)
- Optimal: 20-25°C
- Acceptable: 15-30°C
- Warning: <15 or >30°C
- Critical: <10 or >35°C

### Humidity (%)
- Optimal: 40-60%
- Acceptable: 30-70%
- Warning: <30% or >70%
- Critical: <20% or >80%

### Signal Strength (%)
- Excellent: 70-100%
- Good: 50-70%
- Fair: 30-50%
- Poor: <30%

### Battery Level (%)
- Excellent: 80-100%
- Good: 50-80%
- Fair: 20-50%
- Critical: <20%

## Configuration

### Modifying Environmental Thresholds

Edit `smart_asset_tracking.py` to adjust alert thresholds:

```python
alert_generator = AlertGenerator()
# Modify threshold values in AlertGenerator class methods
```

### Adjusting Simulation Parameters

Modify the number of monitoring cycles:

```python
system = SmartAssetTrackingSystem("WH_001")
system.initialize_assets(20)
system.initialize_inventory(15)
system.run_simulation(num_cycles=2000)  # Change cycle count
```

### Changing Baseline Sensor Values

Adjust initial sensor readings:

```python
tracker = AssetTracker("AST_001", "Asset Name")
tracker.temperature = 25.0  # Set initial temperature
tracker.gps_latitude = 28.6139  # Set initial latitude
tracker.gps_longitude = 77.2090  # Set initial longitude
```

## Output Files

### Data Files
- **asset_tracking_readings.csv**: All asset readings with timestamps and status
- **inventory_readings.csv**: All inventory readings with stock levels
- **system_alerts.csv**: Detailed log of all generated alerts
- **warehouse_analytics.json**: Complete simulation data with statistics

### Visualization Files
- **chart_*.png**: High-resolution (300 DPI) professional charts

### Report File
- **IoT_Smart_Asset_Tracking_Internship_Report.docx**: Comprehensive 30+ page internship report

## Performance Metrics Explained

### Asset Tracking Efficiency
Measures the system's ability to maintain accurate location and status information for all tracked assets. Higher efficiency indicates better real-time visibility and faster response times.

### Inventory Accuracy
Evaluates the system's accuracy in tracking inventory levels and predicting stock needs. Calculated by comparing predicted stock levels against actual consumption patterns.

### Alert Responsiveness
Measures the system's ability to generate timely alerts for anomalies. Higher scores indicate faster detection and notification of critical conditions.

## Real-World Deployment Considerations

### Hardware Integration
- **Tracking Devices**: RFID readers, GPS trackers, BLE beacons
- **Environmental Sensors**: Temperature/humidity sensors, light sensors
- **Edge Computing**: Raspberry Pi or industrial edge gateways
- **Communication**: Wi-Fi, LoRaWAN, or cellular connectivity
- **Power**: Mains-powered with battery backup for critical systems

### Cloud Platform
- Real-time data ingestion via MQTT or REST APIs
- Secure data storage with encryption
- Machine learning for predictive analytics
- Mobile and web dashboards for stakeholders

### Security Measures
- End-to-end encryption for all communications
- Secure authentication and authorization
- Regular security audits and updates
- Compliance with logistics data protection standards

## Future Enhancements

1. **Machine Learning Integration**: Predictive demand forecasting and anomaly detection
2. **Advanced Sensors**: Shock sensors, pressure sensors, light sensors
3. **Mobile Applications**: Native iOS and Android apps for warehouse staff
4. **Cloud Integration**: Real-time data sync with ERP and WMS systems
5. **Blockchain Security**: Immutable audit logs for supply chain transparency
6. **Route Optimization**: Automated routing for efficient warehouse operations
7. **Multi-Warehouse Management**: Centralized control of multiple facilities
8. **Predictive Maintenance**: Equipment maintenance alerts based on usage patterns

## Troubleshooting

### Issue: ImportError for matplotlib or numpy
**Solution**: Install missing packages:
```bash
pip install matplotlib numpy python-docx
```

### Issue: CSV or JSON files not found
**Solution**: Ensure you've run the main simulation first:
```bash
python3 smart_asset_tracking.py
```

### Issue: Charts not generating
**Solution**: Verify matplotlib installation and check file permissions:
```bash
pip install --upgrade matplotlib
```

## Performance Optimization Tips

1. **For Large Datasets**: Increase simulation cycles for more comprehensive analysis
2. **For Real-time Processing**: Implement streaming data processing with message queues
3. **For Cloud Deployment**: Use containerization (Docker) and orchestration (Kubernetes)
4. **For ML Integration**: Prepare data in batches for model training

## Code Quality

The codebase follows professional Python standards:
- Object-oriented design with clear separation of concerns
- Comprehensive docstrings for all classes and methods
- Type hints for improved code clarity
- Modular architecture enabling easy extension
- Extensive error handling and validation

## References

- Python Documentation: https://docs.python.org/3/
- Matplotlib Documentation: https://matplotlib.org/
- IoT in Smart Logistics: https://ieeexplore.ieee.org/
- Supply Chain Technologies: https://www.researchgate.net/
- Warehouse Management Systems: https://www.sciencedirect.com/

## Support and Contact

For questions, issues, or suggestions regarding this project, please refer to the comprehensive documentation in the internship report or contact the development team.

## License

This project is provided for educational and research purposes as part of an internship program.

## Acknowledgments

This project was developed as part of an internship program focused on IoT technologies and intelligent logistics systems. The work demonstrates the practical application of IoT principles in solving real-world warehouse and supply chain challenges, supporting efficient and sustainable logistics operations.

---

**Project Status**: Completed ✓
**Last Updated**: July 13, 2026
**Version**: 1.0
**Total Lines of Code**: 1500+
**Simulation Cycles**: 1000
**Asset Readings**: 20,000
**Inventory Readings**: 15,000
**Alerts Generated**: 28,274
**Visualizations**: 7 professional charts
**Report Pages**: 30+
