// Select the button and paragraph elements
const button = document.querySelector('button');
const paragraph = document.querySelector('p');

// Add a click event listener to the button
button.addEventListener('click', () => {
  // Change the text of the paragraph
  paragraph.textContent = 'Button clicked!';
});
