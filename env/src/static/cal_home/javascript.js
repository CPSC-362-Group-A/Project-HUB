var quotes = [
    "<p>It\'s only after you\'ve stepped outside your comfort zone that you begin to change, grow, and transform. \-Roy T. Bennett</p>",
    "<p>Do what is right, not what is easy nor what is popular. \-Roy T. Bennett, The Light in the Heart</p>",
    "<p>Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. \-Roy T. Bennett, The Light in the Heart</p>",
    "<p>Be yourself; everyone else is already taken.\― Oscar Wilde</p>",
    "<p>Be the change that you wish to see in the world.\― Mahatma Gandhi</p>",
    "<p>Live as if you were to die tomorrow. Learn as if you were to live forever.\― Mahatma Gandhi</p>"
  ]
  
  
  function newQuote() {
    var randomNumber = Math.floor(Math.random() * (quotes.length));
    document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
  }
  
  function saveQuote() {
     var getInput = document.getElementById('quoteDisplay').innerHTML;
     localStorage.setItem("setQuote",getInput);
  
  }
  
  function useQuote() {
       var quote = localStorage.getItem("setQuote");
  if (quote == null)
  {
      quote = "<p>Click the button for a quote.</p>"
          document.getElementById('quoteDisplay').innerHTML = quote;
  }
  else
  {
          document.getElementById('quoteDisplay').innerHTML = quote;
  }
  }