// Source: https://www.geeksforgeeks.org/realtime-chat-app-using-django/
const chatSocket = new WebSocket("wss://" + window.location.host + "/");
chatSocket.onopen = function () {
  let div = document.createElement("div");
  div.innerHTML = "Connected to chat!";
  document.querySelector("#id_chat_item_container").appendChild(div);
};
chatSocket.onclose = function () {
  let div = document.createElement("div");
  div.innerHTML = ```Connection to chat has closed to inactivity!
  <br/>Refresh page to reconnect```;
  document.querySelector("#id_chat_item_container").appendChild(div);
};
document.querySelector("#id_message_send_input").focus();
document.querySelector("#id_message_send_input").onkeyup = function (e) {
  if (e.keyCode == 13) {
    document.querySelector("#id_message_send_button").click();
  }
};
document.querySelector("#id_message_send_button").onclick = function () {
  let messageInput = document.querySelector(
    "#id_message_send_input"
  ).value;
  chatSocket.send(JSON.stringify({
    message: messageInput,
    username: username
  }));
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  let div = document.createElement("div");
  div.innerHTML = data.username + " : " + data.message;
  document.querySelector("#id_message_send_input").value = "";
  document.querySelector("#id_chat_item_container").appendChild(div);
};