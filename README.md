# Universal-Serial-Adapter

## Hackable USB-C UART RS232 Adapter

The **Universal Serial Adapter** is an open-source hardware project designed to bridge USB-C, RS232, and TTL communication. This fully assembled adapter is packed with features tailored for advanced prototyping, embedded development, and system debugging.  

Make one yourself or <a href="https://www.imania.dk/product_info.php?cPath=204&products_id=7224&language=en">buy one here</a>

<img src="./photos/Universal Serial Adapter-main.jpeg"/>

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
git clone https://github.com/AndersBNielsen/Universal-Serial-Adapter.git  
```
## Getting a PCB
This project is kindly sponsored by JLCPCB. They offer cheap, professional looking PCBs and super fast delivery.

Step 1: Get the gerber file zip package from the /hardware folder

Step 2: Upload to JLCPCB [https://jlcpcb.com](https://jlcpcb.com/?from=Anders_N)

<img src="https://github.com/AndersBNielsen/65uino/blob/main/images/upload.png?raw=true" alt="Upload" style="width: 220px;">

Step 3: Pick your color, surface finish and order.

<img src="https://github.com/AndersBNielsen/65uino/blob/main/images/settings.png?raw=true" alt="Select settings" style="width: 220px;">

<img src="https://github.com/AndersBNielsen/65uino/blob/main/images/save.png?raw=true" alt="Save your choice" style="width: 220px;">

If you want JLCPCB to assemble a board, the BOM and placement files are also in the repo. 

You can use these affiliate links to get a board for $2 and also get $80 worth of New User Coupons at: https://jlcpcb.com/?from=Anders_N

And in case you also want to order a 3D-printed case you can use this link. 
How to Get a $7 3D Printing Coupon: https://jlc3dp.com/?from=Anders_N
