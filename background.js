chrome.tabs.onCreated.addListener(function() {
    chrome.tts.speak("You are an unsustainable bitch");
  });
  
  chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.status === 'complete') {
      var message = 'You are visiting: ' + tab.title;
      var options = {
        type: 'basic',
        iconUrl: 'icon.png',
        title: 'New Visit',
        message: message
      };
      chrome.notifications.create(options);
    }
  });
  