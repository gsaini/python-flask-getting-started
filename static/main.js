const source = new EventSource('https://localhost:5000/events');

/**
 * Parses the JSON string received from an event's data property.
 *
 * This function takes the `data` property from an event object, which is expected
 * to be a JSON string, and parses it into a JavaScript object. It is important to
 * ensure that the `event.data` contains valid JSON to avoid runtime errors.
 *
 * @param {Object} event - The event object containing the data to be parsed.
 * @param {string} event.data - A JSON string representing the data payload.
 * @returns {Object} The parsed JavaScript object from the JSON string.
 * @throws {SyntaxError} Throws an error if the JSON string is invalid.
 */
source.onmessage = function (event) {
  const data = JSON.parse(event.data);
  document.getElementById(
    'output'
  ).textContent += `Message: ${data.message} | Time: ${data.timestamp}\n`;
};

/**
 * Handles errors that occur during the EventSource connection.
 *
 * This function is called when an error occurs with the EventSource connection.
 * It logs the error to the console for debugging purposes.
 *
 * @param {Error} err - The error object containing information about the error.
 */
source.onerror = function (err) {
  console.error('EventSource failed:', err);
};
