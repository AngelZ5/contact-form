document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const successAlert = document.getElementById("successAlert");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;
    const consent = document.getElementById("consent").checked;
    const queryType = document.querySelector('input[name="queryType"]:checked');

    if (
      !firstName ||
      !lastName ||
      !email ||
      !message ||
      !consent ||
      !queryType
    ) {
      //this alert ain't showing, i really dont know why
      alert("Please fill out all fields before submitting the form.");

      return;
    }

    form.reset();

    successAlert.classList.remove("d-none");

    setTimeout(function () {
      successAlert.classList.add("d-none");
    }, 3000);
  });
});
