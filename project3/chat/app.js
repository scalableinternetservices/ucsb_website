function date_format(timestamp) {
    var date = new Date(timestamp * 1000);
    return (
        date.toLocaleDateString("en-US") +
        " " +
        date.toLocaleTimeString("en-US")
    );
}

function login() {
    var request = new XMLHttpRequest();
    var form = new FormData();
    form.append("password", password.value);
    form.append("username", username.value);
    sessionStorage.url = url.value;
    request.open("POST", sessionStorage.url + "/login");
    request.onreadystatechange = function() {
        if (this.readyState != 4) return;
        if (this.status === 201) {
            login_modal.style.display = "none";
            password.value = "";
            username.value = "";
            sessionStorage.accessToken = JSON.parse(this.responseText).token;
            start_stream();
        } else if (this.status === 403) {
            alert("Invalid username or password");
        } else {
            alert(this.status + " failure to /login");
        }
    };
    request.send(form);
}

function handle_connect() {
    message.disabled = false;
    message.value = "";
    title.classList.remove("disconnected");
}

function handle_disconnect() {
    message.disabled = true;
    message.value = "Please connect to send messages.";
    title.classList.add("disconnected");
    users = new Set();
    update_users();
}

function output(node) {
    var element = document.createElement("div");
    element.appendChild(node);
    chat.appendChild(element);
    chat.scrollTop = chat.scrollHeight - chat.clientHeight;
}

function show_login() {
    url.value = sessionStorage.url || "http://chat.cs291.com";
    login_modal.style.display = "block";
}

function start_stream() {
    stream = new EventSource(
        sessionStorage.url + "/stream/" + sessionStorage.accessToken
    );

    stream.addEventListener(
        "Disconnect",
        function(event) {
            stream.close();
            handle_disconnect();
            delete sessionStorage.accessToken;
            show_login();
        },
        false
    );

    stream.addEventListener(
        "Join",
        function(event) {
            var data = JSON.parse(event.data);
            users.add(data.user);
            update_users();
            console.log(data);
            output(
                document.createTextNode(
                    date_format(data["created"]) + " JOIN: " + data.user
                )
            );
        },
        false
    );

    stream.addEventListener(
        "Message",
        function(event) {
            var data = JSON.parse(event.data);
            console.log(data);
            output(
                document.createTextNode(
                    date_format(data["created"]) +
                        " (" +
                        data.user +
                        ") " +
                        data.message
                )
            );
        },
        false
    );

    stream.addEventListener(
        "Part",
        function(event) {
            var data = JSON.parse(event.data);
            users.delete(data.user);
            update_users();
            console.log(data);
            output(
                document.createTextNode(
                    date_format(data["created"]) + " PART: " + data.user
                )
            );
        },
        false
    );

    stream.addEventListener(
        "ServerStatus",
        function(event) {
            var data = JSON.parse(event.data);
            console.log(data);
            output(
                document.createTextNode(
                    date_format(data["created"]) + " STATUS: " + data.status
                )
            );
        },
        false
    );

    stream.addEventListener(
        "Users",
        function(event) {
            handle_connect();
            users = new Set(JSON.parse(event.data).users);
            update_users();
        },
        false
    );

    stream.addEventListener(
        "error",
        function(event) {
            handle_disconnect();
            if (event.target.readyState == 2) {
                delete sessionStorage.accessToken;
                show_login();
            } else {
                console.log("Disconnected, retrying");
            }
        },
        false
    );
}

function update_users() {
    user_list.innerHTML = "";
    for (let item of users) {
        var element = document.createElement("li");
        element.appendChild(document.createTextNode(item));
        user_list.appendChild(element);
    }
}

var chat = document.getElementById("chat");
var login_modal = document.getElementById("login-modal");
var message = document.getElementById("message");
var password = document.getElementById("password");
var stream = null;
var title = document.getElementById("title");
var url = document.getElementById("url");
var user_list = document.getElementById("users");
var username = document.getElementById("username");
var users = new Set();

login_modal.addEventListener("keyup", function(event) {
    if (sessionStorage.accessToken !== undefined || event.keyCode !== 13)
        return;
    login();
});

message.addEventListener("keyup", function(event) {
    if (sessionStorage.accessToken === undefined || event.keyCode !== 13)
        return;
    event.preventDefault();
    if (message.value === "") return;

    var form = new FormData();
    form.append("message", message.value);

    var request = new XMLHttpRequest();
    request.open("POST", sessionStorage.url + "/message");
    request.setRequestHeader(
        "Authorization",
        "Bearer " + sessionStorage.accessToken
    );
    request.send(form);

    message.value = "";
});

if (sessionStorage.accessToken === undefined) {
    handle_disconnect();
    show_login();
} else {
    start_stream();
}
