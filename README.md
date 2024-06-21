const currentDate = new Date();
const datePart = currentDate.toISOString().slice(0, 10);
const timePart = currentDate.getHours().toString().padStart(2, '0') + ':' +
                 currentDate.getMinutes().toString().padStart(2, '0') + ':' +
                 currentDate.getSeconds().toString().padStart(2, '0');
const dateTimeString = `${datePart} ${timePart}`;
