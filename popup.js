document.addEventListener('DOMContentLoaded', function() {
    var readButton = document.getElementById('read-button');
    var textToRead = document.getElementById('text-to-read');
  
    readButton.addEventListener('click', function() {
      var utterance = new SpeechSynthesisUtterance(textToRead.value);
      window.speechSynthesis.speak(utterance);
    });
  });
  