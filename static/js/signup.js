$(document).ready(function (params) {
  $(".signup-btn").click(function () {
    let name = $(".name").val();
    let email = $(".mail").val();
    let ps = $(".ps").val();
    let cps = $(".cps").val();

    let data = {
      username: name,
      email: email,
      password1: ps,
      password2: cps,
    };

    ajaxCall("/signup_auth/", "POST", data, function doneFunction(response) {
      if (response.result == true) {
        window.location.href = "/login/";
      } else if (response == false) alert("ajax error occurred");
      else alert("error");
    });
  });
});
