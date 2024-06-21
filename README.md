const currentDate = new Date();
const datePart = currentDate.toISOString().slice(0, 10); // Extract yyyy-mm-dd
const timePart = currentDate.toISOString().slice(11, 19); // Extract hh:mm:ss

this.today = `${datePart} ${timePart}`;
