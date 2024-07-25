const Customer = {
    customerName: "Daniel Efford",
    dateOfBirth: "1989-03-13",
    gender: "M",
    roomPreferences: ["Balconies", "Hot Tubs", "Room Service"],
    paymentMethod: "Cash",
    mailingAddress: {
        streetAddress: "100 Main St.",
        city: "Bay of Bays",
        province: "Newfoundland",
        postalCode: "A1A 1A1"
    },
    phoneNumber: "709-777-1234",
    checkIn: new Date("2024-07-24"),
    checkOut: new Date("2024-07-26"),

}

let getAge = (person) => {
    let thisYear = new Date().getFullYear();
    let birthYear = new Date(person).getFullYear();

    age = thisYear - birthYear;

    return age;
}

let stayDuration = () => {
    let CheckInTime = Customer.checkIn.getTime()
    let CheckOutTime = Customer.checkOut.getTime()

    durationTime = CheckOutTime - CheckInTime

    durationDays = durationTime / (1000 * 3600 * 24)

    return durationDays;
}

const customerDescription = `
            <p>
                Our guest, ${Customer.customerName}, is a ${getAge(Customer.dateOfBirth)}-year-old
                ${Customer.gender === "M" ? "male" : "female"} who prefers rooms with ${Customer.roomPreferences.join(", ")}.<br><br>
                Daniel resides at ${Customer.mailingAddress.streetAddress}, ${Customer.mailingAddress.city}, ${Customer.mailingAddress.province}, ${Customer.mailingAddress.postalCode}.<br><br>
                He will be checking in on ${Customer.checkIn.toDateString()} and checking out on ${Customer.checkOut.toDateString()}, for a stay of ${stayDuration()} days.
                <br><br>If you need to contact him, his phone number is ${Customer.phoneNumber}.
            </p>
            `

document.getElementById("customer-description").innerHTML = customerDescription;

console.log(stayDuration())