#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define SS_PIN  5   // ESP32 pin GPIO5 
#define RST_PIN 27  // ESP32 pin GPIO27 
#define RELAY_PIN 15 // ESP32 pin GPIO15

MFRC522 rfid(SS_PIN, RST_PIN);

// Define the UID values for your cards
byte card1UID[] = {0x13, 0xDC, 0x56, 0xFB};
byte card2UID[] = {0xA3, 0x0E, 0x48, 0xF6};

bool roomOccupied = false;
bool personLeft = false;
byte currentOccupantUID[4] = {0}; // To store the UID of the current occupant
byte lastOccupantUID[4] = {0};    // To store the UID of the person who left

void setup() {
  Serial.begin(9600);
  SPI.begin(); // init SPI bus
  rfid.PCD_Init(); // init MFRC522
  lcd.init();                       // Initialize the LCD
  lcd.backlight();                  // Turn on the backlight
  lcd.clear();                      // Clear the LCD screen
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);   // Initialize relay as ON (lights initially ON)
  lcd.print("Welcome to EMS");
  delay(1000);
  lcd.clear();
  Serial.println("Tap an RFID/NFC tag on the RFID-RC522 reader");
}

void loop() {
  if (rfid.PICC_IsNewCardPresent()) { // new tag is available
    if (rfid.PICC_ReadCardSerial()) { // NUID has been read
      MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
      Serial.print("RFID/NFC Tag Type: ");
      Serial.println(rfid.PICC_GetTypeName(piccType));

      // print UID in Serial Monitor in the hex format
      Serial.print("UID:");
      for (int i = 0; i < rfid.uid.size; i++) {
        Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(rfid.uid.uidByte[i], HEX);
        // Store the UID for later comparison
        currentOccupantUID[i] = rfid.uid.uidByte[i];
      }
      Serial.println();

      // Check if both persons have entered the room
      if (roomOccupied && compareCard(currentOccupantUID, card1UID) && compareCard(currentOccupantUID, card2UID)) {
        // Restart the whole logic
        roomOccupied = false;
        for (int i = 0; i < 4; i++) {
          lastOccupantUID[i] = 0;
        }
      }

      // Check if the room is currently occupied
      if (roomOccupied) {
        // Compare the UID with the last occupant's UID
        if (compareCard(currentOccupantUID, lastOccupantUID)) {
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("Card");
          lcd.setCursor(0, 1);
          lcd.print("Room Occupied");
          digitalWrite(RELAY_PIN, LOW); // Turn off the relay (lights off)
          delay(2000);
        } else {
          // New person entered the room
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("Card");
          lcd.setCursor(0, 1);
          lcd.print("Room Vacant");
          roomOccupied = false;
          digitalWrite(RELAY_PIN, HIGH); // Turn on the relay (lights on)
          delay(2000);
        }
      } else {
        // Room is vacant, store the UID
        for (int i = 0; i < 4; i++) {
          lastOccupantUID[i] = currentOccupantUID[i];
        }
        roomOccupied = true;
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Card");
        lcd.setCursor(0, 1);
        lcd.print("Room Occupied");
        digitalWrite(RELAY_PIN, LOW); // Turn off the relay (lights off)
        delay(2000);
      }

      rfid.PICC_HaltA(); // halt PICC
      rfid.PCD_StopCrypto1(); // stop encryption on PCD
    }
  }
}

// Function to compare RFID card with predefined values
bool compareCard(byte card[], byte storedCard[]) {
  for (int i = 0; i < 4; i++) {
    if (card[i] != storedCard[i]) {
      return false;
    }
  }
  return true;
}
