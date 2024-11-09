SELECT * FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28;

SELECT * FROM crime_scene_reports WHERE id = 297;
SELECT * FROM crime_scene_reports WHERE id = 295;

SELECT * FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28;

SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute < 30
AND activity = 'exit';

SELECT * FROM atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Legget Street'
AND atm_transactions.transaction_type = 'withdraw';

SELECT name FROM people
WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55');

SELECT * FROM flights WHERE year = 2021 AND month = 7 AND day = 29;
SELECT * FROM airports;
SELECT * FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36;

SELECT * FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND caller IN (SELECT phone_number FROM people WHERE name = 'Bruce';

SELECT * FROM phone_calls WHERE caller = '(367) 555-5533' AND duration < 60 AND year = 2021 AND month = 7 AND day = 28;

SELECT name FROM people WHERE phone_number = '(375) 555-8161';
