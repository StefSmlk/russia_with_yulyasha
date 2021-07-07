let list = document.getElementsByClassName('square');
let anotherList = document.getElementsByClassName('carousel-caption');
for (let i = 0; i<list.length; i++){
    list[i].addEventListener('mouseenter', function () {
        this.classList.add('frame');
    });
    anotherList[i].addEventListener('mouseenter', function () {
        list[i].classList.add('frame');
    });
    list[i].addEventListener('mouseleave', function () {
        this.classList.remove('frame');
    });
    anotherList[i].addEventListener('mouseleave', function () {
        list[i].classList.remove('frame');
    });
}


let video = document.getElementById('vid');
let figure = document.getElementById('figure');


figure.addEventListener('mouseenter', function () {
    video.play();
})

figure.addEventListener('mouseleave', function () {
    video.pause();
})


let cont = document.getElementsByClassName('container');

if($(window).width() < 770){
    for (let i =0; i < cont.length; i++){
        if (cont[i].classList.contains('text-end')){
            cont[i].classList.remove('text-end');
            cont[i].classList.add('text-center');
        }
    }
}