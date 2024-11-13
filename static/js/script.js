let counter = 0;

const counterElement = document.getElementById('counter');
const incrementButton = document.getElementById('incrementButton');

incrementButton.addEventListener('click', () => {
    counter++;
    counterElement.textContent = counter;
});
