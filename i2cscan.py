# scan for I2C devices and read the Part ID register to identify the sensor variant

from machine import Pin, SoftI2C

i2c = SoftI2C(sda=Pin(10),  # Here, use your I2C SDA pin (GP.. number, so this is GP10)
                  scl=Pin(11),  # Here, use your I2C SCL pin (GP.. number)
                  freq=400000)  # Fast: 400kHz, slow: 100kHz

print("Starting I2C scan...")
scan_results = i2c.scan()
print(scan_results)

I2C_ADDR = 0x57
REG_PART_ID = 0xFF

# determine the sensor address by getting the result of the I2C scan
for addr in scan_results:
    print(f"Device found at I2C address: {hex(addr)}")
    I2C_ADDR = addr

print(f"Using I2C address: {hex(I2C_ADDR)} to read Part ID...")

# Read 1 byte from the Part ID register (0xFF)
part_id_bytes = i2c.readfrom_mem(I2C_ADDR, REG_PART_ID, 1)
part_id = part_id_bytes[0]

print(f"Part ID read: {hex(part_id)}")

# Match the Hex value to determine the specific variant
if part_id == 0x15:
    print( f"MAX30102 Detected (ID: {hex(part_id)})" )
elif part_id == 0x11:
    print( f"MAX30100 Detected (ID: {hex(part_id)})" )
elif part_id == 0x25:
    print( f"MAX30105 Detected (ID: {hex(part_id)})" )
else:
    print( f"Unknown sensor variant found (ID: {hex(part_id)})" )
