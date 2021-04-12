var quotes = [
  "It\'s only after you\'ve stepped outside your comfort zone that you begin to change, grow, and transform. \-Roy T. Bennett",
  "Do what is right, not what is easy nor what is popular. \-Roy T. Bennett, The Light in the Heart",
  "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. \-Roy T. Bennett, The Light in the Heart"
]

function newQuote() {
  var randomNumber = Math.floor(Math.random() * (quotes.length));
  document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
}
