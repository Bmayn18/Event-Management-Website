# LAN-PLAN

## Levi | Front-end

## Blake | Database
Account
    id
    FirstName
    Lastname
    Username
    Password
    Street
    Email
    Phone
    <Address>>
    [Bookings]
Event
    id
    <Venue>
    <creator>
    Name
    Link [Exterma; e.g. Artist webpage]
    Artist
    Genre
    Date
    Starttime
    BookedTickets {max = venue.capacity, user cannot change venue to one with a lower capacity than BookedTickets }
    Image
    Description
    Price
    Status (Sold out | open | cancelled | unpublished)
    [Comments]
Comment
    Id
    <User>
    <event>
    Createdate
    [Mentions] { stretch }
Booking
    id
    Purchasedtickets
    Bookeddate
    <User>
    <event>
Venue
    Id
    Name
    Link
    Capacity
    <Address>
Address
    id
    Type (Venue/Residential)
    Street
    Suburb {potentially regex generated}
    Postcode {Potentially Regex Generated}

## Yash | DB

## Drew | Forms
