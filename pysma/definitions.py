"""Sensor definitions for SMA WebConnect library for Python."""
from .const import (
    DEVCLASS_BATTERY,
    DEVCLASS_ENERGY_METER,
    DEVCLASS_INVERTER,
    DEVICE_INFO,
    ENERGY_METER_VIA_INVERTER,
    JMESPATHS_TAG,
    OPTIMIZERS_VIA_INVERTER,
)
from .sensor import Sensor

# Status - Operation
#: Status of the device
status = Sensor("6180_08214800", "status", path=JMESPATHS_TAG, l10n_translate=True)
#: General operating status
operating_status_general = Sensor(
    "6180_08412800",
    "operating_status_general",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)

# Status - Operation - Inverter
#: General operating status
inverter_condition = Sensor(
    "6180_08414C00",
    "inverter_condition",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)
#: Inverter Condition
inverter_system_init = Sensor(
    "6800_08811F00",
    "inverter_system_init",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)
#: Grid connection status
grid_connection_status = Sensor(
    "6180_0846A700",
    "grid_connection_status",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)
#: Grid relay status
grid_relay_status = Sensor(
    "6180_08416400",
    "grid_relay_status",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)

# DC side - DC measurements PV
#: Current power generated by the solar panels (A side)
pv_power_a = Sensor("6380_40251E00_0", "pv_power_a", unit="W")
#: Current power generated by the solar panels (B side)
pv_power_b = Sensor("6380_40251E00_1", "pv_power_b", unit="W")
#: Current power generated by the solar panels (C side)
pv_power_c = Sensor("6380_40251E00_2", "pv_power_c", unit="W", enabled=False)
#: Current voltage generated by the solar panels (A side)
pv_voltage_a = Sensor(
    "6380_40451F00_0", "pv_voltage_a", unit="V", factor=100, enabled=False
)
#: Current voltage generated by the solar panels (B side)
pv_voltage_b = Sensor(
    "6380_40451F00_1", "pv_voltage_b", unit="V", factor=100, enabled=False
)
#: Current voltage generated by the solar panels (C side)
pv_voltage_c = Sensor(
    "6380_40451F00_2", "pv_voltage_c", unit="V", factor=100, enabled=False
)
#: Current amperage generated by the solar panels (A side)
pv_current_a = Sensor("6380_40452100_0", "pv_current_a", unit="A", factor=1000)
#: Current amperage generated by the solar panels (B side)
pv_current_b = Sensor("6380_40452100_1", "pv_current_b", unit="A", factor=1000)
#: Current amperage generated by the solar panels (C side)
pv_current_c = Sensor(
    "6380_40452100_2", "pv_current_c", unit="A", factor=1000, enabled=False
)

# DC Side - Insulation monitoring
#: Insulation residual current
insulation_residual_current = Sensor(
    "6102_40254E00", "insulation_residual_current", unit="mA", enabled=False
)

# AC Side - Grid measurements
#: Power supplied to the grid. grid_power = power_l1 + power_l2 + power_l3
grid_power = Sensor("6100_40263F00", "grid_power", unit="W")
#: Grid frequency
frequency = Sensor("6100_00465700", "frequency", unit="Hz", factor=100, enabled=False)

# AC Side - Grid measurements - Active power
#: Power for phase 1
power_l1 = Sensor("6100_40464000", "power_l1", unit="W", enabled=False)
#: Power for phase 2
power_l2 = Sensor("6100_40464100", "power_l2", unit="W", enabled=False)
#: Power for phase 3
power_l3 = Sensor("6100_40464200", "power_l3", unit="W", enabled=False)

# AC Side - Grid measurements - Reactive power
#: Total Reactive Power
grid_reactive_power = Sensor(
    "6100_40265F00", "grid_reactive_power", unit="var", enabled=False
)
#: Reactive Power for phase 1
grid_reactive_power_l1 = Sensor(
    "6100_40666000", "grid_reactive_power_l1", unit="var", enabled=False
)
#: Reactive Power for phase 2
grid_reactive_power_l2 = Sensor(
    "6100_40666100", "grid_reactive_power_l2", unit="var", enabled=False
)
#: Reactive Power for phase 3
grid_reactive_power_l3 = Sensor(
    "6100_40666200", "grid_reactive_power_l3", unit="var", enabled=False
)

# AC Side - Grid measurements - Apparent power
#: Total Apparent Power
grid_apparent_power = Sensor(
    "6100_40666700", "grid_apparent_power", unit="VA", enabled=False
)
#: Apparent Power for phase 1
grid_apparent_power_l1 = Sensor(
    "6100_40666800", "grid_apparent_power_l1", unit="VA", enabled=False
)
#: Apparent Power for phase 2
grid_apparent_power_l2 = Sensor(
    "6100_40666900", "grid_apparent_power_l2", unit="VA", enabled=False
)
#: Apparent Power for phase 3
grid_apparent_power_l3 = Sensor(
    "6100_40666A00", "grid_apparent_power_l3", unit="VA", enabled=False
)


# AC Side - Grid measurements - Power factor
#: Grid Power factor
grid_power_factor = Sensor(
    "6100_00665900", "grid_power_factor", unit="", factor=1000, enabled=False
)
#: Grid Power factor excitation
grid_power_factor_excitation = Sensor(
    "6180_08465A00",
    "grid_power_factor_excitation",
    path=JMESPATHS_TAG,
    l10n_translate=True,
    enabled=False,
)

# AC Side - Grid measurements - Phase Current
#: Current for phase 1
current_l1 = Sensor("6100_40465300", "current_l1", unit="A", factor=1000, enabled=False)
#: Current for phase 2
current_l2 = Sensor("6100_40465400", "current_l2", unit="A", factor=1000, enabled=False)
#: Current for phase 3
current_l3 = Sensor("6100_40465500", "current_l3", unit="A", factor=1000, enabled=False)
#: Total Current
current_total = Sensor("6100_00664F00", "current_total", unit="A", factor=1000)

# AC Side - Grid measurements - Phase voltage
#: Voltage for phase 1
voltage_l1 = Sensor("6100_00464800", "voltage_l1", unit="V", factor=100, enabled=False)
#: Voltage for phase 2
voltage_l2 = Sensor("6100_00464900", "voltage_l2", unit="V", factor=100, enabled=False)
#: Voltage for phase 3
voltage_l3 = Sensor("6100_00464A00", "voltage_l3", unit="V", factor=100, enabled=False)

# AC Side - Measured values - energy
#: Total power yield from a solar installation
total_yield = Sensor("6400_00260100", "total_yield", unit="kWh", factor=1000)
#: The solar plant's yield for today
daily_yield = Sensor("6400_00262200", "daily_yield", unit="Wh")

# AC Side - Measured values - Grid measurements
#: Power supplied to grid measured by energy meter
metering_power_supplied = Sensor("6100_40463600", "metering_power_supplied", unit="W")
#: Power absorbed fromgrid measured by energy meter
metering_power_absorbed = Sensor("6100_40463700", "metering_power_absorbed", unit="W")
#: Grid frequency measured by energy meter
metering_frequency = Sensor(
    "6100_00468100", "metering_frequency", unit="Hz", factor=100
)
#: Total power supplied to the grid measured by energy meter
metering_total_yield = Sensor(
    "6400_00462400", "metering_total_yield", unit="kWh", factor=1000
)
#: Total power from the grid measured by energy meter
metering_total_absorbed = Sensor(
    "6400_00462500", "metering_total_absorbed", unit="kWh", factor=1000
)

# AC Side - Measured values - Phase currents
#: Current for phase 1 measured by energy meter
metering_current_l1 = Sensor(
    "6100_40466500", "metering_current_l1", unit="A", factor=1000
)
#: Current for phase 2 measured by energy meter
metering_current_l2 = Sensor(
    "6100_40466600", "metering_current_l2", unit="A", factor=1000
)
#: Current for phase 3 measured by energy meter
metering_current_l3 = Sensor(
    "6100_40466B00", "metering_current_l3", unit="A", factor=1000
)

# AC Side - Measured values - Phase voltage
#: Voltage for phase 1 measured by energy meter
metering_voltage_l1 = Sensor(
    "6100_0046E500", "metering_voltage_l1", unit="V", factor=100, enabled=False
)
#: Voltage for phase 2 measured by energy meter
metering_voltage_l2 = Sensor(
    "6100_0046E600", "metering_voltage_l2", unit="V", factor=100, enabled=False
)
#: Voltage for phase 3 measured by energy meter
metering_voltage_l3 = Sensor(
    "6100_0046E700", "metering_voltage_l3", unit="V", factor=100, enabled=False
)

# AC Side - Electricity meter - Measured values - Active power feed-in
#: Active Power feed-in for phase 1 measured by energy meter
metering_active_power_feed_l1 = Sensor(
    "6100_0046E800", "metering_active_power_feed_l1", unit="W"
)
#: Active Power feed-in  for phase 2 measured by energy meter
metering_active_power_feed_l2 = Sensor(
    "6100_0046E900", "metering_active_power_feed_l2", unit="W"
)
#: Active Power feed-in  for phase 3 measured by energy meter
metering_active_power_feed_l3 = Sensor(
    "6100_0046EA00", "metering_active_power_feed_l3", unit="W"
)

# AC Side - Electricity meter - Measured values - Active power drawn
#: Active Power drawn for phase 1 measured by energy meter
metering_active_power_draw_l1 = Sensor(
    "6100_0046EB00", "metering_active_power_draw_l1", unit="W"
)
#: Active Power drawn for phase 2 measured by energy meter
metering_active_power_draw_l2 = Sensor(
    "6100_0046EC00", "metering_active_power_draw_l2", unit="W"
)
#: Active Power drawn for phase 3 measured by energy meter
metering_active_power_draw_l3 = Sensor(
    "6100_0046ED00", "metering_active_power_draw_l3", unit="W"
)
#: Current power consumption measured by energy meter
metering_current_consumption = Sensor(
    "6100_00543100", "metering_current_consumption", unit="W", enabled=False
)
#: Total power consumption measured by energy meter
metering_total_consumption = Sensor(
    "6400_00543A00",
    "metering_total_consumption",
    unit="kWh",
    factor=1000,
    enabled=False,
)

# AC Side - PV generation
#: Total kWh generated to date
pv_gen_meter = Sensor("6400_0046C300", "pv_gen_meter", unit="kWh", factor=1000)

# PV Inverter Optimizers
#: Serial number of optimizer
optimizer_serial = Sensor("6800_10852600", "optimizer_serial")
#: Power supplied by optimizer
optimizer_power = Sensor("6100_40652A00", "optimizer_power", unit="W")
#: Current supplied by optimizer
optimizer_current = Sensor(
    "6100_40652900", "optimizer_current", unit="A", factor=1000, enabled=False
)
#: Voltage supplied by optimizer
optimizer_voltage = Sensor(
    "6100_40652800", "optimizer_voltage", unit="V", factor=100, enabled=False
)
#: Temperature of optimizer
optimizer_temp = Sensor(
    "6100_40652B00", "optimizer_temp", unit="°C", factor=10, enabled=False
)


# Battery (inverter) - Battery (general parameters)
#: Total battery state of charge
battery_soc_total = Sensor("6100_00295A00", "battery_soc_total", unit="%")
#: State of charge battery A
battery_soc_a = Sensor("6100_00498F00_0", "battery_soc_a", unit="%", enabled=False)
#: State of charge battery B
battery_soc_b = Sensor("6100_00498F00_1", "battery_soc_b", unit="%", enabled=False)
#: State of charge battery C
battery_soc_c = Sensor("6100_00498F00_2", "battery_soc_c", unit="%", enabled=False)
#: Voltage battery A
battery_voltage_a = Sensor(
    "6100_00495C00_0", "battery_voltage_a", unit="V", factor=100, enabled=False
)
#: Voltage battery B
battery_voltage_b = Sensor(
    "6100_00495C00_1", "battery_voltage_b", unit="V", factor=100, enabled=False
)
#: Voltage battery C
battery_voltage_c = Sensor(
    "6100_00495C00_2", "battery_voltage_c", unit="V", factor=100, enabled=False
)
#: Current battery A
battery_current_a = Sensor(
    "6100_40495D00_0", "battery_current_a", unit="A", factor=1000
)
#: Current battery B
battery_current_b = Sensor(
    "6100_40495D00_1", "battery_current_b", unit="A", factor=1000
)
#: Current battery C
battery_current_c = Sensor(
    "6100_40495D00_2", "battery_current_c", unit="A", factor=1000
)
#: Temperature battery A
battery_temp_a = Sensor("6100_40495B00_0", "battery_temp_a", unit="°C", factor=10)
#: Temperature battery B
battery_temp_b = Sensor("6100_40495B00_1", "battery_temp_b", unit="°C", factor=10)
#: Temperature battery C
battery_temp_c = Sensor("6100_40495B00_2", "battery_temp_c", unit="°C", factor=10)
#: Battery status operating mode
battery_status_operating_mode = Sensor(
    "6180_08495E00",
    "battery_status_operating_mode",
    path=JMESPATHS_TAG,
    l10n_translate=True,
)

# Battery (inverter) - Diagnosis
#: Total battery capacity
battery_capacity_total = Sensor("6100_00696E00", "battery_capacity_total", unit="%")
#: Capacity battery A
battery_capacity_a = Sensor(
    "6100_00499100_0", "battery_capacity_a", unit="%", enabled=False
)
#: Capacity battery B
battery_capacity_b = Sensor(
    "6100_00499100_1", "battery_capacity_b", unit="%", enabled=False
)
#: Capacity battery C
battery_capacity_c = Sensor(
    "6100_00499100_2", "battery_capacity_c", unit="%", enabled=False
)

# Battery (inverter) - Charge (voltage)
#: Charging voltage battery A
battery_charging_voltage_a = Sensor(
    "6102_00493500_0", "battery_charging_voltage_a", unit="V", factor=100, enabled=False
)
#: Charging voltage battery B
battery_charging_voltage_b = Sensor(
    "6102_00493500_1", "battery_charging_voltage_b", unit="V", factor=100, enabled=False
)
#: Charging voltage battery C
battery_charging_voltage_c = Sensor(
    "6102_00493500_2", "battery_charging_voltage_c", unit="V", factor=100, enabled=False
)

# Battery (inverter) - Battery charge (power & energy)
#: Total charging power
battery_power_charge_total = Sensor(
    "6100_00496900", "battery_power_charge_total", unit="W"
)
#: Charging power battery A
battery_power_charge_a = Sensor(
    "6100_00499300_0", "battery_power_charge_a", unit="W", enabled=False
)
#: Charging power battery B
battery_power_charge_b = Sensor(
    "6100_00499300_1", "battery_power_charge_b", unit="W", enabled=False
)
#: Charging power battery C
battery_power_charge_c = Sensor(
    "6100_00499300_2", "battery_power_charge_c", unit="W", enabled=False
)
#: Total charge
battery_charge_total = Sensor(
    "6400_00496700", "battery_charge_total", unit="kWh", factor=1000
)
#: Charge battery A
battery_charge_a = Sensor(
    "6400_00499500_0", "battery_charge_a", unit="kWh", factor=1000, enabled=False
)
#: Charge battery B
battery_charge_b = Sensor(
    "6400_00499500_1", "battery_charge_b", unit="kWh", factor=1000, enabled=False
)
#: Charge battery C
battery_charge_c = Sensor(
    "6400_00499500_2", "battery_charge_c", unit="kWh", factor=1000, enabled=False
)

# Battery (inverter) - Battery discharge (power & energy)
#: Total discharging power
battery_power_discharge_total = Sensor(
    "6100_00496A00", "battery_power_discharge_total", unit="W"
)
#: Disharging power battery A
battery_power_discharge_a = Sensor(
    "6100_00499400_0", "battery_power_discharge_a", unit="W", enabled=False
)
#: Disharging power battery B
battery_power_discharge_b = Sensor(
    "6100_00499400_1", "battery_power_discharge_b", unit="W", enabled=False
)
#: Disharging power battery C
battery_power_discharge_c = Sensor(
    "6100_00499400_2", "battery_power_discharge_c", unit="W", enabled=False
)
#: Total discharge
battery_discharge_total = Sensor(
    "6400_00496800", "battery_discharge_total", unit="kWh", factor=1000
)
#: Discharge battery A
battery_discharge_a = Sensor(
    "6400_00499600_0", "battery_discharge_a", unit="kWh", factor=1000, enabled=False
)
#: Discharge battery B
battery_discharge_b = Sensor(
    "6400_00499600_1", "battery_discharge_b", unit="kWh", factor=1000, enabled=False
)
#: Discharge battery C
battery_discharge_c = Sensor(
    "6400_00499600_2", "battery_discharge_c", unit="kWh", factor=1000, enabled=False
)

# Device Parameters
# Type Label - Type Label
#: Device serial number
serial_number = Sensor("6800_00A21E00", "serial_number")
#: Device name
device_name = Sensor("6800_10821E00", "device_name")
#: Device type
device_type = Sensor(
    "6800_08822000", "device_type", path=JMESPATHS_TAG, l10n_translate=True
)
#: Device manufactorer
device_manufacturer = Sensor(
    "6800_08822B00", "device_manufacturer", path=JMESPATHS_TAG, l10n_translate=True
)
#: Device software version
device_sw_version = Sensor("6800_00823400", "device_sw_version")

# Device - Inverter
#: Power limit of the Inverter
inverter_power_limit = Sensor("6800_00832A00", "inverter_power_limit", unit="W")

# System communication - Meter on Speedwire
#: Serial number of energy meter
energy_meter = Sensor("6800_008AA300", "energy_meter")


sensor_map = {
    DEVCLASS_INVERTER: [
        status,
        pv_power_a,
        pv_power_b,
        pv_power_c,
        pv_voltage_a,
        pv_voltage_b,
        pv_voltage_c,
        pv_current_a,
        pv_current_b,
        pv_current_c,
        grid_power,
        frequency,
        current_l1,
        current_l2,
        current_l3,
        voltage_l1,
        voltage_l2,
        voltage_l3,
        power_l1,
        power_l2,
        power_l3,
        total_yield,
        daily_yield,
        pv_gen_meter,
    ],
    OPTIMIZERS_VIA_INVERTER: [
        optimizer_power,
        optimizer_current,
        optimizer_voltage,
        optimizer_temp,
    ],
    ENERGY_METER_VIA_INVERTER: [
        metering_power_supplied,
        metering_power_absorbed,
        metering_frequency,
        metering_total_yield,
        metering_total_absorbed,
        metering_current_l1,
        metering_current_l2,
        metering_current_l3,
        metering_voltage_l1,
        metering_voltage_l2,
        metering_voltage_l3,
        metering_active_power_feed_l1,
        metering_active_power_feed_l2,
        metering_active_power_feed_l3,
        metering_active_power_draw_l1,
        metering_active_power_draw_l2,
        metering_active_power_draw_l3,
        metering_current_consumption,
        metering_total_consumption,
    ],
    DEVCLASS_BATTERY: [
        battery_voltage_a,
        battery_voltage_b,
        battery_voltage_c,
        battery_charging_voltage_a,
        battery_charging_voltage_b,
        battery_charging_voltage_c,
        battery_current_a,
        battery_current_b,
        battery_current_c,
        inverter_power_limit,
        battery_power_charge_total,
        battery_power_charge_a,
        battery_power_charge_b,
        battery_power_charge_c,
        battery_power_discharge_total,
        battery_power_discharge_a,
        battery_power_discharge_b,
        battery_power_discharge_c,
        grid_reactive_power,
        grid_reactive_power_l1,
        grid_reactive_power_l2,
        grid_reactive_power_l3,
        grid_apparent_power,
        grid_apparent_power_l1,
        grid_apparent_power_l2,
        grid_apparent_power_l3,
        grid_power_factor,
        grid_power_factor_excitation,
        battery_charge_total,
        battery_charge_a,
        battery_charge_b,
        battery_charge_c,
        battery_discharge_total,
        battery_discharge_a,
        battery_discharge_b,
        battery_discharge_c,
        battery_soc_total,
        battery_soc_a,
        battery_soc_b,
        battery_soc_c,
        battery_capacity_total,
        battery_capacity_a,
        battery_capacity_b,
        battery_capacity_c,
        battery_temp_a,
        battery_temp_b,
        battery_temp_c,
        insulation_residual_current,
        inverter_condition,
        operating_status_general,
        battery_status_operating_mode,
        grid_relay_status,
        grid_connection_status,
        inverter_system_init,
        grid_power,
        voltage_l1,
        voltage_l2,
        voltage_l3,
        current_l1,
        current_l2,
        current_l3,
        current_total,
        frequency,
        status,
    ],
    DEVCLASS_ENERGY_METER: [
        status,
        grid_power,
        frequency,
        current_l1,
        current_l2,
        current_l3,
        voltage_l1,
        voltage_l2,
        voltage_l3,
        power_l1,
        power_l2,
        power_l3,
    ],
    DEVICE_INFO: [
        serial_number,
        device_name,
        device_type,
        device_manufacturer,
        device_sw_version,
    ],
}
