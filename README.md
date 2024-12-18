# Universal-Serial-Adapter

 Hackable USB-C UART RS232 Adapter

# **Universal Serial Adapter**  

The **Universal Serial Adapter** is an open-source hardware project designed to bridge USB-C, RS232, and TTL communication. This fully assembled adapter is packed with features tailored for advanced prototyping, embedded development, and system debugging.  



## **Technical Summary**  

### **Key Features**  
- **USB-C to RS232 Interface**  
  - USB-C (female) connector to DSUB9 RS232 (male) port.  
  - Supports bidirectional communication between modern USB-C devices and RS232 hardware.  

- **TTL Signal Breakouts**  
  - TTL RX, TX, and control signal pins exposed for easy interfacing with UART-based systems.  

- **Signal Polarity Configuration**  
  - RS232 RX, TX, and control signals configurable using 2.54mm header jumpers:  
    - **Horizontal jumper placement**: Straight connection.  
    - **Vertical jumper placement**: Crossed connection.  

- **USB-C Line Breakouts**  
  - Access to USB-C data lines for advanced custom applications.  

- **3.3V Linear Regulator**  
  - Integrated 3.3V linear regulator for powering external circuits.  

### **Core Components**  
- **WCH CH340G**: USB-to-UART bridge IC for reliable USB communication.  
- **SP3243**: TTL-to-RS232 transceiver IC for robust RS232 signaling.  

### **Customization and Modifications**  
- Advanced features such as additional breakout options or alternate configurations may require soldering or cutting traces on the PCB.  
- Preinstalled components include:  
  - USB-C connector  
  - DSUB9 RS232 connector  
  - UART header  
  - Configuration jumper blocks  
- Open to further modification for specific use cases.  

### **Open-Source Design**  
- Designed in **KiCAD 8**, with all source files available for inspection and modification.  
- Licensed under an open-source hardware license, encouraging collaboration and adaptation.  
- Repository includes:  
  - KiCAD design files.  
  - PCB layout and schematics.  
  - Bill of Materials (BOM).  

### **Applications**  
- Embedded system development.  
- Debugging and diagnostics of RS232 hardware.  
- Bridging modern USB-C devices to legacy RS232 systems.  

## **Repository Contents**  
- **/hardware/**: KiCAD project files for the PCB.  

## **Important Notes**  
- This adapter is a professional-grade tool and may require advanced soldering and modification skills for some features.  
- Enclosures, cables, and other accessories are not included.  

## **Get Started**  
Clone or download the repository to start customizing:  
```bash  
git clone https://github.com/<your-repo-name>/UniversalSerialAdapter.git  
```