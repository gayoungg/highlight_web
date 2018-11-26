var step1 = document.getElementById("step1");
var step2 = document.getElementById("step2");
var step3 = document.getElementById("step3");

window.onload = function () {
    setTimeout(function () {
        step1.classList.remove('active');
        step2.classList.add('active');
    }, 10000);

    setTimeout(function () {
        step2.classList.remove('active');
        step3.classList.add('active');
    }, 20000);

        setTimeout(function () {
        location.href = "../result/";
    }, 30000);
}