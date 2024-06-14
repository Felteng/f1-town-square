// Source: https://www.geeksforgeeks.org/realtime-chat-app-using-django/
const chatAnchor = document.querySelector("#chat-anchor");
const chatSocket = new WebSocket("wss://" + window.location.host + "/");
const liveChatContainer = document.querySelector("#id-chat-item-container");


chatSocket.onopen = function () {
  let div = document.createElement("div");
  div.innerHTML = (`Connected to chat!
    <br>Anyone can see what you write but nothing 
    written will be saved in that chat after page refresh`
  );
  $(div).addClass("text-start connected-message");
  liveChatContainer.insertBefore(div, chatAnchor);
};


chatSocket.onclose = function () {
  let div = document.createElement("div");
  div.innerHTML = (`Connection to chat has closed!
    <br>Refresh page to try to reconnect`);
  $(div).addClass("text-start text-danger");
  liveChatContainer.insertBefore(div, chatAnchor);
};


/**
 * Checks if the input element (#id_message_send_input) exists,
 * which it only will if the user is logged in. This is to
 * avoid trying to add the event listeners to send_input and
 * send_button, which would result in a console error.
 * 
 * Then check if the layout matches that of 768px screen width
 * to set the input in focus.
 * That is to ensure that if the user is visitng from a mobile
 * device they are not instantly scrolled down to the bottom
 * of the homepage layout where the input is.
 */
if (document.querySelector("#id_message_send_input")) {
  if (window.matchMedia("(min-width: 768px)").matches) {
    document.querySelector("#id_message_send_input").focus();
  }


  document.querySelector("#id_message_send_input").onkeyup = function (e) {
    if (e.keyCode === 13) {
      document.querySelector("#id_message_send_button").click();
    }
  };


  document.querySelector("#id_message_send_button").onclick = function () {
    /**
     * Custom addition of 'if (/[a-z0-9]/i.test(messageInput))'
     * used to check if the input contains any alphanumerical
     * characters to not have the chat spammed with empty
     * strings of text.
     *
     * Username variable is defined in the template using DTL.
     */
    let messageInput = document.querySelector(
      "#id_message_send_input"
    ).value;
    if (/[a-z0-9]/i.test(messageInput)) {
      chatSocket.send(JSON.stringify({
        message: messageInput,
        username: username
      }));
      document.querySelector("#id_message_send_input").value = "";
    }
  };
}

chatSocket.onmessage = function (e) {
  /**
   * Adds the message received and the time of day
   * to a div that will dispaly that information
   * to users in the chat when inserted.
   */
  const data = JSON.parse(e.data);
  const date = new Date();
  let div = document.createElement("div");
  div.innerHTML = `<h6 class="mb-0">${data.username}
  <span class="message-date">
  @${date.getHours() + ":" +
  (date.getMinutes() < 10 ? "0" : "") + date.getMinutes() + ":" +
  date.getSeconds()}
  </span></h6>
  <p class="chat-message">${data.message}</p>
  <hr class="message-break">`;
  $(div).addClass("text-start");
  liveChatContainer.insertBefore(div, chatAnchor);
};