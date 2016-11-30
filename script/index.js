document.getElementById("loginButton").addEventListener("click",function (ev) {
    ev.preventDefault();
    var user=document.getElementById("usernameField").value;
    var password=document.getElementById("passwordField").value;
    console.log(user+" "+password);
    if(user=="genovefa" && password=="123"){
        document.location="home-librarian.html";
    }else if(user=="jdol" && password=="123"){
        document.location="books-user.html";
    }else{
        document.getElementById("info").innerHTML="INVALID CREDENTIALS !";
    }
})
