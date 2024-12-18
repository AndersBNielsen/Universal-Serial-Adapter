#!/bin/python3
import serial
import serial.tools.list_ports
import time
import random
import sys

# Constants
#BAUD_RATES = [9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600, 1500000, 2000000]  # Test baud rates
BAUD_RATES = [57600, 115200, 230400, 460800, 921600, 1500000, 2000000, 3000000]  # Test baud rates
BLOCK_SIZE = 1024  # 1KB of data

def detect_serial_ports():
    """Detect serial ports starting with 'cu.usbserial'."""
    ports = [port.device for port in serial.tools.list_ports.comports() if "cu.usbserial" in port.device]
    if len(ports) < 2:
        print("Error: At least two 'cu.usbserial' ports are required.")
        sys.exit(1)
    return ports[0], ports[1]

def generate_random_data(size):
    """Generate a block of random data."""
    return bytearray(random.getrandbits(8) for _ in range(size))

def test_baud_rate(tx_port, rx_port, baud_rate, data):
    """Test a given baud rate by sending and receiving a block of data."""
    try:
        with serial.Serial(tx_port, baud_rate, timeout=2) as tx_ser, \
             serial.Serial(rx_port, baud_rate, timeout=2) as rx_ser:
            print(f"Testing baud rate: {baud_rate} bps")

            # Clear buffers
            tx_ser.reset_input_buffer()
            tx_ser.reset_output_buffer()
            rx_ser.reset_input_buffer()
            rx_ser.reset_output_buffer()

            # Send data
            start_time = time.time()
            tx_ser.write(data)
            tx_ser.flush()  # Ensure all data is sent

            # Receive data
            received_data = rx_ser.read(len(data))
            end_time = time.time()

            # Check for errors
            errors = sum(1 for a, b in zip(data, received_data) if a != b)
            elapsed_time = end_time - start_time
            throughput = (len(data) * 8) / elapsed_time if elapsed_time > 0 else 0  # Bits per second

            print(f"  Data size: {len(data)} bytes")
            print(f"  Time taken: {elapsed_time:.2f} seconds")
            print(f"  Throughput: {throughput:.2f} bps")
            print(f"  Errors: {errors}\n")
            return errors == 0

    except serial.SerialException as e:
        print(f"Serial error at baud rate {baud_rate}: {e}")
        return False

if __name__ == "__main__":
    # Auto-detect serial ports
    tx_port, rx_port = detect_serial_ports()
    print(f"Detected TX port: {tx_port}")
    print(f"Detected RX port: {rx_port}")

    # Generate random data
    random_data = generate_random_data(BLOCK_SIZE)

    print("\nStarting serial link test...\n")
    for baud_rate in BAUD_RATES:
        success = test_baud_rate(tx_port, rx_port, baud_rate, random_data)
        if not success:
            print(f"Test failed at baud rate {baud_rate}.")
            sys.exit(1)

    print("All baud rates tested successfully!")
