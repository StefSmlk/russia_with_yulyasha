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


let video = document.getElementById('vid')
let figure = document.getElementById('figure')


figure.addEventListener('mouseenter', function () {
    video.play()
})

figure.addEventListener('mouseleave', function () {
    video.pause()
})

