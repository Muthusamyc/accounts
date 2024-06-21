const currentDate = new Date();
const options = {
  timeZone: 'Asia/Kolkata', // Set the timezone to UTC+05:30 (Chennai, Kolkata, Mumbai, New Delhi)
  hour12: false, // Use 24-hour format
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit'
};

this.today = currentDate.toLocaleString('en-IN', options);
