MESSAGE="""
DEAR {},

This email is to confirm your booking on {}.

FLIGHT DETAILS

    FLIGHT NUMBERS: ({},{})

    DEPATURE DATES: ({},{})

     DEPARTURE      ARRIVAL
            {}               {}
         {}         {}
            {}               {}
         {}         {}
    DURATIONS: ({},{})

    SEATS: ({},{})



PASSENGER DETAILS

    PASSPORT NUMBER: {}
    NAME: {}
    DOB: {}
    SEX: {}
    PHONE: {}
    PNR: : {}

Further details of your bookings are listed below:

BOOKING ID: {}
TOTAL FARE: {}

Amenities: Complementary Wifi,InFlight Entertainment,
            Airport Lounge,Inflight Gym

Baggage info: Free check-in baggage allowance is 30 kg per adult & child. 
                Each bag must not exceed 32 kg and overall dimensions of 
                checked baggage should not exceed 62 inches. 

Cancellation policy: Cancellations made 7 days or more in advance of 
                    the check-in day, will receive a 100% refund. 
                    Cancellations made within 3 - 6 days will incur 
                    a 20% fee. Cancellations made within 48 hours 
                    to the check-in day will incur a 30% fee.
                    Cancellation made within 24 Hrs to the check-in 
                    day will incur a 50% fee.

ABOUT THIS TRIP: 

            Use your Trip ID for all communication

            Check-in counters for International flights 
                close 75 minutes before departure

            Your carry-on baggage shouldn't weigh more than 7kgs

            Carry photo identification, you will need it as proof of 
                identity while checking-in

            Kindly ensure that you have the relevant visa, immigration 
                clearance and travel with a passport, with a validity of at least 6 months.

If you have any inqueries, Please do not hesitate to contact
or call the AIRLINE directly

We are looking forward to your visit and hope that you enjoy your stay
Best regards
""".format('NAVEED', "datetime.date(2020, 10, 2)", 'G310', 'G281', '2020-11-11', '2020-11-12', 'DXB', 'SYD', '00:00:00', '13:45:00', 'SYD', 'BOM', '13:45:00', '01:45:00', '13:45:00', '12:00:00', 'A35', 'A35', '12345678', 'NAVE', '2003-04-20', 'M', '+971558004998', 3398, 3398, 2205)
print(MESSAGE)