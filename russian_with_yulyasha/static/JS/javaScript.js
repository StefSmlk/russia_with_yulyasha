let list = document.getElementsByClassName('square')
let anotherList = document.getElementsByClassName('carousel-caption')
for (let i = 0; i<list.length; i++){
    list[i].addEventListener('mouseenter', function () {
        this.classList.add('frame')
    })
    anotherList[i].addEventListener('mouseenter', function () {
        list[i].classList.add('frame')
    })
    list[i].addEventListener('mouseleave', function () {
        this.classList.remove('frame')
    })
    anotherList[i].addEventListener('mouseleave', function () {
        list[i].classList.remove('frame')
    })
}


// let emList = document.getElementsByTagName('span')
// setInterval(function () {
//     for (let i=2; i<11; i++){
//         emList[i].classList.toggle('span-stripe-em')
//     }
// }, 5000)