// function ShowPass() {
//     const btn = document.querySelector('.password__btn')
//     const input = document.querySelector('.password__input')

    
//         btn.addEventListener('click', () => {
//         btn.classList.toggle('active')

//         if (input.getAttribute('type') === 'password') {
//             input.setAttribute('type', 'text')
//         }
//         else {
//             input.setAttribute('type', 'password')
//         }
//     })
// }
// ShowPass()

let btnPass = document.querySelectorAll('.js-btn-password');

btnPass.forEach(function (btn) {
    btn.onclick = function () {
        let target = this.getAttribute('data-target'),
        inputPass = document.querySelector(target);

        if (inputPass.getAttribute('type') === 'password') {
            inputPass.setAttribute('type', 'text');
            btn.classList.add('active');
        }
        else {
            inputPass.setAttribute('type', 'password');
            btn.classList.remove('active');
        }
    }
})