/*
    An example serial code to understand the serial data format from the Ground Station receiver to the GUI.
    https://github.com/LalitK-Space/Ground_Station

    By: Lalit Kumar
     https://lalitk.space/

*/

/* -- Serial Data variables -- */
String data_Serial;
String dataToGUI;

/* -- Data To Transmit -- */

// Data_0: To indicate Start of Telemetry Packet
char startTele = '<';
// Data_17: To indicate End of the Telemetry Packet
char endTele = '>';

/* -- Data from the Flight Computer -- */
// For understanding purpose they are assigned to their respective index

// Data_1: GPS_Fix
int gpsFix = 1;
// Data_2: GPS_Quality
int gpsQuality = 2;
// Data_3: GPS_Satellites
int gpsSats = 3;
// Data_4: GPS_Altitude
float gpsAltitude = 4;
// Data_5: GPS_Latitude
float gpsLat = 5;
// Data_6: GPS_Longitude
float gpsLong = 6;
// Data_7: GPS_Speed
float gpsSpeed = 7;
// Data_8: GPS_Latitude_Direction
char gpsLatDir = '8';
// Data_9: GPS_Longitude_Direction
char gpsLongDir = '9';
// Data_10: System_Voltage_Level_5
float systemVoltage_5v = 10;
// Data_11: System_Voltage_Level_3
float systemVoltage_3v = 11;
// Data_12: Altitude
float Baro_Altitude = 12;
// Data_13: Temperature
float Baro_Temperature = 13;
// Data_14: X Axis
float orientation_X = 14;
// Data_15: Y Axis
float orientation_Y = 15;
// Data_16: Z Axis
float orientation_Z = 16;

void setup()
{
  /* --  Start Serial Communication -- */
  Serial.begin(9600); // Both GUIs are configured to receive serial data at a baud rate of 9600.
}

void loop()
{
  /* -- Telemetry Packet -- */
  data_Serial = data_Serial + startTele + "," + gpsFix + "," + gpsQuality + "," + gpsSats + "," + gpsAltitude + "," + gpsLat + "," + gpsLong + "," + gpsSpeed
                + "," + gpsLatDir + "," + gpsLongDir + "," + systemVoltage_5v + "," + systemVoltage_3v + "," + Baro_Altitude + "," + Baro_Temperature + "," +
                orientation_X + "," + orientation_Y + "," + orientation_Z + "," + endTele;

  /* Final Telemetry Packet, Ready to transmit -- */
  dataToGUI = data_Serial;

  /* -- Transmission (Serially) -- */
  Serial.println(dataToGUI);  // Transmitted with \n [Serial.println]

  /* -- Reset Telemetry Package -- */
  data_Serial = "";

  /* -- Desired Delay between Packets*/
  delay(1000);
}
